# API DATA FETCHER
# fetch data from public API
# save to CSV
# CLI arguments for output

import os
import csv
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--output", help = "Path to output file")
parser.add_argument("--limit", type = int, help = "Number of fetched users")
args = parser.parse_args()

BASE_DIR = os.path.dirname(__file__)
writer_fallback = os.path.join(BASE_DIR, "test_files/users_api.csv")

api = "https://jsonplaceholder.typicode.com/users"
users_path = args.output if args.output else writer_fallback
limit = args.limit if args.limit else 10
if limit <= 0:
    print("[ERROR] Limit must be greater than 0")
    exit()

def fetch_data():

    data = []
    response = requests.get(api)

    if response.status_code != 200:
        print(f"Failed request: {response.status_code}")
        exit()
    else:
        data = response.json()
        fetched_users = data[:limit]

    return fetched_users

def process_data(fetched_users):

    processed_users = []
    for user in fetched_users:
        name = user["name"]
        email = user["email"]
        company = user["company"]["name"]
        city = user["address"]["city"]
        processed_users.append({
            "name": name,
            "email": email,
            "company": company,
            "city": city
        })
    return processed_users

def save_data(processed_users):
    try:
        dir_name = os.path.dirname(users_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok = True)
        with open(users_path, "w", encoding = "utf-8", newline = "") as users_details:
            
            csvwriter = csv.DictWriter(users_details, fieldnames = ["name", "email", "company", "city"], lineterminator = "\n")

            csvwriter.writeheader()
            for user in processed_users:
                csvwriter.writerow(user)

        print("[SUCCESS] File saved successfully")
                                    
    except IOError:
        print("[ERROR] Failed to write data to file")

def main():
    raw_data = fetch_data()
    print(f"[INFO] Fetched {len(raw_data)} users")

    clean_data = process_data(raw_data)
    print(f"[INFO] Cleaned {len(clean_data)} users")

    save_data(clean_data)


if __name__ == "__main__":
    main()