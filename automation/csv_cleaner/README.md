CSV Cleaner

Cleans and standardizes messy CSV data.

How to run:

Default mode:
python csv_cleaner/csv_cleaner.py

Custom input/output:
python csv_cleaner/csv_cleaner.py --input path/to/input.csv --output path/to/output.csv

Options:
--input "Path to input CSV file (default: test_files/users_messy.csv)"
--output "Path to output CSV file (default: test_files/users_clean.csv)"

What it does:
- Removes duplicate rows
- Trims whitespace
- Converts text to title case
- Standardizes formatting
- Outputs clean, consistent CSV data