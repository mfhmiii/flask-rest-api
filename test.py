import requests

BASE = "http://127.0.0.1:5000/"

response1 = requests.get(BASE + "helloworld")
response2 = requests.post(BASE + "helloworld")

response3 = requests.get(BASE + "params/fahmi/1")
response4 = requests.get(BASE + "var/not-fahmi")

print(response1.json())
print(response2.json())
print(response3.json())
print(response4.json())