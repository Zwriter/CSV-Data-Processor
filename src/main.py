from ingestion.csv_reader import reader
from transformation.normalizer import normalize
from config.config import ACCEPTED_DATE_FORMATS
from config.customer_config import CUSTOMER_DATE_COLUMN

def customer_normalizer():
    df = reader("data/raw/customers.csv")
    df = normalize(
        df, 
        date_column=CUSTOMER_DATE_COLUMN, 
        accepted_formats=ACCEPTED_DATE_FORMATS
    )
    return df

if __name__ == "__main__":
    print(customer_normalizer())
    