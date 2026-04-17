PDF Report Generator

Problem:
Need to convert CSV data into professional PDF reports - manual formatting is time-consuming.

Solution:
Automated PDF generation - reads CSV, creates formatted PDF with table and summary.

Setup:

pip install -r requirements.txt

Run:

Note: Run from the pdf_generator/ directory.

python pdf_generator.py
python pdf_generator.py --help
python pdf_generator.py --input data.csv --output report.pdf --title "Company Sales Report"

Options:
--input   input CSV file (default: from config.json)
--output  output PDF file (default: from config.json)
--title   report title (default: from config.json)

What it does:
- Loads CSV data
- Generates summary statistics
- Creates formatted PDF table
- Adds title and styling
- Shows rows processed count

Config:

Edit config.json:
- paths: input CSV and output PDF paths
- report: title and author

PDF features:
- Professional table formatting
- Header row with grey background
- Centered alignment
- Grid borders
- Summary statistics

Example use cases:
- Sales reports
- Employee lists
- Inventory reports
- Data exports for clients
