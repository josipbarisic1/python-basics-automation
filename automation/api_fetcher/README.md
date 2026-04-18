# API Data Fetcher

**Problem:**  
Need to fetch user data from API and convert to CSV for analysis.

**Solution:**  
Fetches data from API, validates, handles errors, exports clean CSV.

## Setup

`pip install -r requirements.txt`

## Run

**Note:** Run from the `api_fetcher/` directory.

`python api_fetcher.py`
`python api_fetcher.py --help`
`python api_fetcher.py --output custom.csv --limit 5`

**Options:**
`--output`  output path (default: `test_files/users_api.csv`)
`--limit`   number of users (default: 10)

## What it does

- Fetches users from API
- Validates data
- Handles request failures
- Parses JSON safely
- Handles missing fields
- Exports to CSV
- Shows users fetched count

## Example output

```
name,email,company,city
Leanne Graham,Sincere@april.biz,Romaguera-Crona,Gwenborough
Ervin Howell,[missing_email],Deckow-Crist,South Elvis
```
