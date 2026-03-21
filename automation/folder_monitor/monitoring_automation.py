# Day 13
# Folder monitoring automation
# detect new CSV files in a folder
# automatically process them
# output cleaned files to another folder

import os
import csv
import time

monitor_path = "test_files/monitor"
clean_path = "test_files/clean"
processed_files = set()


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
        with open(os.path.join(monitor_path, new_file), "r") as new_file_messy, open(os.path.join(clean_path, new_name), "w") as new_file_clean:
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
            
    except FileNotFoundError:
        print("File doesn't exist")
    except IOError:
        print("Failed to write data to file")
    
    return True



def main():
    while True:
        print("Checking for new files...")
        new_files = check_new_files()
        if new_files:
            print("New .csv file detected. \nProcessing now...")
            for new_file in new_files:
                success = clean_csv(new_file)
                if success:
                    processed_files.add(new_file)
                    print(f"{new_file} processed successfully.")

        time.sleep(10)


if __name__ == "__main__":
    main()