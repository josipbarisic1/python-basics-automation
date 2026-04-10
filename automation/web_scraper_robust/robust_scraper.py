# ROBUST WEB SCRAPER
# scrape data from website
# handle request failures and retries
# process and filter data
# save results to CSV

import csv
import requests
from bs4 import BeautifulSoup
import time
import random
import os
import argparse
import sys

parser = argparse.ArgumentParser(
    description="Scrapes book data with retry logic and exports to CSV"
)
parser.add_argument(
    "--output",
    help="Path to output CSV file (default: test_files/clean_books.csv)",
    metavar="FILE"
)
args = parser.parse_args()

BASE_DIR = os.path.dirname(__file__)
writer_fallback = os.path.join(BASE_DIR, "test_files/clean_books.csv")

output_path = args.output if args.output else writer_fallback

headers = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_data():
    data = []

    for page in range(1, 6):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        if page > 1:
            print(f"[INFO] Sleeping before next page...")
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
            continue
        elif response.status_code != 200:
            print(f"[ERROR] Failed request: {response.status_code}, skipping page")
            continue

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


def save_data(data):
    try:
        dir_name = os.path.dirname(output_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok = True)
        with open(output_path, "w", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "price", "rating", "available"],
                lineterminator="\n"
            )

            writer.writeheader()

            for row in data:
                writer.writerow(row)

        print(f"\n[SUCCESS] Data saved successfully")
        print(f"  Books scraped: {len(data)}")
        print(f"  Output: {output_path}")

    except IOError:
        print("[ERROR] Failed to write file")
        sys.exit(1)


def main():
    print("[INFO] Starting scraper...")
    raw_data = scrape_data()
    print(f"[INFO] Scraped {len(raw_data)} books")
    
    clean_data = process_data(raw_data)
    print(f"[INFO] Filtered to {len(clean_data)} books")
    
    save_data(clean_data)


if __name__ == "__main__":
    main()