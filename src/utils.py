"""
Utility Functions
"""

import pandas as pd

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load dataset from a CSV file.

    Parameters:
    ___________
    file_path : str
        Path to the CSV file.

    Returns:
    ________
    DataFrame
    """

    return pd.read_csv(file_path)