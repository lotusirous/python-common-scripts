from pymongo import MongoClient
def mongodb():
    client = MongoClient("mongodb://mongodb0.example.net:27017")
    db = client["test"] # test is a collection

    # insert
    a_dict = dict()
    result = db["restaurants"].insert_one(a_dict)

    # query
    cursor = db["restaurants"].find()
    for doc in cursor:
        print(doc)