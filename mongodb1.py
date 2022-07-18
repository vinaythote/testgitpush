import pymongo
client = pymongo.MongoClient("mongodb+srv://vinaythote:qweasd123@cluster0.sjgiw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Vinay",
    "lastname": "Thote",
    "email": "vinaythote7@gmail.com"
}

db1 = client['mongodb1']
coll = db1['test']
coll.insert_one(d )