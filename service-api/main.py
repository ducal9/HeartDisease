from flask import Flask, jsonify, request
import pandas as pd
from config import Config
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#API get email
@app.route('/api-get-file-from-email')
def api_get_file_from_email():
    try:
        url = Config.SERVICE_EMAIL_DOWNLOAD+"/get-file"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({"status": "success", "data": data}), 200
        else:
            return jsonify({"status": "error", "message": "Failed to fetch file from email"}), response.status_code
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api-test', methods=['POST'])
def api_test(): 
    data = request.get_json()
    print(data)
    return jsonify({"Success": "Success-200", "data": data})
            
#API Predict
@app.route('/api-predict', methods=['POST'])
def api_predict(): 
    data = request.get_json()
    pre_processing_url = Config.SERVICE_PRE_PROCESSING + "/pre-processing"
    try:
        pre_processing_response = requests.post(pre_processing_url, json=data)
        if pre_processing_response.status_code == 200:
            processed_data = pre_processing_response.json()
            print(processed_data)
            predict_url = Config.SERVICE_PREDICTION+"/predict"

            predict_response = requests.post(predict_url, json=processed_data)

            if predict_response.status_code == 200:
                return jsonify({"Success": "Success", "data": predict_response.json()}), 200
            else:
                return jsonify({"error": "Failed to call predict service", "status_code": predict_response.status_code, "response": predict_response.text}), predict_response.status_code
        else:
            return jsonify({"error": "Failed to call pre-processing service", "status_code": pre_processing_response.status_code, "response": pre_processing_response.text}), pre_processing_response.status_code
    except Exception as e:
        return jsonify({"error": "Đã xảy ra lỗi", "message": str(e)}), 500

#API Predict V2
@app.route('/api-predict-v2', methods=['POST'])
def api_predict_v2(): 
    data = request.get_json()
    pre_processing_url = Config.SERVICE_PRE_PROCESSING + "/pre-processing"
    pre_processing_maxmin_url = Config.SERVICE_PRE_PROCESSING + "/pre-processing-maxmin"
    try:
        pre_processing_response = requests.post(pre_processing_url, json=data)
        pre_processing_maxmin_response = requests.post(pre_processing_maxmin_url, json=data)
        if pre_processing_response.status_code == 200 and pre_processing_maxmin_response.status_code == 200:
            processed_data = pre_processing_response.json()
            processed_data_maxmin = pre_processing_maxmin_response.json()
            print(processed_data)
            print(processed_data_maxmin)
            
            predict_url = Config.SERVICE_PREDICTION+"/predict"
            predict_maxmin_url = Config.SERVICE_PREDICTION+"/predict-maxmin"
            
            predict_response = requests.post(predict_url, json=processed_data)
            predict_maxmin_response = requests.post(predict_maxmin_url, json=processed_data)
            if predict_maxmin_response.status_code == 200 and predict_response.status_code == 200:
                predict_maxmin_predictions = predict_maxmin_response.json().get("predictions", [])
                predict_response_prediction = predict_response.json().get("prediction")

                all_predictions = predict_maxmin_predictions + [str(predict_response_prediction)]
                vote_counts = {value: all_predictions.count(value) for value in set(all_predictions)}

                majority_vote = max(vote_counts, key=vote_counts.get)
        
                return jsonify({
                    "Success": "Success",
                    "result": majority_vote,
                    "predict_maxmin_response_data": predict_maxmin_response.json(),
                    "predict_response_data": predict_response.json()
                }), 200
            else:
                error_message = {
                    "error": "Failed to call predict service",
                    "status_code_predict": predict_response.status_code,
                    "response_predict": predict_response.text,
                    "status_code_predict_maxmin": predict_maxmin_response.status_code,
                    "response_predict_maxmin": predict_maxmin_response.text
                }
                return jsonify(error_message), 400  # Trả về mã lỗi 400 khi có sự cố
        else:
            return jsonify({
                "error": "Failed to call pre-processing service",
                "status_code": {
                    "pre_processing": pre_processing_response.status_code,
                    "pre_processing_maxmin": pre_processing_maxmin_response.status_code
                },
                "response": {
                    "pre_processing": pre_processing_response.text,
                    "pre_processing_maxmin": pre_processing_maxmin_response.text
                }
            }), max(pre_processing_response.status_code, pre_processing_maxmin_response.status_code)
    except Exception as e:
        return jsonify({"error": "Đã xảy ra lỗi", "message": str(e)}), 500

#API Training-data
@app.route('/api-training-data', methods=['POST'])
def api_training_data():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if not file.filename or not file.filename.lower().endswith('.csv'):
        return jsonify({"error": "File is not CSV or no file selected"}), 400

    files = {'file': (file.filename, file.stream, 'text/csv')}
    
    try:
        df = pd.read_csv(file)
        data_json = df.to_dict(orient='records')
        pre_processing_url = Config.SERVICE_PRE_PROCESSING + "/pre-processing"
        pre_processing_url_v2 = Config.SERVICE_PRE_PROCESSING + "/pre-processing-v2"
        
        pre_processing_response = requests.post(pre_processing_url, json=data_json)
        pre_processing_response_v2 = requests.post(pre_processing_url_v2, json=data_json)
        if pre_processing_response.status_code != 200 and pre_processing_response_v2.status_code != 200:
            error_responses = {
                "pre-processing": pre_processing_response.json() if pre_processing_response.status_code != 200 else "Success",
                "pre-processing-v2": pre_processing_response_v2.json() if pre_processing_response_v2.status_code != 200 else "Success"
            }
            return jsonify({"error": "Pre-processing failed", "responses": error_responses}), 400
        
        training_data = pre_processing_response.json()
        training_data_v2 = pre_processing_response_v2.json()
        training_url = Config.SERVICE_PREDICTION+"/training"
        training_url_v2 = Config.SERVICE_PREDICTION+"/training-v2"
        
        training_response = requests.post(training_url, json=training_data)
        training_response_v2 = requests.post(training_url_v2, json=training_data_v2)
        
        if training_response.status_code != 200 or training_response_v2.status_code != 200:
            error_responses = {
                "training": training_response.json() if training_response.status_code != 200 else "Success",
                "training-v2": training_response_v2.json() if training_response_v2.status_code != 200 else "Success"
            }
            return jsonify({"error": "Training failed", "responses": error_responses}), 400

        # Success response
        responses = {
            "training": training_response.json(),
            "training-v2": training_response_v2.json()
        }
        return jsonify({"message": "File processed and trained successfully", "responses": responses}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/')
def index():
    return "This is API Service"


if __name__ == '__main__':
     # Chạy luồng lấy dữ liệu từ React
    #from threading import Thread
    #data_thread = Thread(target=get_and_print_data)
    #data_thread.start()
    app.run(host='127.0.0.1', port=8032, debug=True)