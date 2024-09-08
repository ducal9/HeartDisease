import pandas as pd
import pymongo
from config import Config
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

client = pymongo.MongoClient(Config.MONGO_URL)
db = client.PRE
collection = db.Heart_Disease_Data

data = list(collection.find())
df = pd.DataFrame(data)
df = df.drop(columns=['_id'])

# Xem trước vài dòng đầu của dữ liệu
print(df.head())

# Kiểm tra thông tin về dữ liệu
print(df.info())

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

print("Số lượng dữ liệu sau khi xử lý:", len(df))

# Chuẩn hóa các cột giá trị liên tục
scaler = MinMaxScaler()
continuous_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
df[continuous_columns] = scaler.fit_transform(df[continuous_columns])

print(df.head())


