import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["pythonwithmongodb"]

mycollection=mydb["programmers"]

print("MongoDB Database\n")
print("All data in Programmers Colection :\n")
# x=mycollection.find_one()
#
# print(x)

# for y in mycollection.find():
#     print(y)

# for y in mycollection.find({},{"_id":0,"Nmae":1,"Language Known":1}):
#     print(y)

for x in mycollection.find({},{ "Language Known": 0 }):
  print(x)
