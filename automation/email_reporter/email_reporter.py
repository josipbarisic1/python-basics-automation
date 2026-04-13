import smtplib
import json
import os
import logging
import sys
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import argparse


logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description="Generates CSV report and sends via email with attachment"
)
parser.add_argument(
    "--input",
    help="Path to input CSV file (default: from config.json)",
    metavar="FILE"
)
parser.add_argument(
    "--subject",
    help="Email subject line (default: from config.json)",
    metavar="TEXT"
)
parser.add_argument(
    "--recipient",
    help="Email recipient address (default: from config.json)",
    metavar="EMAIL"
)
args = parser.parse_args()

if args.input and not os.path.exists(args.input):
    logger.error(f"Input file not found: {args.input}")
    sys.exit(1)

    

def load_config(config_path=None):
    if config_path is None:
        base_dir = os.path.dirname(__file__)
        config_path = os.path.join(base_dir, "config.json")
    
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        logger.info(f"Loaded config from {config_path}")
        return config
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config: {e}")
        sys.exit(1)

def generate_report(csv_path):
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        if not data:
            return "No data found in CSV."
        
        total_rows = len(data)
        fieldnames = list(data[0].keys())
        
        report = f"CSV Report Summary\n"
        report += f"=" * 50 + "\n\n"
        report += f"Total rows: {total_rows}\n"
        report += f"Columns: {', '.join(fieldnames)}\n\n"
        
        report += f"First 5 entries:\n"
        report += "-" * 50 + "\n"
        for i, row in enumerate(data[:5], 1):
            report += f"{i}. {row}\n"
        
        return report
        
    except FileNotFoundError:
        logger.error(f"CSV file not found: {csv_path}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to generate report: {e}")
        sys.exit(1)

def attach_csv(msg, csv_path):
    try:
        with open(csv_path, 'rb') as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
        
        encoders.encode_base64(part)
        
        filename = os.path.basename(csv_path)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={filename}'
        )
        
        msg.attach(part)
        logger.info(f"Attached file: {filename}")
    except FileNotFoundError:
        logger.error(f"CSV file not found: {csv_path}")
        sys.exit(1)

def send_email(config, subject, body, recipient, csv_path=None):
    msg = MIMEMultipart()
    msg['From'] = config['smtp']['email']
    msg['To'] = recipient
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    if csv_path:
        attach_csv(msg, csv_path)
    
    try:
        server = smtplib.SMTP(config['smtp']['server'], config['smtp']['port'])
        server.starttls()
        server.login(config['smtp']['email'], config['smtp']['password'])
        server.send_message(msg)
        server.quit()
        print("\n[SUCCESS] Email sent!")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s'
    )
    
    config = load_config()
    csv_path = args.input if args.input else config["paths"]["input"]
    subject = args.subject if args.subject else config["report"]["subject"]
    recipient = args.recipient if args.recipient else config["recipient"]
    
    report = generate_report(csv_path)
    send_email(config, subject, report, recipient, csv_path)
    
    print(f"[SUCCESS] Report sent to {recipient}")
    print(f"  Subject: {subject}")
    print(f"  Attachment: {os.path.basename(csv_path)}")

if __name__ == "__main__":
    main()
