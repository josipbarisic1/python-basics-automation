CSV Merger

Problem:
Multiple monthly CSV files need to be combined into one chronological dataset.

Solution:
Automatically merges all monthly files, sorts chronologically, outputs single CSV.

Run:

python csv_merger.py
python csv_merger.py --help
python csv_merger.py --input folder/ --output merged.csv

Options:
--input   folder with CSVs (default: test_files/)
--output  merged CSV (default: test_files/merged_sales.csv)

Input format:
Files named: sales_january.csv, sales_february.csv, etc.

Output:
Shows files merged and total rows processed.
