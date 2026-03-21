# Day 11
# Script that scrapes data from a webpage
# extracts specific fields
# and saves results to CSV.

# All books under 20£, rated 4 or above -> csv: title,rating,price,availability

import csv
import requests
from bs4 import BeautifulSoup


def return_pages_and_parse_data():
    try:
        with open("test_files_extractor/scraped_data.csv", "w", encoding = "utf-8") as scraped_data:
            csvwriter = csv.DictWriter(scraped_data, fieldnames = ["title","rating","price","availability"], lineterminator = "\n")
            csvwriter.writeheader()
            for page in range(1, 51):
                url = f"https://books.toscrape.com/catalogue/page-{page}.html"

                response = requests.get(url)
                response.encoding = "utf-8"

                if response.status_code == 200:
                    html = response.text
                else:
                    print(f'Failed to return data, status code: {response.status_code}')
                    exit()

                soup = BeautifulSoup(html, "html.parser")

                filter_books_and_write(soup, csvwriter)



    except IOError:
        print("Failed to write data to file")
        exit()

def filter_books_and_write(soup, csvwriter):
    products = soup.find_all("article", class_="product_pod")
    for product in products:
        product_title = product.find("h3").find("a")["title"]

        price = product.find("p", class_="price_color")
        product_price = price.text
        if float(product_price[1:]) >= 20:
            continue

        availability = product.find("p", class_="availability")
        if "instock" in availability["class"]:
            product_availability = "In Stock"
        else:
            product_availability = "Out of Stock"

        rating = product.find("p", class_="star-rating")
        if "Four" in rating["class"]:
            product_rating = 4
        elif "Five" in rating["class"]:
            product_rating = 5
        else:
            continue

        csvwriter.writerow({
            "title": product_title,
            "rating": product_rating,
            "price": product_price,
            "availability": product_availability
        })



if __name__ == "__main__":
    return_pages_and_parse_data()


