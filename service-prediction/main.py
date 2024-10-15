import pandas as pd
from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
import os
import shutil


app = Flask(__name__)

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
    print(f"Độ tin cậy của mô hình: {accuracy:.2f}")
    joblib.dump(model, MODEL_FILE)
    return accuracy

def load_model():
    if os.path.exists(MODEL_FILE):
        return joblib.load(MODEL_FILE)
    else:
        raise Exception("Model file not found!")

#Training
@app.route('/training', methods=['POST'])
def training():
    data = request.get_json()
    df = pd.DataFrame(data)
    create_training_folder()
    accuracy = train_model(df)
    print(df.head())
    return jsonify({"message": "Model trained successfully!", "accuracy": f"{accuracy:.2f}"})

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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8031, debug=True)
