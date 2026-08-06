"""
Model Prediction Module

AUTHOR: Shashi Kumar Singh
PROJECT: House Price Prediction
"""

import joblib
from src.config import MODEL_DIR

# Default model
MODEL_PATH = MODEL_DIR / "linear_regression.pkl"

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

        [
            area,
            bedrooms,
            bathrooms,
            stories,
            mainroad,
            guestroom,
            basement,
            hotwaterheating,
            airconditioning
        ]

    Returns
    -------
    float
        Predicted house price.
    """

    model = load_model()

    prediction = model.predict([features])

    return prediction[0]