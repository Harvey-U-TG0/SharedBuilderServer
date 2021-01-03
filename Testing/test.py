import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "helloworld/bill/1")
#print(response.json())

# Test Data
data = [{"likes": 10, "name": "Tim", "views": 100000},
        {"likes": 5, "name": "Harry", "views": 100},
        {"likes": 1, "name": "Edward", "views": 10},
        {"likes": 5, "name": "William", "views": 30}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())

# Patch an existing result
response = requests.patch(BASE + "video/2", {"views":99})
print(response.json())