from flask import Flask, jsonify
import pymongo
from config import Config
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
import json

app = Flask(__name__)
client = pymongo.MongoClient(Config.MONGO_URL)
db = client.PRE
collection = db.Heart_Disease_Data


@app.route('/select-model')
def select_model():
    return "Model"


@app.route('/model-lr')
def model_logistic_regression():
    data = pd.read_csv("E:\Fork\heartdiseaseproject\service-prediction\heart.csv")

    # In thông tin dữ liệu và kiểm tra giá trị null
    print(data.info())
    print(data.isnull().sum())

    y = data["target"]
    X = data.drop('target', axis=1)

    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

    # Chuẩn hóa dữ liệu
    scale = StandardScaler()
    X_train = scale.fit_transform(X_train)
    X_test = scale.transform(X_test)

    # Huấn luyện mô hình Logistic Regression
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Dự đoán trên tập kiểm tra
    y_predict = model.predict(X_test)

    # Tính các chỉ số đánh giá
    accuracy = accuracy_score(y_test, y_predict)
    precision = precision_score(y_test, y_predict)
    recall = recall_score(y_test, y_predict)

    # Tổng số mẫu
    total_samples = len(y_test)

    # Tổng số dự đoán chính xác
    correct_predictions = (y_test == y_predict).sum()

    # Tổng số dự đoán sai
    incorrect_predictions = (y_test != y_predict).sum()

    # Tạo DataFrame chỉ chứa số thứ tự, nhãn ban đầu và nhãn dự đoán
    results = pd.DataFrame({
        'Index': range(len(y_test)),
        'Actual': y_test.values,
        'Predicted': y_predict
    })

    # Chuyển đổi các giá trị thành kiểu dữ liệu Python cơ bản
    results['Actual'] = results['Actual'].astype(int)
    results['Predicted'] = results['Predicted'].astype(int)

    # Chuẩn bị kết quả để trả về
    output = {
        'metrics': {
            'Accuracy': float(accuracy),
            'Precision': float(precision),
            'Recall': float(recall),
            'Total Samples': total_samples,
            'Correct Predictions': int(correct_predictions),
            'Incorrect Predictions': int(incorrect_predictions)
        },
        'results': results.to_dict(orient="records")
    }

    # Trả về kết quả JSON với format đẹp
    return json.dumps(output, indent=4), 200, {'Content-Type': 'application/json'}


@app.route('/')
def index():
    return "This is Prediction Service"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8031, debug=True)
