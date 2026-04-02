# BOOK DATA PIPELINE
# load target book titles from CSV
# scrape books with dynamic pagination
# clean and filter scraped data
# match books against input list
# fetch user data from API
# enrich book data with user information
# save final dataset to CSV
# CLI arguments for input/output

import csv
import requests
from bs4 import BeautifulSoup
import time
import random
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "Path to input file")
parser.add_argument("--output", help = "Path to output file")
args = parser.parse_args()

BASE_DIR = os.path.dirname(__file__)
reader_fallback = os.path.join(BASE_DIR, "test_files/input_books.csv")
writer_fallback = os.path.join(BASE_DIR, "test_files/user_books.csv")

input_path = args.input if args.input else reader_fallback
output_path = args.output if args.output else writer_fallback

api = "https://jsonplaceholder.typicode.com/users"

headers = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36"
}

def load_input_titles():
    try:
        with open(input_path, "r", encoding="utf-8") as input_books:
            csvreader = csv.DictReader(input_books)
            return list(csvreader)
        
    except FileNotFoundError:
        print("[ERROR] File doesn't exist")
        exit()

def scrape_data():
    data = []
    url = "https://books.toscrape.com/catalogue/page-1.html"
    page = 1

    while url:     

        if page > 1:
            print(f"[INFO] Sleeping before {page}. page...")
            time.sleep(random.uniform(1, 3))

        response = None
        for attempt in range(3):
            try:
                response = requests.get(url, headers = headers, timeout = 5)
                response.encoding = "utf-8"

                if response.status_code == 200:
                    break
                else:
                    print(f"[ERROR] Attempt {attempt + 1}, page {page} failed: {response.status_code}")
            
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] Attempt {attempt + 1}, page {page} failed: {e}")

        if not response:
            print(f"[ERROR] Request failed completely for page {page}, skipping")
            break
        elif response.status_code != 200:
            print(f"[ERROR] Failed request: {response.status_code}, skipping page")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("article", class_="product_pod")

        for product in products:
            title = product.find("h3").find("a")["title"]
            price = product.find("p", class_="price_color").text
            availability = product.find("p", class_="availability").text.strip()
            rating_class = product.find("p", class_="star-rating")["class"]

            data.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating_class": rating_class
            })
        
        next_button = soup.find("li", class_="next")
        if next_button:
            next_page = next_button.find("a")["href"]
            url = "https://books.toscrape.com/catalogue/" + next_page
        else:
            url = None

        page += 1

    return data


def process_data(data):
    processed = []

    for item in data:
        title = item["title"].strip()

        price = float(item["price"].replace("£", "").replace("Â", ""))

        availability = True if "In stock" in item["availability"] else False

        if "Five" in item["rating_class"]:
            rating = 5
        elif "Four" in item["rating_class"]:
            rating = 4
        else:
            continue

        if price >= 20:
            continue

        processed.append({
            "title": title,
            "price": price,
            "rating": rating,
            "available": availability
        })

    return processed

def fetch_data():
    try:
        response = requests.get(api, timeout = 5)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        exit()

    if response.status_code != 200:
        print(f"[ERROR] Failed request: {response.status_code}")
        exit()
    try:
        data_users = response.json()
    except ValueError:
        print("[ERROR] Failed to parse JSON response")
        exit()

    if not isinstance(data_users, list):
        print("[ERROR] Unexpected API format")
        exit()
    return data_users

def filter_books(clean_data_books, loaded_titles):
    matched_books = []
    titles = {row.get("title", "").strip().lower() for row in loaded_titles}

    for row in clean_data_books:
        title = row.get("title", "").strip().lower()

        if title not in titles:
            continue
    
        matched_books.append(row)
        
    
    return matched_books

def enrich_data(matched_books, data_users):
    processed_entries = []
    if not matched_books:
        print("[WARNING] No matching books found after filtering")

    if not data_users:
        print("[ERROR] No users available for enrichment")
        exit()
    
    for row in matched_books:

        title = row.get("title", "")
        price = row.get("price", "")
        rating = row.get("rating", "")
        availability = row.get("available", "")

        random_user = random.choice(data_users)

        name = random_user.get("name", "[missing_name]")
        
        company_data = random_user.get("company") or {}
        company = company_data.get("name", "[missing_company]")

        email = random_user.get("email", "[missing_email]")


        processed_entries.append({
            "title": title,
            "price": price,
            "rating": rating,
            "available": availability,
            "user_name": name,
            "email": email,
            "company": company,
        })

    return processed_entries

def save_data(processed_entries):

    if not processed_entries:
        print("[INFO] No data to save, exiting...")
        exit()
    try:
        dir_name = os.path.dirname(output_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok = True)
        with open(output_path, "w", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "price", "rating", "available", "user_name", "email", "company"],
                lineterminator="\n"
            )

            writer.writeheader()

            for row in processed_entries:
                writer.writerow(row)

    except IOError:
        print("[ERROR] Failed to write file")


def main():
    loaded_titles = load_input_titles()
    print(f"[INFO] Loaded {len(loaded_titles)} rows from CSV")
    
    raw_data_books = scrape_data()
    clean_data_books = process_data(raw_data_books)

    print(f"[DEBUG] Raw scraped: {len(raw_data_books)}")
    print(f"[DEBUG] After processing: {len(clean_data_books)}")

    data_users = fetch_data()
    print(f"[INFO] Fetched {len(data_users)} users from API")

    matched_books = filter_books(clean_data_books, loaded_titles)

    enriched = enrich_data(matched_books, data_users)
    print(f"[INFO] Processed {len(enriched)} rows")

    save_data(enriched)
    print("[SUCCESS] Data written to file successfully")

if __name__ == "__main__":
    main()