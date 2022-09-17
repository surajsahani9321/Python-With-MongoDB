import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["pythonwithmongodb"]

print(myclient.list_database_names())

for db in myclient.list_database_names():
    print(db)

if "pythonwithmysql"  in myclient.list_database_names():

    print("Database exits")
else:
    print("Database not exists")

print(mydb.list_collection_names())

if "customers" in mydb.list_collection_names():
    print("Database exists")
else:
    print("Database doesn't exists")