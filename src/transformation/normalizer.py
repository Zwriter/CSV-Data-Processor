import pandas as pd
import numpy as np

def normalize_whitespace(df: pd.DataFrame):
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True).str.strip()
    return df

def normalize_email(df: pd.DataFrame):
    if "email" not in df.columns:
        return df
    
    df["email"] = df["email"].str.lower()
    return df

def normalize_date(df: pd.DataFrame, date_column: str | None = None, accepted_formats: list[str] | None = None) -> pd.DataFrame:
    if date_column is None or accepted_formats is None:
        return df
    if date_column not in df.columns:
        return df

    normalized_dates = pd.Series(pd.NaT, index=df.index)
    for date_format in accepted_formats:
        date_series = pd.to_datetime(df[date_column], errors="coerce", format=date_format)
        normalized_dates = normalized_dates.combine_first(date_series)
    
    df[date_column] = normalized_dates
    return df

def normalize_empty_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace('', np.nan)
    return df

def normalize(df: pd.DataFrame, date_column: str | None = None, accepted_formats: list[str] | None = None):
    df = normalize_whitespace(df)
    df = normalize_empty_values(df)
    df = normalize_email(df)
    df = normalize_date(df, date_column=date_column, accepted_formats=accepted_formats)
    return df
