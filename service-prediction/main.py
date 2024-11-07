import pandas as pd
from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import joblib
import os
import shutil


app = Flask(__name__)

#V1
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRAINING_FOLDER = os.path.join(BASE_DIR, 'training')
MODEL_FILE = os.path.join(TRAINING_FOLDER, 'decision_tree_model.pkl')

def create_training_folder():
    if os.path.exists(TRAINING_FOLDER):
        shutil.rmtree(TRAINING_FOLDER)
    os.makedirs(TRAINING_FOLDER)

def train_model(df):
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    joblib.dump(model, MODEL_FILE)
    print(f"Độ tin cậy của mô hình: {accuracy:.2f}")
    return accuracy

#Training
@app.route('/training', methods=['POST'])
def training():
    data = request.get_json()
    df = pd.DataFrame(data)
    create_training_folder()
    accuracy = train_model(df)
    print(df.head())
    return jsonify({"message": "Model trained successfully!", "accuracy": f"{accuracy:.2f}"})

def load_model():
    if os.path.exists(MODEL_FILE):
        return joblib.load(MODEL_FILE)
    else:
        raise Exception("Model file not found!")
    
#Predict
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])
    #df = pd.DataFrame(data) 
    model = load_model()
    try:
        prediction = model.predict(df)
        return jsonify({'prediction': int(prediction[0])})
        #predictions = model.predict(df)
        #return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


#V2
TRAINING_FOLDER_V2 = os.path.join(BASE_DIR, 'training_v2')
MODEL_FILES = {
    'knn': os.path.join(TRAINING_FOLDER_V2, 'knn_model.pkl'),
    'logistic_regression': os.path.join(TRAINING_FOLDER_V2, 'logistic_regression_model.pkl')
}

def create_training_folder_v2():
    if os.path.exists(TRAINING_FOLDER_V2):
        shutil.rmtree(TRAINING_FOLDER_V2)
    os.makedirs(TRAINING_FOLDER_V2)

def train_models(df):
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # K-Nearest Neighbors
    knn_model = KNeighborsClassifier()
    knn_model.fit(X_train, y_train)
    knn_accuracy = knn_model.score(X_test, y_test)
    joblib.dump(knn_model, MODEL_FILES['knn'])

    # Logistic Regression
    lr_model = LogisticRegression(max_iter=1000)
    lr_model.fit(X_train, y_train)
    lr_accuracy = lr_model.score(X_test, y_test)
    joblib.dump(lr_model, MODEL_FILES['logistic_regression'])

    # Kết quả độ chính xác của ba mô hình
    return {
        "knn_accuracy": knn_accuracy,
        "logistic_regression_accuracy": lr_accuracy
    }

# Training v2
@app.route('/training-v2', methods=['POST'])
def training_v2():
    data = request.get_json()
    df = pd.DataFrame(data)
    create_training_folder_v2()
    accuracies = train_models(df)
    return jsonify({
        "message": "All models trained successfully!",
        "accuracies": {
            "K-Nearest Neighbors": f"{accuracies['knn_accuracy']:.2f}",
            "Logistic Regression": f"{accuracies['logistic_regression_accuracy']:.2f}"
        }
    })

#def load_model():
#    if os.path.exists(MODEL_FILE):
#        return joblib.load(MODEL_FILE)
#    else:
#        raise Exception("Model file not found!")
#TRAINING_FOLDER_V2 = os.path.join(BASE_DIR, 'training_v2')
#MODEL_FILES = {
#    'knn': os.path.join(TRAINING_FOLDER_V2, 'knn_model.pkl'),
#    'logistic_regression': os.path.join(TRAINING_FOLDER_V2, 'logistic_regression_model.pkl')
#}
def load_models(model_name):
    if model_name in MODEL_FILES:
        model_path = MODEL_FILES[model_name]
        if os.path.exists(model_path):
            return joblib.load(model_path)
        else:
            raise Exception(f"Model file {model_name} not found!")
    else:
        raise Exception(f"Model {model_name} is not defined!")
    
#Predict
@app.route('/predict-maxmin', methods=['POST'])
def predict_maxmin():
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])
    result = []
    for model_name in MODEL_FILES:
        try:
            model = load_models(model_name)
            prediction = model.predict(df)
            result.append(str(prediction[0])) 
        except Exception as e:
            return jsonify({'error': f"Error with model {model_name}: {str(e)}"}), 400
    return jsonify({'predictions': result})
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8031, debug=True)
