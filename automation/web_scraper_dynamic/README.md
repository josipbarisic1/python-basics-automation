Dynamic Web Scraper

Scrapes books with automatic pagination.

Setup:

pip install -r requirements.txt

Run:

python dynamic_scraper.py
python dynamic_scraper.py --output custom.csv

Options:
--output  output CSV (default: test_files/clean_books.csv)

What it does:
- Scrapes all pages automatically
- Follows "next page" links
- Uses browser-like headers
- Retries failed requests (3x)
- Stops if page fails (fail-fast)
- Adds delay between requests
- Filters by rating (4-5 stars)
- Filters by price (under £20)
- Exports to CSV

Output:
test_files/clean_books.csv
