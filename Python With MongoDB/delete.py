import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["pythonwithmongodb"]

mycollection = mydb["programmers"]

print("MongoDB Database\n")
print("Delete Query on Programmers Colection :\n")


myquery = {"Name": "Advait"}

# mycollection.delete_one(myquery)





myquery = {"Name": {"$regex":"^A"}}
mycollection.delete_many({})


for x in mycollection.find():
    print(x)

