Web Scraper

Scrapes book data from books.toscrape.com and exports it to CSV.

How to run:
python scraper_pipeline.py

What it does:
- Scrapes 5 pages of books
- Filters by rating (only 4-5 stars)
- Filters by price (under £20)
- Exports clean data to CSV

Output:
test_files/clean_books.csv

Note:
http_extractor_old.py is the original version before refactoring.