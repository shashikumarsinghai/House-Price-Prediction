"""
Data Preprocessing Module
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from src.config import(
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH
)
from src.utils import load_dataset

def preprocess_data():
    """
    Load, preprocess and split the dataset.
    """

    # Load Dataset
    df = load_dataset(RAW_DATA_PATH)

    # Encode categorical columns
    categorical_columns = df.select_dtypes(include="object").columns

    encoder = LabelEncoder()

    for col in categorical_columns:
        df[col] = encoder.fit_transform(df[col])

    # Save processed dataset
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    # Features and Target
    X = df.drop("price", axis=1)
    y = df["price"]

    # Train-Test-Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test

        