# Day 9
# Script that reads multiple CSV files
# merges them
# and outputs a combined dataset.

import os
import csv
import argparse

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

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "Path to input CSV file")
parser.add_argument("--output",  help = "Path to output CSV file")
args = parser.parse_args()

BASE_DIR = os.path.dirname(__file__)
folder_fallback = os.path.join(BASE_DIR, "test_files")
writer_fallback = os.path.join(BASE_DIR, "test_files/merged_sales.csv")

folder_path = args.input if args.input else folder_fallback
files = [
    f for f in os.listdir(folder_path)
    if f.endswith(".csv") and f.startswith("sales_")
]
#print(f"\n{files}")

files = sorted(files, key = lambda f: months[f.split("_")[1].split(".")[0]])
#print(f"\n{files}")

try:
    output_path = args.output if args.output else writer_fallback
    with open(output_path, "w", encoding = "utf-8", newline = "") as merged_sales:
        print(f"[INFO] Reading from: {folder_path}")
        print(f"[INFO] Writing to: {output_path}")
        csvwriter = csv.DictWriter(merged_sales, fieldnames = ["date", "product", "quantity", "price"], lineterminator = "\n")
        csvwriter.writeheader()
        for file in files:
            name, extension = os.path.splitext(file)
            if extension == ".csv":
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r", encoding = "utf-8") as monthly_sales:
                    csvreader = csv.DictReader(monthly_sales)
                    for row in csvreader:
                        csvwriter.writerow(row)

    print("[SUCCESS] CSV files merged successfully")

except FileNotFoundError:
    print("[ERROR] File doesn't exist")
except IOError:
    print("[ERROR] Failed to write data to file")
            



