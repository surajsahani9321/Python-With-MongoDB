import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["pythonwithmongodb"]

mycollection = mydb["programmers"]

print("MongoDB Database\n")
print("Drop Query on Programmers Colection :\n")

if mycollection.drop():
    print("Programmer Collection Is Successfully Deleted")
else:
    print("Something went wrong")

