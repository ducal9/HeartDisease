from flask import Flask, jsonify, request
import pandas as pd
import requests
from config import Config
app = Flask(__name__)


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