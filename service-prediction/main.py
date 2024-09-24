from flask import Flask,request, jsonify
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
import os


app = Flask(__name__)


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

    # Xóa thư mục 'training' nếu tồn tại và tạo lại
    current_dir = os.path.dirname(os.path.abspath(__file__))
    training_dir = os.path.join(current_dir, 'training')

    if os.path.exists(training_dir):
        import shutil
        shutil.rmtree(training_dir)  # Xóa thư mục
    os.makedirs(training_dir)  # Tạo thư mục mới

    # Lưu mô hình vào file
    model_file = f"{training_dir}/training.joblib"
    joblib.dump(best_model, model_file)

    # Lưu dữ liệu huấn luyện
    training_data_file = f"{training_dir}/training_data.pkl"
    joblib.dump((X_train, y_train), training_data_file)

    model_info = {
        'model_name': best_model_name,
        'model_file': model_file,
        'accuracy': best_accuracy,
        'num_train': int(num_train),
        'num_test': int(num_test),
        'total_data': int(total_data)
    }

    print(f"Best model: {best_model_name} saved as {model_file}")

    # Trả kết quả dưới dạng JSON
    return jsonify(results)



@app.route('/predict', methods=['POST'])
def predict():
    # Nhận dữ liệu từ yêu cầu POST
    input_data = request.get_json()

    # Lấy thư mục chứa file Python hiện tại
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Đường dẫn đến mô hình đã lưu
    model_file = os.path.join(current_dir, 'training', 'training.joblib')  # Thay đổi phù hợp nếu cần
    model = joblib.load(model_file)

    # Đường dẫn đến dữ liệu huấn luyện đã lưu
    training_data_file = os.path.join(current_dir, 'training', 'training_data.pkl')
    X_train, y_train = joblib.load(training_data_file)

    # Chuyển đổi dữ liệu đầu vào thành DataFrame
    input_df = pd.DataFrame([input_data])  # Đảm bảo đầu vào là một DataFrame

    # Tiền xử lý dữ liệu tương tự như khi huấn luyện
    imputer = SimpleImputer(strategy='mean')
    input_df = imputer.fit_transform(input_df)

    scaler = StandardScaler()
    input_df = scaler.fit_transform(input_df)

    # Dự đoán
    predictions = model.predict(input_df)
    return jsonify({'prediction': predictions[0].item()})  # Nếu predictions[0] là một int64


@app.route('/')
def index():
    return "This is Prediction Service"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8031, debug=True)
