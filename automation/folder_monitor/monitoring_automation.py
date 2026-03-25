# Day 13
# Folder monitoring automation
# detect new CSV files in a folder
# automatically process them
# output cleaned files to another folder

import os
import csv
import time
import argparse

processed_files = set()

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "Path to monitored folder")
parser.add_argument("--output", help = "Path to output folder")
parser.add_argument("--interval", type = int, help = "Check interval in seconds")
args = parser.parse_args()

BASE_DIR = os.path.dirname(__file__)
monitor_fallback = os.path.join(BASE_DIR, "test_files/monitor")
writer_fallback = os.path.join(BASE_DIR, "test_files/clean")

monitor_path = args.input if args.input else monitor_fallback
clean_path = args.output if args.output else writer_fallback
interval = args.interval if args.interval else 5

def check_new_files():
    files = os.listdir(monitor_path)
    new_files = []
    for file in files:
        full_path_src = os.path.join(monitor_path, file)
        is_file = os.path.isfile(full_path_src)
        if is_file and file.lower().endswith(".csv") and file not in processed_files:
            new_files.append(file)
    return new_files


def clean_csv(new_file):
    try:
        name, ext = os.path.splitext(new_file)
        new_name = f"{name}_clean{ext}"
        input_file = os.path.join(monitor_path, new_file)
        output_file = os.path.join(clean_path, new_name)
        with open(input_file, "r", encoding = "utf-8") as new_file_messy, open(output_file, "w", encoding = "utf-8", newline = "") as new_file_clean:
            csvreader = csv.DictReader(new_file_messy)
            csvwriter = csv.DictWriter(new_file_clean, fieldnames = csvreader.fieldnames, lineterminator = "\n")

            set_uniques = set()
            csvwriter.writeheader()
            for row in csvreader:
                for field in row:
                    if row[field]:
                        row[field] = row[field].strip().title()
                    
                if tuple(row.values()) not in set_uniques and any(row.values()):
                    set_uniques.add(tuple(row.values()))
                    csvwriter.writerow(row)
        return True
            
    except FileNotFoundError:
        print("[ERROR] File doesn't exist")
        return False
    except IOError:
        print("[ERROR] Failed to write data to file")
        return False
    



def main():
    while True:
        print("[INFO] Checking for new files...")
        new_files = check_new_files()
        if new_files:
            print(f"[INFO] {len(new_files)} new file(s) detected. \nProcessing now...")
            for new_file in new_files:
                success = clean_csv(new_file)
                if success:
                    processed_files.add(new_file)
                    print(f"[SUCCESS] {new_file} processed successfully.")

        time.sleep(interval)


if __name__ == "__main__":
    main()