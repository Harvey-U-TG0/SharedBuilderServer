import requests
import json

# The base URL to access the server
BASE = "http://127.0.0.1:5000/"

username = "Emily"
modelID = 'test'

response = requests.get(BASE + "getModel/"+modelID)
print(response.text)