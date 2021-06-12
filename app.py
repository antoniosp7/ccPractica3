import pymongo
from pymongo import MongoClient

MONGO_URI = 'mongodb://127.0.0.1:27017'

client = MongoClient(MONGO_URI)

db = client['test']

collection = db['documents']

print(db)

print(collection)

crimes = collection.aggregate(
    [{
    "$group" : 
        {"_id" : "$crimedescr", 
         "num" : {"$sum" : 1}
         }}, {'$sort':{'num':-1}}
    ])

#text_file = open("crimes.txt", "w")
for i in crimes:
    print(i)
#    text_file.write(str(i) + '\n')

#text_file.close()





