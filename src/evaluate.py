"""
Model Evaluation Module

AUTHOR: Shashi Kumar Singh
PROJECT: House Price Prediction
"""

import joblib
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from src.preprocess import preprocess_data
from src.config import MODEL_DIR, METRICS_DIR
from src.models import get_models

def evaluate_model():
    """
    Evaluate all trained models.
    """

    # Load test data
    _, X_test, _, y_test = preprocess_data()

    # Create metrics directory
    METRICS_DIR.mkdir(parents=True, exist_ok=True)

    results = {}

    for model_name in get_models().keys():

        file_name = model_name.lower().replace(" ", "_") + ".pkl"
        model_path = MODEL_DIR / file_name

        # Load model
        model = joblib.load(model_path)

        # Prediction
        y_pred = model.predict(X_test)

        # Metrics
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        results[model_name] = {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "R2": r2,
        }

    # Save metrics
    metrics_file = METRICS_DIR / "metrics.txt"
    model_path = MODEL_DIR / file_name

    with open(metrics_file, "w") as file:

        file.write("MODEL EVALUATION RESULTS\n")
        file.write("=" * 50 + "\n\n")

        for model_name, metric in results.items():

            file.write(f"{model_name}\n")
            file.write("-" * 30 + "\n")
            file.write(f"MAE  : {metric['MAE']:.2f}\n")
            file.write(f"MSE  : {metric['MSE']:.2f}\n")
            file.write(f"RMSE : {metric['RMSE']:.2f}\n")
            file.write(f"R2   : {metric['R2']:.4f}\n\n")

    return results