import pandas as pd
import sys
import os
import django

# Set up Django environment
sys.path.append("/path/to/your/django/project")  # Replace with the path to your Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biz.settings")  # Replace with your Django project's settings module
django.setup()

from company.models import Company  # Replace "companies" with the actual name of your app and model

def load_data_from_csv(file_path):
    chunk_size = 1000  # Adjust this value based on your system's memory capacity and performance
    counter = 0

    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        # Process the chunk and save data to the database
        process_chunk(chunk)
        counter += len(chunk)
        print(f"Processed {counter} records.")

def process_chunk(chunk):
    companies = []
    for _, row in chunk.iterrows():
        company = Company(
            COMPANY_PIN=row.get('COMPANY_PIN', None),
            COMPANY_NAME=row.get('COMPANY_NAME', None),
            ITAX_STATUS=row.get('ITAX_STATUS', None),
            COMPANY_REG_STATUS=row.get('COMPANY_REG_STATUS', None),
            PHYSICAL_LOCATION=row.get('PHYSICAL_LOCATION', None),
            POSTAL_ADDRESS=row.get('POSTAL_ADDRESS', None),
            COMPANY_CONTACT=row.get('COMPANY_CONTACT', None),
            BUSINESS_REG_NUM=row.get('BUSINESS_REG_NUM', None),
            EMAIL_ADDRESS=row.get('EMAIL_ADDRESS', None),
            # Add other fields here based on your Company model
        )
        companies.append(company)

    # Save the records in bulk to the database
    Company.objects.bulk_create(companies)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python data_loader.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    load_data_from_csv(file_path)
