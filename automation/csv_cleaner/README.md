CSV Cleaner

Cleans messy CSV data.

Run:

python csv_cleaner.py
python csv_cleaner.py --input messy.csv --output clean.csv

Options:
--input   input CSV (default: test_files/users_messy.csv)
--output  output CSV (default: test_files/users_clean.csv)

What it does:
- Removes duplicates
- Trims whitespace
- Converts to title case
- Standardizes formatting
