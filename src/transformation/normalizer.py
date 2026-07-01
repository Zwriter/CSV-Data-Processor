import pandas as pd

def normalize_whitespaces(df: pd.DataFrame):
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True).str.strip()
    return df

def normalize_emails(df: pd.DataFrame):
    if "email" not in df.columns:
        return df
    
    df["email"] = df["email"].str.lower()
    return df

def normalize_dates(df: pd.DataFrame, date_column: str | None = None, accepted_formats: list[str] | None = None) -> pd.DataFrame:
    if date_column is None or accepted_formats is None:
        return df
    if date_column not in df.columns:
        return df

    date_series = pd.to_datetime(df[date_column], errors="coerce", format=accepted_formats[0])
    for date_format in accepted_formats[1:]:
        date_series = pd.to_datetime(df[date_column], errors="coerce", format=date_format).combine_first(date_series)

    df[date_column] = date_series
    return df

def normalize(df: pd.DataFrame, date_column: str | None = None, accepted_formats: list[str] | None = None):
    df = normalize_whitespaces(df)
    df = normalize_emails(df)
    df = normalize_dates(df, date_column=date_column, accepted_formats=accepted_formats)
    return df
