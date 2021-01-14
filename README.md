# SharedBuilderServer
-A repository for the server and database programs that can be run on any system you wish to use as the server. (Python). This repository can be cloned and run in a virtual environment by downloading the pip requirements and setting up Mongo DB as explained in the readme.


# Settting Up a Mongo database

1) Before doing any of this you need to install and create a mongodb service running on this device

2)Download mongodb using "https://www.mongodb.com/try/download/community" and it's on the right

3) Follow the second option in this tutorial "https://treehouse.github.io/installation-guides/mac/mongo-mac.html"mkdir -p /data/db

4) Launching the mongo database:, then run sudo ~/mongodb/bin/mongod --dbpath=/Users/<username>/data/db
If this doesn't work it is likely that the database may already be running. To stop it, open mongo shell and use these commands
use admin.

db.shutdownServer()

6) Commands "https://docs.mongodb.com/manual/reference/mongo-shell/" for mongo shell

7) Get into mogno shell using ~/mongodb/bin/mongo in terminal or navigating to it directly and double clicking if this does not work.