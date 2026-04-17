CSV Cleaner

Problem:
Messy CSV data with duplicates, inconsistent formatting, extra whitespace.

Solution:
Automated cleaning - removes duplicates, trims whitespace, standardizes to title case.

Setup:

pip install -r requirements.txt

Run:

Note: Run from the csv_cleaner/ directory.

python csv_cleaner.py
python csv_cleaner.py --help
python csv_cleaner.py --input messy.csv --output clean.csv

Options:
--input   input CSV (default: test_files/users_messy.csv)
--output  output CSV (default: test_files/users_clean.csv)

What it does:
- Removes duplicates
- Trims whitespace
- Converts to title case
- Standardizes formatting
- Shows processed row count
