# Email Reporter

**Problem:**  
Need to send automated CSV reports via email - manual sending is time-consuming.

**Solution:**  
Generates summary report from CSV, sends email with attachment automatically.

## Setup

1. Configure SMTP settings in `config.json` (see `config.example.json`)
2. For Gmail: generate App Password at https://myaccount.google.com/apppasswords

## Run

**Note:** Run from the `email_reporter/` directory.

`python email_reporter.py`
`python email_reporter.py --help`
`python email_reporter.py --input data.csv --subject "Weekly Report" --recipient client@example.com`

**Options:**
`--input`      input CSV file (default: from `config.json`)
`--subject`    email subject (default: from `config.json`)
`--recipient`  recipient email (default: from `config.json`)

## What it does

- Loads CSV data
- Generates summary report (row count, columns, first 5 entries)
- Attaches CSV file
- Sends email via SMTP
- Shows confirmation with recipient and attachment info

## Config

Edit `config.json`:
- SMTP settings (server, port, email, password)
- Default recipient
- Default CSV path
- Default subject line

## Security

- `config.json` contains sensitive data (password)
- Never commit `config.json` to Git
- Use `config.example.json` as template
For production use, consider SendGrid API or OAuth2 instead of App Passwords.
