import pdfplumber
import pandas as pd

def extract_tables(uploaded_file):

    tables_data = []

    with pdfplumber.open(uploaded_file) as pdf:

        for page_num, page in enumerate(pdf.pages, start=1):

            tables = page.extract_tables()

            for table_num, table in enumerate(tables, start=1):

                df = pd.DataFrame(table)

                tables_data.append({
                    "page": page_num,
                    "table_number": table_num,
                    "dataframe": df
                })

    return tables_data
