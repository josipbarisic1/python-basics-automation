# Day 10
# Script that cleans messy CSV data
# removes duplicates
# and standardizes formatting.

import csv

path = "test_files"

def clean_csv():
    try:
        with open(f"{path}/users_messy.csv", "r") as users_messy, open(f"{path}/users_clean.csv", "w") as users_clean:
            csvreader = csv.DictReader(users_messy)
            csvwriter = csv.DictWriter(users_clean, fieldnames = csvreader.fieldnames, lineterminator = "\n")

            set_uniques = set()
            csvwriter.writeheader()
            for row in csvreader:
                for attribute in row:
                    #print(f"|{row[e]}|")
                    row[attribute] = row[attribute].strip().title()
                    
                if tuple(row.values()) not in set_uniques:
                    set_uniques.add(tuple(row.values()))
                    csvwriter.writerow(row)
            
    except FileNotFoundError:
        print("File doesn't exist")
    except IOError:
        print("Failed to write data to file")

if __name__ == "__main__":
    clean_csv()