from flask import Flask, jsonify
import pymongo
from config import Config
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, ConfusionMatrixDisplay, classification_report
from sklearn.preprocessing import StandardScaler
import json
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
import joblib

app = Flask(__name__)
client = pymongo.MongoClient(Config.MONGO_URL)
db = client.PRE
collection_hdd = db.Heart_Disease_Data
collection_training = db.Training


@app.route('/select-model')

def select_model():
    df = pd.read_csv("E:/Fork/heartdiseaseproject/service-prediction/heart_new.csv")
    
    y = df["target"]
    X = df.drop('target', axis=1)

    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    imputer = SimpleImputer(strategy='mean')
    X_train = imputer.fit_transform(X_train)
    X_test = imputer.transform(X_test)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        'Logistic Regression': LogisticRegression(),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC(),
        'KNN': KNeighborsClassifier(),
        'Gradient Boosting': GradientBoostingClassifier(),
        'XGBoost': XGBClassifier(),
        'AdaBoost': AdaBoostClassifier(), 
        'Naive Bayes': GaussianNB(),       
        'MLP Neural Network': MLPClassifier() 
    }

    results = {}
    total_data = len(df)
    num_train = len(X_train)
    num_test = len(X_test)

    best_model_name = None
    best_accuracy = 0

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)

        correct_predictions = (y_pred == y_test).sum()
        incorrect_predictions = (y_test.size - correct_predictions)

        results[name] = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'num_train': int(num_train),
            'num_test': int(num_test),
            'correct_predictions': int(correct_predictions),
            'incorrect_predictions': int(incorrect_predictions),
            'total_data': int(total_data)
        }

        # Lưu mô hình tốt nhất
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model_name = name
            best_model = model

    # Lưu mô hình vào file
    model_file = f"{best_model_name.replace(' ', '_')}.joblib"
    joblib.dump(best_model, model_file)


    model_info = {
        'model_name': best_model_name,
        'model_file': model_file,
        'accuracy': best_accuracy,
        'num_train': int(num_train),
        'num_test': int(num_test),
        'total_data': int(total_data)
    }
    
    #collection_training.insert_one(model_info)

    print(f"Best model: {best_model_name} saved as {model_file}")

    # Xuất kết quả ra file JSON
    report_file = "model_report.json"
    with open(report_file, 'w') as f:
        json.dump(results, f, indent=4)

    # Trả kết quả dưới dạng JSON
    return jsonify(results)


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
