import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["pythonwithmongodb"]

mycollection=mydb["programmers"]

print("MongoDB Database\n")
print("All sorted data in Programmers Colection :\n")

# for x in mycollection.find().sort("Name",-1):
#     print(x)

myquery={"Name":"Advait"}
for x in mycollection.find(myquery):
    print(x)

