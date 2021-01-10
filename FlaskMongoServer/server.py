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

    # Update the database with with the new brick config
    mongo.db.InterfaceData.update_one(myquery, newvalues,upsert= True)


    usersDocument = mongo.db.InterfaceData.find_one(myquery)

    # Check if user is updating
    userEditing = usersDocument["userEditing"]
    if (userEditing != False):
        print ("user {} is updating the model {}" .format(username,userEditing))
        # Find if a model document with this ID exists
        modelDoc = mongo.db.modelData.find_one({ "_id": userEditing })
        
        # If not make one and set this users contrubtion in the users contributions
        if (modelDoc == None):
            newModel = {
                        '_id': userEditing,
                        'userContributions': [usersDocument],
                        'cost': 10
            }
            newDoc = mongo.db.modelData.insert_one(newModel)
        else:
            userContribs = modelDoc['userContributions']
            
            
            updated = False 
            for contrib in userContribs:
                if (contrib['_id'] == username):
                    contrib['brickConfig'] = bricks
                    #print('updated brick configuration to ' + str(contrib['brickConfig']))
                    updated = True
                    break
            
            if (updated == False):
                userContribs.append(usersDocument)


            mongo.db.modelData.save(modelDoc)

                    
        
        # If so update that model accordingly
        myquery = { "_id": userEditing }
        newvalues = { "$set": { 'userContributions': bricks} }

        # Update the database with with the new brick config
        #mongo.db.modelData.update_one(myquery, newvalues, upsert= True)




    #print(mongo.db.InterfaceData.count())
    #print(mongo.db.InterfaceData.find()[0])
    #print(mongo.db.modelData.find_one({"_id": userEditing}))

    #print('{} posted interface data to server '.format(username))
    #print (interfaceData)

    return 'Added data succesfully', 200



# Given a username and new model ID (or False) will update the users editing status
@app.route('/updateUserEditing/<username>/<modelID>', methods=['GET'])
def updateUserEditing(username,modelID):
    print ('user id {} requests to change their editing model ID to {}'. format(username,modelID))

    myquery = { "_id": username }

    if (modelID == 'False'):
        newvalues = { "$set": { "userEditing": False} }
    else:
        newvalues = { "$set": { "userEditing": modelID} }

    mongo.db.InterfaceData.update_one(myquery, newvalues,upsert= True)

    newModelIDValue = mongo.db.InterfaceData.find_one(myquery)["userEditing"]
    print ("user editing value set to " + str(newModelIDValue))


    return 'Changed user editing data succesfully', 200



# Fetching data from the server
@app.route('/getModel/<modelID>', methods=['GET'])
def getModel(modelID):
    # Access server database and get the model with that id
    # If the model doesnt exist then create one


    modelDoc = mongo.db.modelData.find_one({ "_id": modelID })
        
    
    # If not make one with an empty user contribution
    if (modelDoc == None):
        newModel = {
                    '_id': modelID,
                    'userContributions': [],
                    'cost': 10
        }
        modelDocToSend = mongo.db.modelData.insert_one(newModel)
    else:
        modelDocToSend = modelDoc

    return modelDocToSend, 200






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)





#Data format reference

# Document in Interface Data
#{
#   '_id': <username>
#    'brickConfig': List of brick dictionaries eg [{'shapeID': 11, 'position': [0, 0], 'colourID': 9.0}, ....]
#   'userEditing': either a model ID as a string or False
#}

# Model Data Docuemnt example
 #{
#   '_id': <model id as a string>
#   'userContributions': List of Interface Data Docuemnts as shown above
#   'cost': string of the cost eg '10'
#}




