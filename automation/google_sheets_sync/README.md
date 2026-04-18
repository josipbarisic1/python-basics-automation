# Google Sheets Sync

**Problem:**  
Need to read data from Google Sheets, process it, and write results back - manual work is slow.

**Solution:**  
Automated sync - reads Google Sheets data, filters by department, writes to new sheet.

## Setup

1. Install dependencies:
`pip install -r requirements.txt`

2. Google Cloud setup:
   - Create project at https://console.cloud.google.com/
   - Enable Google Sheets API
   - Create Service Account
   - Download JSON key as `service-account.json`
   - Place in this folder

3. Share your Google Sheet:
   - Open `service-account.json`
   - Copy the email address (sheets-automation@...)
   - Share your Google Sheet with that email (Editor access)

4. Configure:
   - Copy Sheet ID from URL
   - Edit `config.json` with your sheet_id

## Run

**Note:** Run from the `google_sheets_sync/` directory.

```
python sheets_sync.py
python sheets_sync.py --help
python sheets_sync.py --department Sales
```

**Options:**
`--department`  department to filter (default: Engineering)

## What it does

- Connects to Google Sheets via Service Account
- Reads all data from first sheet
- Filters by department
- Creates new sheet with filtered data
- Auto-names output sheet (e.g., "Engineering Only")
- Shows rows processed count

## Config

Edit `config.json`:
- `service_account_file`: path to JSON key
- `sheet_id`: Google Sheet ID from URL

## Security

- `service-account.json` contains credentials
- `config.json` contains sheet ID
- Never commit these to Git
- Use `config.example.json` as template

## Example workflow

1. Employee data in "Sheet1"
2. Run script with `--department Engineering`
3. New sheet "Engineering Only" created with filtered data
