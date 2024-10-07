from flask import Flask, jsonify, request
import pandas as pd
from config import Config
import requests

app = Flask(__name__)


@app.route('/get-file-from-email')
def get_file_from_email():
    try:
        url = Config.SERVICE_EMAIL_DOWNLOAD+"/get-file"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({"status": "success", "data": data}), 200
        else:
            return jsonify({"status": "error", "message": "Failed to fetch file from email"}), response.status_code
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/get-report')
def get_report():
    return "Lấy báo cáo từ service-prediction"


@app.route('/')
def index():
    return "This is API Service"


if __name__ == '__main__':
     # Chạy luồng lấy dữ liệu từ React
    from threading import Thread
    data_thread = Thread(target=get_and_print_data)
    data_thread.start()
    app.run(host='127.0.0.1', port=8032)