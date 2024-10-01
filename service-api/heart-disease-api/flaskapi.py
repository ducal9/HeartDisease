from flask import Flask, request, jsonify

app = Flask(__name__)

# Lưu trữ dữ liệu mới nhất
latest_data = None

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    global latest_data
    latest_data = data
    return jsonify({'message': 'Data received successfully', 'data': data, 'prediction': 'Sample prediction based on data'})

@app.route('/api/latest', methods=['GET'])
def get_latest_data():
    if latest_data:
        return jsonify(latest_data)
    else:
        return jsonify({'message': 'No data available'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)