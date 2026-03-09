# Day 4
# Script that reads a CSV file
# filters users younger than 18
# and saves adult users to a new CSV file.

import csv

try:
    with open("users.csv", "r") as users, open("adults.csv", "w") as adults:
        csvreader = csv.DictReader(users)
        csvwriter = csv.DictWriter(adults, fieldnames = csvreader.fieldnames, lineterminator = "\n")

        csvwriter.writeheader()
        for row in csvreader:
            if int(row["age"]) >= 18:
                csvwriter.writerow(row)

except FileNotFoundError:
    print("File doesn't exist")