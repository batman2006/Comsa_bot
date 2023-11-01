from pymongo import MongoClient
from urllib.parse import quote_plus
from connections import db_password

encoded_password = quote_plus(db_password)

cluster = MongoClient(
    f"mongodb+srv://nazarworker17:{encoded_password}@cluster0.momxsd3.mongodb.net/?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test"]

post = {"_id":0 ,"User":"dwwimm","Login":"log1","Password":"pass1"}

collection.insert_one(post)

documents = collection.find()


for document in documents:
    print(document)