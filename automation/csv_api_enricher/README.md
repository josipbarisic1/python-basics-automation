CSV API Enricher

Enriches CSV data by matching rows with data from a public API and exporting the result to a new CSV file.

How to run:

Default mode:
python csv_api_enricher/csv_api_enricher.py

Custom configuration:
python csv_api_enricher/csv_api_enricher.py --input path/to/input.csv --output path/to/output.csv

Options:
--input "Path to input CSV file (default: test_files/basic_user_info.csv)"
--output "Path to output CSV file (default: test_files/expanded_user_info.csv)"

What it does:
- Loads data from a CSV file
- Fetches user data from a public API
- Matches CSV rows with API data (by email)
- Handles missing or unmatched records safely
- Extracts relevant fields (name, company, city)
- Merges CSV and API data into a single dataset
- Exports enriched data to a new CSV file

Example output:

name,email,company,city
Leanne Graham,Sincere@april.biz,Romaguera-Crona,Gwenborough
[not_found],notfound@test.com,,