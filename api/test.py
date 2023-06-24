import requests
import json

BASE = "http://127.0.0.1:5000/"

new_user = {
    "user": "Sinclair",
    "password": "helloworld",
    "email": "sinclair@email.com"
}

response = requests.get(BASE + "helloworld")
if response.status_code == 200:
    custom_header = response.headers.get("Custom-Header")
    print(custom_header)
else:
    print("Could not get entry: ", response.status_code)
input()

response = requests.put(BASE + "new/user", json=new_user)
if response.status_code == 201:
    custom_header = response.headers.get("Custom-Header")
    print(custom_header)
else:
    print("Could not create blog: ", response.status_code)
input()

email = new_user["email"]
response = requests.get(BASE + f"user/{email}")
if response.status_code == 302:
    custom_header = response.headers.get("Custom-Header")
    print(custom_header)
else:
    print("Could not create blog: ", response.status_code)
input()