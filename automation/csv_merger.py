# Day 9
# Script that reads multiple CSV files
# merges them
# and outputs a combined dataset.

import os
import csv

months = {
    "january":1,
    "february":2,
    "march":3,
    "april":4,
    "may":5,
    "june":6,
    "july":7,
    "august":8,
    "september":9,
    "october":10,
    "november":11,
    "december":12
}

files = [
    f for f in os.listdir("test_files_merger")
    if f.startswith("sales_")
]
#print(f"\n{files}")

files = sorted(files, key = lambda f: months[f.split("_")[1].split(".")[0]])
#print(f"\n{files}")

try:
    with open("test_files_merger/merged_sales.csv", "w") as merged_sales:
        csvwriter = csv.DictWriter(merged_sales, fieldnames = ["date", "product", "quantity", "price"], lineterminator = "\n")
        csvwriter.writeheader()
        for file in files:
            name, extension = os.path.splitext(file)
            if extension == ".csv":
                with open(f"test_files_merger/{file}", "r") as monthly_sales:
                    csvreader = csv.DictReader(monthly_sales)
                    for row in csvreader:
                        csvwriter.writerow(row)

except FileNotFoundError:
    print("File doesn't exist")
except IOError:
    print("Failed to write data to file")
            



