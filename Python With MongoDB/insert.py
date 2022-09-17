import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["pythonwithmongodb"]

mycollection=mydb["programmers"]

# myrecord={"Name":"Suraj Sahani","Language Known":"Java,Python"}
# x=mycollection.insert_one(myrecord)
# print(x.inserted_id)

mylist=[

{"Name":"Advait","Language Known":"Java,Python"},
{"Name":"Adarsh","Language Known":"Java,Python"},
{"Name":"Hritik","Language Known":"Java,Python"},
{"Name":"Amit","Language Known":"Java,Python"},
{"Name":"Rakesh","Language Known":"Java,Python"},
{"Name":"Shubham","Language Known":"Java,Python"},
{"Name":"Amkit","Language Known":"Java,Python"},
{"Name":"Aniket","Language Known":"Java,Python"},
{"Name":"Vikas","Language Known":"Java,Python"},
{"Name":"Jagdish","Language Known":"Java,Python"},


]

# y=mycollection.insert_many(mylist)
# print(y.inserted_ids)
#
# mylist=[
#
# {"_id":1,"Name":"Advait","Language Known":"Java,Python"},
# {"_id":2,"Name":"Advait","Language Known":"Java,Python"},
# {"_id":3,"Name":"Advait","Language Known":"Java,Python"},
# {"_id":4,"Name":"Advait","Language Known":"Java,Python"},
# {"_id":5,"Name":"Advait","Language Known":"Java,Python"},
#
#
#
# ]

y=mycollection.insert_many(mylist)
print(y.inserted_ids)



