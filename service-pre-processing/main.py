from flask import Flask, jsonify, request
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import pymongo
from config import Config

app = Flask(__name__)

client = pymongo.MongoClient(Config.MONGO_URL)
db = client.HDD
collection = db.Heart_Disease_Data


@app.route('/import-mongodb', methods=['POST'])
def import_mongodb():
    try:
        data = request.get_json()
        existing_data = []

        for item in data:
            query = {key: item[key] for key in item.keys() if key != '_id'}
            if collection.find_one(query):
                existing_data.append(item)
        
        data_to_insert = [item for item in data if item not in existing_data]
        
        if data_to_insert:
            result = collection.insert_many(data_to_insert)
            res = len(result.inserted_ids)
        else:
            res = 0

        return jsonify({"message": "Success", "documents_insert": res, "documents_existing": len(existing_data)})
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)})
    
@app.route('/pre-processing', methods=['POST'])
def pre_processing():
    try:
        data = request.get_json()
        res = do_pre_processing(data)
        return jsonify(res) 
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)})
    
def do_pre_processing(data):
    df = pd.DataFrame(data)
    # Kiểm tra thông tin về dữ liệu
    print(df.info())
    # Xem trước vài dòng đầu của dữ liệu
    print(df.head())

    print("Số lượng dữ liệu trước khi xử lý:", len(df))
    
    #Null
    df = df.dropna()

    #Age
    df = df[(df['age'] >= 29) & (df['age'] <= 77)]

    #Sex
    df = df[(df['sex'] >= 0) & (df['sex'] <= 1)]

    #Chest Pain Type
    df = df[(df['cp'] >= 0) & (df['cp'] <= 3)]

    #Resting Blood Pressure
    df = df[(df['trestbps'] >= 80) & (df['trestbps'] <= 250)]

    #Serum Cholesterol in mg/dl
    df = df[(df['chol'] >= 126) & (df['chol'] <= 564)]

    #Fasting Blood Sugar > 120 mg/dl
    df = df[(df['fbs'] >= 0) & (df['fbs'] <= 1)]

    #Resting Electrocardiographic Results
    df = df[(df['restecg'] >= 0) & (df['restecg'] <= 2)]

    #Maximum Heart Rate Achieved 
    df = df[(df['thalach'] >= 71) & (df['thalach'] <= 202)]

    #Exercise Induced Angina
    df = df[(df['exang'] >= 0) & (df['exang'] <= 1)]

    #Oldpeak (ST Depression Induced by Exercise Relative to Rest)
    df = df[(df['oldpeak'] >= 0) & (df['oldpeak'] <= 6.2)]

    #The Slope of the Peak Exercise ST Segment
    df = df[(df['slope'] >= 0) & (df['slope'] <= 2)]

    #Number of Major Vessels Colored by Fluoroscopy
    df = df[(df['ca'] >= 0) & (df['ca'] <= 3)]

    #Thal (Thallium Stress Test Result)
    df = df[(df['thal'] >= 1) & (df['thal'] <= 3)]

    print("Số lượng dữ liệu sau khi xử lý:", len(df))

    # Chuẩn hóa các cột giá trị liên tục
    # scaler = MinMaxScaler()
    # continuous_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    # df[continuous_columns] = scaler.fit_transform(df[continuous_columns])
    # print(df.head())
    df = df.drop_duplicates()

    return df.to_dict(orient='records')

@app.route('/')
def index():
    return "This is Pre-Precessing Service"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8033, debug=True)


