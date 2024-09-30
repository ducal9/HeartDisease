from flask import Flask, jsonify, request, Response, send_from_directory
import pandas as pd
import requests
from config import Config
import imaplib
import email
from email.header import decode_header
import os
import shutil
from config import Config

app = Flask(__name__)


@app.route('/get-file')
def get_file():
    download_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "download")
    files = os.listdir(download_folder)
    
    if not files:
        return jsonify({"message": "No files to send."}), 404
    
    file_name = files[0]
    if not file_name.endswith('.csv'):
        return jsonify({"message": "The file is not a CSV."}), 400
    
    file_path = os.path.join(download_folder, file_name)
    try:
        df = pd.read_csv(file_path)

        columns = df.columns.tolist()
        #print(f"Columns in CSV: {columns}")

        if not all(col in df.columns for col in ['Date', 'Time', 'Heart Rate']):
            return jsonify({
                "message": "Missing required columns (Date, Time, Heart).",
                "columns": ', '.join(columns)  # Chuyển danh sách columns thành chuỗi
            }), 400
        result = df[['Date', 'Time', 'Heart Rate']].to_dict(orient='records')
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error reading CSV file: {str(e)}"}), 500
    

@app.route('/get-email')
def get_email():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(Config.EMAIL, Config.PASSWORD)
    mail.select("inbox")
    
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()
    
    subjects = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    download_folder = os.path.join(current_dir, "download")
    
    if os.path.exists(download_folder):
        shutil.rmtree(download_folder)
    os.makedirs(download_folder)
    
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                if "My Heart Rate" in subject:
                    subjects.append(subject)
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_disposition() == "attachment":
                                filename = part.get_filename()
                                if filename:
                                    filepath = os.path.join(download_folder, filename)
                                    with open(filepath, "wb") as f:
                                        f.write(part.get_payload(decode=True))
        mail.store(email_id, '+FLAGS', '\Seen')
    
    mail.logout()

    return jsonify(subjects)


@app.route('/import-db', methods=['POST'])
def import_db():
    try:
        file = request.files['file']
        df = pd.read_csv(file)
        
        data = df.to_dict(orient='records')
        url_pre = Config.SERVICE_PRE_PROCESSING + "/pre-processing"

        res_pre = requests.post(url_pre, json=data)
        if res_pre.status_code == 200:
            try:
                data = res_pre.json()
                url_import = Config.SERVICE_PRE_PROCESSING + "/import-mongodb"
                res_import = requests.post(url_import, json=data)
                return jsonify(res_import.json())
            except ValueError:
                return res_pre.text
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)})

@app.route('/')
def index():
    return "This is Email Service"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8072, debug=True)