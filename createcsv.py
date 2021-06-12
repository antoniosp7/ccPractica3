import pymongo
from pymongo import MongoClient
import pandas as pd

MONGO_URI = 'mongodb://127.0.0.1:27017'

client = MongoClient(MONGO_URI)

db = client['test']

collection = db['documents']

results = collection.find()

df = pd.DataFrame((results))

df['cdatetime'] = df['cdatetime'].astype(str).str[7:-3]

df.to_csv('SacramentocrimeJanuary2006-2.csv', index=False)