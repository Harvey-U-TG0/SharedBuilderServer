from flask import Flask, request
from flask_pymongo import PyMongo
from testData import ModelTestData

app = Flask(__name__)
#The SharedBuilder is a referece to the server and database
app.config["MONGO_URI"] = "mongodb://localhost:27017/SharedBuilder"
mongo = PyMongo(app)


# Sending data to the server

@app.route('/postInterfaceData/<username>', methods=['POST'])
def postInterfaceData(username):
    interfaceDataRecieved = request.get_json()

    # A list containing dictionaries for each brick
    bricks = interfaceDataRecieved['bricks']

    # Update Interface Data collection, creates new document if needed
    myquery = { "_id": username }
    newvalues = { "$set": { "brickConfig": bricks} }

    mongo.db.InterfaceData.update_one(myquery, newvalues,upsert= True)

    print(mongo.db.InterfaceData.count())
    print(mongo.db.InterfaceData.find()[0])

    #print('{} posted interface data to server '.format(username))
    #print (interfaceData)

    return 'Added data succesfully', 200

# Given a username and new model ID (or False) will update the users editing status
@app.route('/updateUserEditing/<username>/<modelID>', methods=['POST'])
def updateUserEditing(username,modelID):
    print ('user id {} requests to change their editing model ID to {}'. format(username,modelID))

    myquery = { "_id": username }

    if (modelID == 'False'):
        newvalues = { "$set": { "userEditing": False} }
    else:
        newvalues = { "$set": { "userEditing": modelID} }

    mongo.db.InterfaceData.update_one(myquery, newvalues,upsert= True)

    newModelIDValue = mongo.db.InterfaceData.find_one(myquery)["userEditing"]
    print ("user editing value set to " + newModelIDValue)


    return 'Changed user editing data succesfully', 200





# Fetching data from the server

@app.route('/getModel', methods=['GET'])
def getModel():
    return ModelTestData.modelB, 200






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)