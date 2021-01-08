# Settting Up a Mongo database

1) Before doing any of this you need to install and create a mongodb service running on this device

2)Download mongodb using "https://www.mongodb.com/try/download/community" and it's on the right

3) Follow the second option in this tutorial "https://treehouse.github.io/installation-guides/mac/mongo-mac.html"mkdir -p /data/db

4) Launching the mongo database:, then run sudo ~/mongodb/bin/mongod --dbpath=/Users/harveyu/data/db
If this doesn't work it is likely that the database may already be running. To stop it, open mongo shell and use these commands
use admin
db.shutdownServer()


6) Commands "https://docs.mongodb.com/manual/reference/mongo-shell/" for mongo shell

7) Get into mogno shell using ~/mongodb/bin/mongo in terminal or navigating to it directly and double clicking if this does not work.

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
