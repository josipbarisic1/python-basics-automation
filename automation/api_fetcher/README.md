API Data Fetcher

Fetches user data from a public API and exports it to CSV.

How to run:

Default mode:
python api_fetcher/api_fetcher.py

Custom configuration:
python api_fetcher/api_fetcher.py --output path/to/csv --limit 5

Options:
--output    Path to output file (default: test_files/users_api.csv)
--limit     Number of users to fetch (default: 10)

What it does:
- Fetches user data from API
- Extracts relevant fields (name, email, company, city)
- Converts JSON data into CSV format
- Limits number of users (optional)