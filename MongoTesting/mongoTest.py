# Requests allows a python program to esseentially type in URL requests
import requests

# The base URL to access the server
BASE = "http://127.0.0.1:5000/"

# User name
username = "Harvey"

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
            "brickConfig": handPosition,
            "handPosition": handPosition
        }

example = {"username": "max", "brickConfg": ["bod","far"], "handPosition": ["zar","mar"]}

# Get Test
response = requests.get(BASE + "brickLayout/2")
print(response.json())
input()

# Add user test
response = requests.put(BASE + "brickLayout/2", example, )
print(response.json())

