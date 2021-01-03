# This python file is run to test various functionalities of the server

# Requests allows a python program to esseentially type in URL requests
import requests
import json

# The base URL to access the server
BASE = "http://127.0.0.1:5000/"

# User name
username = "Emily"

# Current brick configuration
brickConfig = [{"type": "1x1",
                "colour": "y",
                "position": [0,0]},
                
                {"type": "1x1",
                "colour": "y",
                "position": [0,0]}]

handPosition = [5,5]



testDict = {
            "username": username, 
            "brickConfig": brickConfig,
            "handPosition": handPosition
        }

# example = {"username": "max", "brickConfg": ["bod","far"], "handPosition": ["zar","mar"]}

# # Get Test
# response = requests.get(BASE + "brickLayout/2")
# print(response.json())
# input()

# # Add user test
# response = requests.put(BASE + "brickLayout/2", example, )
# print(response.json())



response = requests.post(BASE + "addCustomUser", json=testDict, headers={'Content-Type': 'application/json'})
print(response.text)

input()

response = requests.get(BASE + "getUser" + "/Emily")
print(response.text)