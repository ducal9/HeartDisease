from flask import Flask, jsonify, request
import pandas as pd
import pymongo
from config import Config


app = Flask(__name__)
client = pymongo.MongoClient(Config.MONGO_URL)
db = client.PRE
collection = db.Heart_Disease_Data


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
    app.run(host='127.0.0.1', port=8032)