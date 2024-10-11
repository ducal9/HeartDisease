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
    try:
        # Lấy port từ Config
        pre_processing_url = Config.SERVICE_PRE_PROCESSING+"/pre-processing"
        
        # Dữ liệu giả lập để gửi request (nếu cần)
        data = [
            {
                "age": 45,
                "sex": 1,
                "cp": 3,
                "trestbps": 130,
                "chol": 250,
                "fbs": 0,
                "restecg": 1,
                "thalach": 180,
                "exang": 0,
                "oldpeak": 2.3,
                "slope": 1,
                "ca": 0,
                "thal": 2
            }
        ]

        # Gửi request POST tới API /pre-processing
        response = requests.post(pre_processing_url, json=data)

        # Kiểm tra xem request có thành công không
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"message": "Có lỗi xảy ra khi gọi /pre-processing", "status_code": response.status_code})
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)})


@app.route('/')
def index():
    return "This is API Service"


if __name__ == '__main__':
     # Chạy luồng lấy dữ liệu từ React
    from threading import Thread
    data_thread = Thread(target=get_and_print_data)
    data_thread.start()
    app.run(host='127.0.0.1', port=8032)