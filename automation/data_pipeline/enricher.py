import random
import logging
import sys

logger = logging.getLogger(__name__)

def enrich_data(matched_books, data_users):
    processed_entries = []
    if not matched_books:
        logger.warning("No matching books found after filtering")

    if not data_users:
        logger.error("No users available for enrichment")
        sys.exit(1)
    
    for row in matched_books:

        title = row.get("title", "")
        price = row.get("price", "")
        rating = row.get("rating", "")
        available = row.get("available", "")

        random_user = random.choice(data_users)

        name = random_user.get("name", "[missing_name]")
        
        company_data = random_user.get("company") or {}
        company = company_data.get("name", "[missing_company]")

        email = random_user.get("email", "[missing_email]")


        processed_entries.append({
            "title": title,
            "price": price,
            "rating": rating,
            "available": available,
            "user_name": name,
            "email": email,
            "company": company,
        })

    logger.info(f"Enriched {len(processed_entries)} rows")
    return processed_entries