import pandas as pd

customer_required_fields = ["customer_id","first_name","last_name","email","signup_date"]

def validate_customers(df):
    if not any(key in df for key in customer_required_fields):
        raise ValueError(f"Headers not included: {customer_required_fields}")

    return