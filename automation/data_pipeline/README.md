Book Data Pipeline

Scrapes books, filters by input CSV, enriches with API data, exports to CSV.

Structure:

Refactored into modules:
- main.py → CLI + orchestration
- scraper.py → scraping + pagination
- processor.py → cleaning + filtering
- api.py → API calls
- enricher.py → data enrichment
- writer.py → CSV I/O
- book_data_pipeline.py → old version (reference)

Uses logging instead of print.

Setup:

pip install -r requirements.txt

Run:

Note: Must be run from the data_pipeline/ directory.

python main.py
python main.py --input custom.csv --output result.csv

Options:
--input   input CSV path (default: test_files/input_books.csv)
--output  output CSV path (default: test_files/user_books.csv)

What it does:
- Scrapes books.toscrape.com
- Retries failed requests
- Follows pagination automatically
- Cleans and filters data
- Matches against input CSV
- Fetches users from API
- Enriches books with user info
- Saves to CSV

Example output:

title,price,rating,available,user_name,email,company
Book A,15.99,5,True,Leanne Graham,Sincere@april.biz,Romaguera-Crona
