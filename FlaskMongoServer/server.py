from flask import Flask, request
from flask_pymongo import PyMongo
from testData import ModelTestData

app = Flask(__name__)
#The SharedBuilder is a referece to the server and database
app.config["MONGO_URI"] = "mongodb://localhost:27017/SharedBuilder"
mongo = PyMongo(app)


# Sending data to the server

@app.route('/getUser/<username>', methods=['GET'])
def getUser(username):
    print(username)
    online_users = mongo.db.users.find_one({"username": username})
    print(online_users)
    online_users["_id"] = str(online_users["_id"])
    return online_users, 200

@app.route("/addUser", methods=['POST'])
def addUser():
    mydict = {
        "username": "Nathan",
        "handPosition": [5, 5],
        "brickConfig": []
    }
    online_users = mongo.db.users.insert_one(mydict)
    print(online_users)
    return str(online_users.inserted_id), 200

@app.route("/addCustomUser", methods=['POST'])
def addCustomUser():
    newUser = request.get_json()
    print(newUser)

    print(type(newUser))
    online_users = mongo.db.users.insert_one(newUser)
    
    print(online_users)
    return str(online_users.inserted_id), 200

@app.route('/postInterfaceData/<username>', methods=['POST'])
def postInterfaceData(username):
    interfaceDataRecieved = request.get_json()

    # A list containing dictionaries for each brick
    bricks = interfaceDataRecieved['bricks']

    document = {
        "_id": username,
        "brickConfig": bricks
    }

    #print(data)

    # Upload data to the databse
    #uploadID = mongo.db.InterfaceData.insert_one(document)
    

    myquery = { "_id": username }
    newvalues = { "$set": { "brickConfig": bricks } }


    mongo.db.collection.update_one(myquery, newvalues,upsert= True)

    print(mongo.db.collection.count())

    #print('{} posted interface data to server '.format(username))
    #print (interfaceData)

    return 'Added data succesfully', 200



# Fetching data from the server

@app.route('/unityTestGet', methods=['GET'])
def unityTestGet():
    data = {
        "level": 1,
        "timeElapsed": 1.5,
        "playerName": "Nathan"
    }
    return data, 200

@app.route('/getModel', methods=['GET'])
def getModel():
    return ModelTestData.modelB, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)