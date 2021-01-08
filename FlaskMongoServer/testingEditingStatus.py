import requests
import json

# The base URL to access the server
BASE = "http://127.0.0.1:5000/"

username = "Emily"


response = requests.post(BASE + "updateUserEditing/"+username+'/'+'test')
print(response.text)