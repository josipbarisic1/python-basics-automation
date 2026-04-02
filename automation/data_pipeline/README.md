Book Data Pipeline

Scrapes book data, filters it based on input CSV, enriches it with API data, and exports to CSV.

How to run:

Default mode:
python data_pipeline/book_data_pipeline.py

Custom configuration:
python data_pipeline/book_data_pipeline.py --input path/to/input.csv --output path/to/output.csv

Options:
--input "Path to input CSV file (default: test_files/input_books.csv)"
--output "Path to output CSV file (default: test_files/user_books.csv)"

What it does:
- Scrapes book data from books.toscrape.com
- Handles request retries and failures
- Automatically follows pagination
- Cleans and filters scraped data
- Loads input CSV with target book titles
- Filters only matching books
- Fetches user data from API
- Enriches book data with random user info
- Saves final structured data to CSV

Example output:

title,price,rating,available,user_name,email,company
Book A,15.99,5,True,Leanne Graham,Sincere@april.biz,Romaguera-Crona