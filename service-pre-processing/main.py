from flask import Flask, jsonify, request
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from config import Config
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://mcv:mcv@cluster0.cena4mj.mongodb.net/')  # Sửa URL nếu cần
db = client['HD_DB']  # Đặt tên database MongoDB
collection = db['Data']  # Đặt tên collection MongoDB

@app.route('/pre-processing', methods=['POST'])
def pre_processing():
    try:
        data = request.get_json()
        res = do_pre_processing(data)
        return jsonify(res) 
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)})

@app.route('/pre-processing-v2', methods=['POST'])
def pre_processing_v2():
    try:
        data = request.get_json()
        res = do_pre_processing(data)
        
        # Chuyển đổi các cột liên tục bằng MinMaxScaler
        scaler = MinMaxScaler()
        continuous_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
        res_df = pd.DataFrame(res)
        processed_data = res_df.to_dict(orient='records')
        collection.delete_many({})
        collection.insert_many(processed_data)
        if all(col in res_df.columns for col in continuous_columns):
            res_df[continuous_columns] = scaler.fit_transform(res_df[continuous_columns])
        
        print(res_df.head())
        return jsonify(res_df.to_dict(orient='records'))  # Trả về JSON cho danh sách các bản ghi
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)})

@app.route('/pre-processing-maxmin', methods=['POST'])
def pre_processing_maxmin():
    try:
        data = request.get_json()
        all_data = list(collection.find())
        df = pd.DataFrame(all_data)
        if '_id' in df.columns:
            df = df.drop(columns=['_id'])
        print("Cột trong DataFrame:", df.columns.tolist())
        
        continuous_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
        missing_columns = [col for col in continuous_columns if col not in df.columns]
        if missing_columns:
            return jsonify({"message": "Thiếu các cột: " + ", ".join(missing_columns)}), 400
        
        scaler = MinMaxScaler()
        scaler.fit(df[continuous_columns])

        input_df = pd.DataFrame(data) 

        if not all(col in input_df.columns for col in continuous_columns):
            return jsonify({"message": "Bản ghi đầu vào thiếu các cột cần thiết."}), 400
        
        input_df[continuous_columns] = scaler.transform(input_df[continuous_columns])
        processed_record = input_df.to_dict(orient='records')[0]
        
        return jsonify(processed_record)
    
    except Exception as e:
        return jsonify({"message": "Đã xảy ra lỗi", "error": str(e)}), 500

def do_pre_processing(data):
    if isinstance(data, dict):
        df = pd.DataFrame(data, index=[0])  
    else:
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

    df = df.drop_duplicates()
    df = df[sorted(df.columns)]
    print("Số lượng dữ liệu sau khi xử lý:", len(df))

    return df.to_dict(orient='records')

@app.route('/')
def index():
    return "This is Pre-Precessing Service"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8033, debug=True)


