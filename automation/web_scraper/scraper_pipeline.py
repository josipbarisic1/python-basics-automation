# Day 12
# Refactored automation script that separates
# scraping, processing and exporting logic.


import csv
import requests
from bs4 import BeautifulSoup


def scrape_data():
    data = []

    for page in range(1, 6):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        response = requests.get(url)
        response.encoding = "utf-8"

        if response.status_code != 200:
            print(f"Failed request: {response.status_code}")
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
        with open("test_files/clean_books.csv", "w", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "price", "rating", "available"],
                lineterminator="\n"
            )

            writer.writeheader()

            for row in data:
                writer.writerow(row)

    except IOError:
        print("Failed to write file")


def main():
    raw_data = scrape_data()
    clean_data = process_data(raw_data)
    save_data(clean_data)


if __name__ == "__main__":
    main()