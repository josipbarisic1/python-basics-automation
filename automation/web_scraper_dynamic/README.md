Dynamic Web Scraper

Scrapes book data from books.toscrape.com using automatic pagination and exports it to CSV.

How to run:

Default mode:
python web_scraper_robust/dynamic_scraper.py

Custom configuration:
python web_scraper_robust/dynamic_scraper.py --output path/to/output.csv

Options:
--output "Path to output file (default: test_files/clean_books.csv)"

What it does:
- Scrapes book data across all available pages
- Automatically follows "next page" links
- Uses browser-like headers to avoid blocking
- Retries failed requests (up to 3 attempts)
- Stops execution if a page fails to load
- Adds delay between requests to reduce detection
- Filters by rating (4–5 stars)
- Filters by price (under £20)
- Cleans and structures scraped data
- Exports results to CSV

Output:
test_files/clean_books.csv