"""
Model Prediction Module

AUTHOR: Shashi Kumar Singh
PROJECT: House Price Prediction
"""

import joblib
import pandas as pd

from src.config import MODEL_DIR

# Default model
MODEL_PATH = MODEL_DIR / "linear_regression.pkl"

# Feature order used during training
FEATURE_NAMES = [
    "area",
    "bedrooms",
    "bathrooms",
    "stories",
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
]

def load_model():
    """
    Load the trained machine learning model.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found: {MODEL_PATH}\n"
            "Please train the model first."
        )

    return joblib.load(MODEL_PATH)

def predict_price(features):
    """
    Predict house price.

    Parameters
    ----------
    features : list or array-like
        Input features in the following order:
        area, bedrooms, bathrooms, stories,
        mainroad, guestroom, basement,
        hotwaterheating, airconditioning


    Returns
    -------
    float
        Predicted house price.
    """

    if len(features) != len(FEATURE_NAMES):
        raise ValueError(
            f"Expected {len(FEATURE_NAMES)} features, "
            f"but received {len(features)}."
        )

    model = load_model()

    # Create DataFrame with the same feature names
    input_data = pd.DataFrame(
        [features],
        columns=FEATURE_NAMES
    )

    prediction = model.predict(input_data)

    return float(prediction[0])