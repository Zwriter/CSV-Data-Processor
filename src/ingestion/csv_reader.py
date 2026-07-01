import os
from pathlib import Path
import pandas as pd

def validate_file_path(path):
    try:
        file_path = Path(path).expanduser().resolve()
    except Exception as e:
        raise ValueError(f"Invalid path format: {e}")
        
    if not file_path.exists():
        raise FileNotFoundError(f"File path does not exist: {file_path}")
    
    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"File is not readable: {file_path}")
    
    return file_path


def reader(file_path):
    path = validate_file_path(file_path)

    try:
        return pd.read_csv(path)
    except pd.errors.ParserError as e:
        raise ValueError(f"Could not parse CSV file: {e}")
    except UnicodeDecodeError as e:
        raise ValueError(f"Could not decode CSV file: {e}")
    