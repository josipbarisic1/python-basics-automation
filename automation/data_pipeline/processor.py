import logging

logger = logging.getLogger(__name__)

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

    logger.info(f"Processed {len(processed)} books after filtering")
    return processed

def filter_books(clean_books, loaded_titles):
    matched_books = []
    titles = {row.get("title", "").strip().lower() for row in loaded_titles}

    for row in clean_books:
        title = row.get("title", "").strip().lower()

        if title not in titles:
            continue
    
        matched_books.append(row)
    
    logger.info(f"Matched {len(matched_books)} books against input list")
    return matched_books