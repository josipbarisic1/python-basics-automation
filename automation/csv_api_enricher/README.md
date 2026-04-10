CSV API Enricher

Enriches CSV data by matching with API data.

Setup:

pip install -r requirements.txt

Run:

python csv_api_enricher.py
python csv_api_enricher.py --help
python csv_api_enricher.py --input basic.csv --output enriched.csv

Options:
--input   input CSV (default: test_files/basic_user_info.csv)
--output  output CSV (default: test_files/expanded_user_info.csv)

What it does:
- Loads CSV
- Fetches API data
- Matches by email
- Handles missing records
- Merges data
- Exports enriched CSV
- Shows rows enriched count

Example output:

name,email,company,city
Leanne Graham,Sincere@april.biz,Romaguera-Crona,Gwenborough
[not_found],notfound@test.com,,
