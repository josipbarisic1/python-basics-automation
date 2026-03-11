# Day 6
# Mini automation project
# combine CSV processing with API calls
# and save processed results.

import csv
import requests
import json

def find_user_by_name():
    url = "https://randomuser.me/api/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        user = data["results"][0]

        gender = user["gender"]
        email = user["email"]
        city = user["location"]["city"]

        return{
            "gender" : gender,
            "email" : email,
            "city" : city
        }

    else:
        print(f'Failed to return data, status code: {response.status_code}')
        exit()


try:
    with open("users.csv", "r") as names, open("user_details.csv", "w") as user_details:
        csvreader = csv.DictReader(names)
        csvwriter = csv.DictWriter(user_details, fieldnames = csvreader.fieldnames + ["gender", "email", "city"], lineterminator = "\n")

        csvwriter.writeheader()
        for row in csvreader:
            user_info = find_user_by_name()
            row.update(user_info)
            csvwriter.writerow(row)
                                   
except FileNotFoundError:
    print("File doesn't exist")
except IOError:
    print("Failed to write data to file")



