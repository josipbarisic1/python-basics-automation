Robust Web Scraper

Problem:
Web scraping fails due to timeouts, blocks, or connection issues.

Solution:
Scrapes with retry logic, browser-like headers, delays - handles failures gracefully.

Setup:

pip install -r requirements.txt

Run:

python robust_scraper.py
python robust_scraper.py --help
python robust_scraper.py --output custom.csv

Options:
--output  output CSV (default: test_files/clean_books.csv)

What it does:
- Scrapes multiple pages
- Uses browser-like headers
- Retries failed requests (3x)
- Handles failures, skips broken pages
- Adds delay between requests
- Filters by rating (4-5 stars)
- Filters by price (under £20)
- Exports to CSV
- Shows books scraped count

Output:
test_files/clean_books.csv
