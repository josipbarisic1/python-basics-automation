from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import csv
import json
import os
import logging
import sys

logger = logging.getLogger(__name__)

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

def load_csv_data(csv_path):
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        logger.info(f"Loaded {len(data)} rows from CSV")
        return data
    except FileNotFoundError:
        logger.error(f"CSV file not found: {csv_path}")
        sys.exit(1)

def generate_pdf(data, output_path, title, author):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()
    
    title_para = Paragraph(f"<b>{title}</b>", styles['Title'])
    elements.append(title_para)
    elements.append(Spacer(1, 0.3*inch))
    
    summary = f"Total rows: {len(data)}"
    summary_para = Paragraph(summary, styles['Normal'])
    elements.append(summary_para)
    elements.append(Spacer(1, 0.3*inch))
    
    if data:
        headers = list(data[0].keys())
        table_data = [headers]
        
        for row in data:
            table_data.append([str(row[key]) for key in headers])
        
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        elements.append(table)
    
    doc.build(elements)
    logger.info(f"PDF generated: {output_path}")

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s'
    )
    
    config = load_config()
    csv_path = config['paths']['input']
    output_path = config['paths']['output']
    
    data = load_csv_data(csv_path)
    generate_pdf(data, output_path, config['report']['title'], config['report']['author'])
    
    print(f"\n[SUCCESS] PDF generated")
    print(f"  Output: {output_path}")

if __name__ == "__main__":
    main()
