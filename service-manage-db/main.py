from flask import Flask, jsonify, request
import pandas as pd
from config import Config
<<<<<<< HEAD
from flask_cors import CORS
import time
import requests
=======
import requests

>>>>>>> f70c6f510df56279bb84b08e00706d668a15befb
app = Flask(__name__)


<<<<<<< HEAD


CORS(app)  # Cho phép CORS để React/Frontend có thể truy cập


def get_and_print_data():
    """Lấy dữ liệu từ API và in ra terminal với mỗi giá trị khi có dữ liệu mới."""
    url = 'http://localhost:5000/api/latest'  # URL của Flask API
    last_data = None  # Biến lưu trữ dữ liệu cũ để so sánh
    
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Kiểm tra lỗi nếu có
            data = response.json()

            # So sánh dữ liệu mới với dữ liệu cũ
            if data != last_data:
                print("\nDữ liệu mới nhận được từ API:")
                for key, value in data.items():
                    print(f"{key}: {value}")
                
                # Cập nhật dữ liệu cũ
                last_data = data
                
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi lấy dữ liệu: {e}")
        
        # Đợi 2 giây trước khi kiểm tra dữ liệu lần nữa
        time.sleep(2)


@app.route('/reset-db', methods=['GET'])
def reset_db():
=======
@app.route('/get-file-from-email')
def get_file_from_email():
>>>>>>> f70c6f510df56279bb84b08e00706d668a15befb
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
    return "This is Import-DB Service"


if __name__ == '__main__':
     # Chạy luồng lấy dữ liệu từ React
    from threading import Thread
    data_thread = Thread(target=get_and_print_data)
    data_thread.start()
    app.run(host='127.0.0.1', port=8032)