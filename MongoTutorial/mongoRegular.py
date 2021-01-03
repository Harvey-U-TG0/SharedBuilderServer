import pymongo

# Before doing any of this you need to install and create a mongodb service running on this device
# Download mongodb using "https://www.mongodb.com/try/download/community" and it's on the right
# Follow the second option in this tutorial "https://treehouse.github.io/installation-guides/mac/mongo-mac.html"mkdir -p /data/db
# Store database date instead in ~/data/db, then run sudo ~/mongodb/bin/mongod --dbpath=/Users/harveyu/data/db
# Open up the mongodb shell in the terminal using "mongod"

# Commands "https://docs.mongodb.com/manual/reference/mongo-shell/" for mongo shell
# Get into mogno shell using ~/mongodb/bin/mongo in terminal


# This is not a database, it's a instance of mongodb
# An instance of mongodb, can hold many databases
print("1")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# This is connecting to a specific database called "mydatabase" in the mongodb instance/service
print("2")
mydb = myclient["mydatabase"]

# This is creating/getting a collection/table 
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x.inserted_id) 

print(mycol.find_one({"name": "John"}))

print(myclient.list_database_names())