import requests
from bs4 import BeautifulSoup
import time
import random
import logging

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36"
}


def scrape_data(config):
    data = []
    base_url = config["base_url"]
    url = base_url + "page-1.html"
    page = 1
    max_pages = config.get("max_pages", 999)

    while url and page <= max_pages:     

        if page > 1:
            delay_min = config["delay_min"]
            delay_max = config["delay_max"]
            logger.info(f"Sleeping before page {page}...")
            time.sleep(random.uniform(delay_min, delay_max))

        response = _fetch_page(url, page, config)

        if not response:
            logger.error(f"Request failed completely for page {page}, skipping")
            break
        elif response.status_code != 200:
            logger.error(f"Failed request: {response.status_code}, skipping page")
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
            url = base_url + next_page
        else:
            url = None

        page += 1

    logger.info(f"Scraped {len(data)} books total")
    return data

def _fetch_page(url, page, config):
    response = None
    retry_attempts = config["retry_attempts"]
    timeout = config["timeout"]
    for attempt in range(retry_attempts):
            try:
                response = requests.get(url, headers = HEADERS, timeout = timeout)
                response.encoding = "utf-8"

                if response.status_code == 200:
                    break
                else:
                    logger.warning(f"Attempt {attempt + 1}, page {page} failed: {response.status_code}")
            
            except requests.exceptions.RequestException as e:
                logger.warning(f"Attempt {attempt + 1}, page {page} failed: {e}")
    return response