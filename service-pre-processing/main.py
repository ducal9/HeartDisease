import pandas as pd
import pymongo
from config import Config


client = pymongo.MongoClient(Config.MONGO_URL)
db = client.PRE
collection = db.Heart_Disease_Data

data = list(collection.find())
df = pd.DataFrame(data)

print("Số lượng dữ liệu trước khi xử lý:", len(df))

if '_id' in df.columns:
    df.drop(columns=['_id'], inplace=True)

df.replace('', pd.NA, inplace=True)  
df.dropna(inplace=True) 

print("Số lượng dữ liệu sau khi xử lý:", len(df))

print(df.head())

#Dữ liệu sau khi xử lý sẽ lưu vào client.HDD

