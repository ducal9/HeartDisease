from flask import Flask, render_template
import pymongo
from config import Config


app = Flask(__name__)
client = pymongo.MongoClient(Config.MONGO_URL)
db = client.PRE
collection = db.Heart_Disease_Data


@app.route('/count-document')
def count_document():
    collection_count = len(db.list_collection_names())
    return str("Số lượng "+str(collection_count))


@app.route('/')
def index():
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8031)
