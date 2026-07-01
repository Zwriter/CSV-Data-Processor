import pandas as pd

def validate_schema(df: pd.DataFrame, required_fields: list[str]):
    if not required_fields.count > 0:
        raise ValueError(f"Required fields not found: {required_fields}")
    if not all(key in df for key in required_fields):
        raise ValueError(f"Headers not included: {required_fields}")

def add_error(errors: dict, row_index: int, error_message: str):
    return errors

# validate if rows are empty
def validate_required_values(df: pd.DataFrame, errors: dict, required_fields: list[str]):
    for col in required_fields:
        missing_mask = df.isna()[col]
        missing_indices = missing_mask[missing_mask].index

        for index in missing_indices:
            add_error(errors, index, f"Missing {col}")

#use regex structure and pandas
def validate_email(df: pd.DataFrame, errors: dict): return

#idk yet
def validate_primary_key(df: pd.DataFrame, errors: dict): return

#if the dates are not in the future
def validate_dates(df: pd.DataFrame, errors: dict): return

#eliminate the rows that appear as keys in error
def create_valid_df(df: pd.DataFrame, errors: dict) -> pd.DataFrame: return

def validate(df: pd.DataFrame, required_fields: list[str]):
    validate_schema(df, required_fields=required_fields)
    errors = {}
    validate_required_values(df, errors, required_fields)
    validate_email(df, errors)
    validate_primary_key(df, errors)
    validate_dates(df, errors)

    valid_df = create_valid_df(df, errors)

    return valid_df, errors