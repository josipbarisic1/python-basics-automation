# CSV MERGER
# Script that reads multiple CSV files
# merges them
# and outputs a combined dataset.

import os
import csv
import argparse
import sys

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

parser = argparse.ArgumentParser(
    description="Merges multiple monthly CSV files into one chronologically sorted dataset"
)
parser.add_argument(
    "--input",
    help="Path to folder containing CSV files (default: test_files/)",
    metavar="FOLDER"
)
parser.add_argument(
    "--output",
    help="Path to output merged CSV file (default: test_files/merged_sales.csv)",
    metavar="FILE"
)
args = parser.parse_args()

if args.input and not os.path.isdir(args.input):
    print(f"[ERROR] Input folder not found: {args.input}")
    sys.exit(1)

BASE_DIR = os.path.dirname(__file__)
folder_fallback = os.path.join(BASE_DIR, "test_files")
writer_fallback = os.path.join(BASE_DIR, "test_files/merged_sales.csv")

folder_path = args.input if args.input else folder_fallback
files = [
    f for f in os.listdir(folder_path)
    if f.endswith(".csv") and f.startswith("sales_")
]

files = sorted(files, key = lambda f: months[f.split("_")[1].split(".")[0]])

total_rows = 0
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
                        total_rows += 1

    print(f"\n[SUCCESS] CSV files merged successfully")
    print(f"  Files merged: {len(files)}")
    print(f"  Total rows: {total_rows}")
    print(f"  Output: {output_path}")

except FileNotFoundError:
    print("[ERROR] File doesn't exist")
except IOError:
    print("[ERROR] Failed to write data to file")
            



