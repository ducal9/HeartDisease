from flask import Flask, jsonify, request, Response
import pandas as pd
import requests
from config import Config
import imaplib
import email
from email.header import decode_header


app = Flask(__name__)

# Thông tin tài khoản Gmail của bạn
username = "hdp24092000@gmail.com"
password = "ccag kfnl taro kjiv"


def connect_to_imap(username, password):
    try:
        # Kết nối đến máy chủ IMAP
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        # Đăng nhập
        mail.login(username, password)
        print("Login successful!")

        # Chọn thư mục INBOX
        mail.select("INBOX")
        print("Selected INBOX successfully!")

        return mail
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
        return None


def fetch_emails(mail):
    # Tìm tất cả email trong thư mục INBOX
    status, messages = mail.search(None, "ALL")

    # Chia nhỏ danh sách ID email
    email_ids = messages[0].split()

    for email_id in email_ids:
        # Lấy email theo ID
        res, msg = mail.fetch(email_id, "(RFC822)")
        msg = msg[0][1]

        # Phân tích cú pháp email
        msg = email.message_from_bytes(msg)

        # Lấy tiêu đề email
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')

        print(f"Email ID: {email_id.decode()}, Subject: {subject}")


@app.route('/get-email')
def get_email():
    mail = connect_to_imap(username, password)
    if mail:
        fetch_emails(mail)
        # Đóng kết nối
        mail.logout()
    return "Success", 200


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
    return "This is Temp-Import-DB Service"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8072, debug=True)