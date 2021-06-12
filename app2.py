import pymongo
from pymongo import MongoClient

MONGO_URI = 'mongodb://127.0.0.1:27017'

client = MongoClient(MONGO_URI)

db = client['test']

collection = db['documentsFormatDates']

print(db)

print(collection)

dates = collection.aggregate(
    [{
    "$group" : 
        {"_id" : "$cdatetime", 
         "num" : {"$sum" : 1}
         }}, {'$sort':{'num':-1}}
    ])

#text_file = open("dates.txt", "w")
for i in dates:
    print(i)
#    text_file.write(str(i) + '\n')

#text_file.close()