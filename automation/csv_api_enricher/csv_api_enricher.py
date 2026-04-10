# CSV API ENRICHER
# load CSV data
# fetch data from API
# match and enrich records
# save results to CSV
# CLI arguments for input/output

import os
import csv
import requests
import argparse
import sys

parser = argparse.ArgumentParser(
    description="Enriches CSV data by matching with API user data"
)
parser.add_argument(
    "--input",
    help="Path to input CSV file (default: test_files/basic_user_info.csv)",
    metavar="FILE"
)
parser.add_argument(
    "--output",
    help="Path to output CSV file (default: test_files/expanded_user_info.csv)",
    metavar="FILE"
)
args = parser.parse_args()

if args.input and not os.path.exists(args.input):
    print(f"[ERROR] Input file not found: {args.input}")
    sys.exit(1)

BASE_DIR = os.path.dirname(__file__)
reader_fallback = os.path.join(BASE_DIR, "test_files/basic_user_info.csv")
writer_fallback = os.path.join(BASE_DIR, "test_files/expanded_user_info.csv")

api = "https://jsonplaceholder.typicode.com/users"

input_path = args.input if args.input else reader_fallback
output_path = args.output if args.output else writer_fallback

def load_data():
    try:
        with open(input_path, "r", encoding="utf-8") as input_csv:
            csvreader = csv.DictReader(input_csv)
            return list(csvreader)
        
    except FileNotFoundError:
        print("[ERROR] File doesn't exist")
        sys.exit(1)

def fetch_data():
    try:
        response = requests.get(api, timeout = 5)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        sys.exit(1)

    if response.status_code != 200:
        print(f"[ERROR] Failed request: {response.status_code}")
        sys.exit(1)
    try:
        data = response.json()
    except ValueError:
        print("[ERROR] Failed to parse JSON response")
        sys.exit(1)

    if not isinstance(data, list):
        print("[ERROR] Unexpected API format")
        sys.exit(1)
    return data

def build_lookup(fetched_data):
    lookup = {}
    for user in fetched_data:
        if not isinstance(user, dict):
            continue

        email = user.get("email")
        if email:
            lookup[email.lower()] = user
    
    return lookup


def process_data(csv_rows, lookup):
    processed_users = []
    for row in csv_rows:

        raw_email = row.get("email") or ""
        email = raw_email.lower()
        api_user = lookup.get(email)

        if api_user:

            name = api_user.get("name", "[missing_name]")
            
            company_data = api_user.get("company") or {}
            company = company_data.get("name", "")

            address = api_user.get("address") or {}
            city = address.get("city", "")
        else:
            name = "[not_found]"
            company = ""
            city = ""

        processed_users.append({
            "name": name,
            "email": raw_email,
            "company": company,
            "city": city
        })

    return processed_users

def save_data(processed_users):
    try:
        dir_name = os.path.dirname(output_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok = True)
        with open(output_path, "w", encoding = "utf-8", newline = "") as users_details:
            
            csvwriter = csv.DictWriter(users_details, fieldnames = ["name", "email", "company", "city"], lineterminator = "\n")

            csvwriter.writeheader()
            for user in processed_users:
                csvwriter.writerow(user)

        print(f"\n[SUCCESS] File saved successfully")
        print(f"  Rows enriched: {len(processed_users)}")
        print(f"  Output: {output_path}")
                                    
    except IOError:
        print("[ERROR] Failed to write data to file")

def main():
    csv_rows = load_data()
    print(f"[INFO] Loaded {len(csv_rows)} rows from CSV")

    api_data = fetch_data()
    print(f"[INFO] Fetched {len(api_data)} users from API")

    lookup = build_lookup(api_data)

    enriched = process_data(csv_rows, lookup)
    print(f"[INFO] Processed {len(enriched)} rows")

    save_data(enriched)


if __name__ == "__main__":
    main()