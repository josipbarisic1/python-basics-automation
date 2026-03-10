# Day 5
# Script that calls a public API
# fetches JSON data
# and saves the response to a file.

import requests
import json

url = "https://randomuser.me/api/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f'Failed to return data, status code: {response.status_code}')
    exit()

try:
    with open("data.json", "w") as random_user:
        json.dump(data, random_user, indent = 4)
except IOError:
    print("Failed to write data to file")

user = data["results"][0]
fname = user["name"]["first"]
lname = user["name"]["last"]
print(f"User {fname} {lname} dumped...")