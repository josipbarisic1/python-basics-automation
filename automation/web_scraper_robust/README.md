Robust Web Scraper

Scrapes book data from books.toscrape.com with improved reliability and exports it to CSV.

How to run:

Default mode:
python web_scraper_robust/robust_scraper.py

Custom configuration:
python web_scraper_robust/robust_scraper.py --output path/to/output.csv

Options:
--output "Path to output CSV file (default: test_files/clean_books.csv)"

What it does:
- Scrapes multiple pages of book data
- Uses browser-like headers to avoid blocking
- Retries failed requests (up to 3 attempts)
- Handles request failures and skips broken pages
- Adds delay between requests to reduce detection
- Filters by rating (4–5 stars)
- Filters by price (under £20)
- Cleans and structures scraped data
- Exports results to CSV

Output:
test_files/clean_books.csv