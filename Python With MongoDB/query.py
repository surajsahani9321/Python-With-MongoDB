import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["pythonwithmongodb"]

mycollection = mydb["programmers"]

print("MongoDB Database\n")
print("Filters Query on Programmers Colection :\n")


# myquery = {"Name": {"$gt":"C"}}
# for x in mycollection.find(myquery):
#     print(x)


myquery = {"Name": {"$regex":"^A"}}
for x in mycollection.find(myquery):
    print(x)

