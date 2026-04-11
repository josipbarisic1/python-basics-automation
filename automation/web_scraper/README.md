Web Scraper

Problem:
Need book data from website for analysis.

Solution:
Scrapes books.toscrape.com, filters by rating and price, exports to CSV.

Setup:

pip install -r requirements.txt

Run:

python scraper_pipeline.py

What it does:
- Scrapes 5 pages
- Filters by rating (4-5 stars)
- Filters by price (under £20)
- Exports to CSV

Output:
test_files/clean_books.csv

Note:
http_extractor_old.py is old version before refactor.
