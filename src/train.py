"""
Model Training Module

AUTHOR: Shashi Kumar Singh
PROJECT: House Price Prediction
"""

import joblib

from src.preprocess import preprocess_data
from src.config import MODEL_DIR
from src.models import get_models


def train_model():
    """
    Train all machine learning models and save them.
    """

    # Load preprocessed data
    X_train, _, y_train, _ = preprocess_data()

    # Create model directory
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    trained_models = {}

    # Get all models
    models = get_models()

    for model_name, model in models.items():

        print(f"Training {model_name}...")

        # Train model
        model.fit(X_train, y_train)

        # Save model
        file_name = model_name.lower().replace(" ", "_") + ".pkl"
        model_path = MODEL_DIR / file_name

        joblib.dump(model, model_path)

        trained_models[model_name] = model

        print(f"✅ {model_name} trained and saved successfully.")

    return trained_models