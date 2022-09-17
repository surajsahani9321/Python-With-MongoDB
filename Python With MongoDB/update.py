import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["pythonwithmongodb"]

mycollection = mydb["programmers"]

print("MongoDB Database\n")
print("Update Query on Programmers Colection :\n")


myquery = {"Name": "Advait"}
newvalues = {"$set": {"Nmae":"Advait Bhai"}}
mycollection.update_one(myquery,newvalues)


x=mycollection.update_many(myquery,newvalues)
print(x.modified_count,"documents updated")



myquery = {"Name": {"$regex":"^A"}}
for x in mycollection.find(myquery):
    print(x)

