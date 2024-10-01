from flask import Flask, jsonify, request
import pandas as pd
import pymongo
from config import Config
from flask_cors import CORS
import time
import requests
app = Flask(__name__)
client = pymongo.MongoClient(Config.MONGO_URL)
db = client.PRE
collection = db.Heart_Disease_Data




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
    try:
        collection.delete_many({})
        return jsonify({"message": "Dữ liệu trong Heart_Disease_Data đã được xóa!"})
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)})


@app.route('/import-db', methods=['POST'])
def import_db():
    try:
        file = request.files['file']
        df = pd.read_csv(file)
        data = df.to_dict(orient='records')
        collection.insert_many(data)
        return jsonify({"message": "Dữ liệu đã được nhập thành công vào MongoDB!"})
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)})


@app.route('/export-db')
def export_db():
    return "Đã xuất file thành công"


@app.route('/')
def index():
    return "This is Import-DB Service"


if __name__ == '__main__':
     # Chạy luồng lấy dữ liệu từ React
    from threading import Thread
    data_thread = Thread(target=get_and_print_data)
    data_thread.start()
    app.run(host='127.0.0.1', port=8032)