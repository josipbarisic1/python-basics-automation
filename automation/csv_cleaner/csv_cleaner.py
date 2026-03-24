# Day 10
# Script that cleans messy CSV data
# removes duplicates
# and standardizes formatting.

import os
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "Path to input CSV file")
parser.add_argument("--output",  help = "Path to output CSV file")
args = parser.parse_args()

BASE_DIR = os.path.dirname(__file__)
reader_fallback = os.path.join(BASE_DIR, "test_files/users_messy.csv")
writer_fallback = os.path.join(BASE_DIR, "test_files/users_clean.csv")

def clean_csv():
    try:
        input_path = args.input if args.input else reader_fallback
        output_path = args.output if args.output else writer_fallback
        with open(input_path, "r", encoding = "utf-8") as users_messy, open(output_path, "w", encoding = "utf-8", newline = "") as users_clean:
            print(f"[INFO] Reading from: {input_path}")
            print(f"[INFO] Writing to: {output_path}")
            csvreader = csv.DictReader(users_messy)
            csvwriter = csv.DictWriter(users_clean, fieldnames = csvreader.fieldnames, lineterminator = "\n")

            set_uniques = set()
            csvwriter.writeheader()
            for row in csvreader:
                for field in row:
                    if row[field]:
                        row[field] = row[field].strip().title()
                    
                if tuple(row.values()) not in set_uniques:
                    set_uniques.add(tuple(row.values()))
                    csvwriter.writerow(row)

        print("[SUCCESS] CSV cleaned successfully")

    except FileNotFoundError:
        print("[ERROR] File doesn't exist")
    except IOError:
        print("[ERROR] Failed to write data to file")

if __name__ == "__main__":
    clean_csv()