from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
#Flask Pymongo includes everything needed for mongo
from flask_pymongo import PyMongo


# Setup flask app
app = Flask(__name__)
api = Api(app)
#For now we have made a server called mydatabase which will will access
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app) #Initialise the app

# Data Parser
brick_put_args = reqparse.RequestParser()
brick_put_args.add_argument("username",type=str, help="Username associated with the build unit",required=True)
brick_put_args.add_argument("brickConfig",type=list, help="A list containing information about the current brick placement",required=True)
brick_put_args.add_argument("handPosition",type=list, help="Current coordinates of hand above the build plate",required=True)

resource_fields = {
    'username': fields.String,
    'brickConfig': fields.List,
    'handPosition': fields.List,
}

class BricksLayout(Resource):
    def get(self, user_id):
        online_users = mongo.db.customers.find_one({"name": "Harvey"})
        print(online_users)
        online_users["_id"] = str(online_users["_id"])
        return online_users, 200

    #@marshal_with(resource_fields)
    def put(self, user_id):
        args = brick_put_args.parse_args()
        print(args["brickConfig"])
        
        
        
        mydict = {
            "username": "Nathan", 
            "lastUpdated": "London", 
            "brick": [
                {
                    "brickType": "2x2",
                    "colour": "red",
                    "position": [12, 10, 0]
                },
                {
                    "brickType": "2x4",
                    "colour": "blue",
                    "position": [8, 4, 0]
                }
            ]
        }
        online_users = mongo.db.customers.insert_one(mydict)
        print(online_users)
        return str(online_users.inserted_id), 200

# Will make different classes for different actions

# The path is written in the quotations
api.add_resource(BricksLayout, "/brickLayout/<int:user_id>")

# Run the server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)