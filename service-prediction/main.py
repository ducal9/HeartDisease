from flask import Flask, jsonify
import pymongo
from config import Config


app = Flask(__name__)
client = pymongo.MongoClient(Config.MONGO_URL)
db = client.PRE
collection = db.Heart_Disease_Data


@app.route('/select-model')
def select_model():
    return "Model"

@app.route('/')
def index():
    return "This is Prediction Service"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8031)
