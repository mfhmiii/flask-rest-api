import requests

BASE = "http://127.0.0.1:5000/"

response1 = requests.get(BASE + "helloworld")
response2 = requests.post(BASE + "helloworld")

response3 = requests.get(BASE + "params/fahmi/1")
response4 = requests.get(BASE + "var/not-fahmi")

# response5 = requests.put(BASE + "video/1", {"likes":10, "name":"intro", "views":1000})
input()
response6 = requests.get(BASE + "video/1")

data = [{"likes":214, "name":"intro", "views":3234},
        {"likes":554, "name":"main", "views":4356},
        {"likes":32, "name":"end", "views":34}]

for i in range(len(data)):
    response5 = requests.put(BASE + "video/" + str(i), data[i])
    print(response5.json())

input()
response7 = requests.delete(BASE + "video/0")

print(response1.json())
print(response2.json())
print(response3.json())
print(response4.json())
print(response6.json())
print(response7)