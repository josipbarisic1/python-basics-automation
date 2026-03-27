CSV Merger

Merges multiple monthly CSV files into one combined dataset, sorted chronologically.

How to run:

Default mode (uses test files):
 python csv_merger/csv_merger.py

Custom input/output:
 python csv_merger/csv_merger.py --input path/to/folder --output path/to/merged.csv

Options:
--input     Path to folder containing CSV files (default: test_files/)
--output    Path to output merged CSV file (default: test_files/merged_sales.csv)

Input format:
Files should be named: sales_january.csv, sales_february.csv, etc.