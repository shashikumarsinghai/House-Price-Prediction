"""
Model Visualization Module

AUTHOR: Shashi Kumar Singh
PROJECT: House Price Prediction
"""

import joblib
import matplotlib.pyplot as plt

from src.config import MODEL_DIR, PLOT_DIR
from src.preprocess import preprocess_data

def plot_actual_vs_predicted():
    """
    Create and save Actual vs Predicted price plot.
    """

    # Load test data
    _, X_test, _, y_test = preprocess_data()

    # Load best performing model
    model_path = MODEL_DIR / "linear_regression.pkl"
    model = joblib.load(model_path)

    # Make prediction
    y_pred = model.predict(X_test)

    # Create plots directory
    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    # Create plot
    plt.figure(figsize=(8, 6))

    plt.scatter(y_test, y_pred)

    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted House Prices")

    # Reference line
    min_price = min(y_test.min(), y_pred.min())
    max_price = max(y_test.max(), y_pred.max())

    plt.plot(
        [min_price, max_price],
        [min_price, max_price],
        linestyle="--"
    )

    plt.tight_layout()

    # Save plot
    plot_path = PLOT_DIR / "actual_vs_predicted.png"
    plt.savefig(plot_path)
    plt.close()

    print(f"✅ Plot saved successfully at:\n{plot_path}")


def plot_residuals():
    """
    Create and save residual plot.
    """

    # Load test data
    _, X_test, _, y_test = preprocess_data()

    # Load model
    model_path = MODEL_DIR / "linear_regression.pkl"
    model = joblib.load(model_path)

    # Predictions
    y_pred = model.predict(X_test)

    # Residuals
    residuals = y_test - y_pred

    # Create plot directory
    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    # Create plot
    plt.figure(figsize=(8, 6))

    plt.scatter(y_pred, residuals)

    plt.axhline(y=0, linestyle="--")

    plt.xlabel("Predicted Price")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")

    plt.tight_layout()

    # Save plot
    plot_path = PLOT_DIR / "residual_plot.png"
    plt.savefig(plot_path)
    plt.close()

    print(f"✅ Residual plot saved successfully at:\n{plot_path}")


def plot_feature_importance():
    """
    Create and save feature importance plots
    for Decision Tree and Random Forest.
    """

    _, X_test, _, _ = preprocess_data()

    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    models = {
        "Decision Tree": "decision_tree.pkl",
        "Random Forest": "random_forest.pkl",
    }

    for model_name, model_file in models.items():

        model_path = MODEL_DIR / model_file
        model = joblib.load(model_path)

        importance = model.feature_importances_

        plt.figure(figsize=(9, 6))

        plt.barh(X_test.columns, importance)

        plt.xlabel("Feature Importance")
        plt.ylabel("Features")
        plt.title(f"{model_name} - Feature Importance")

        plt.tight_layout()
        file_name = model_name.lower().replace(" ", "_")
        plot_path = PLOT_DIR / f"{file_name}_feature_importance.png"

        plt.savefig(plot_path)
        plt.close()

        print(
            f"✅ {model_name} feature importance saved at:\n"
            f"{plot_path}"
        )

if __name__ == "__main__":
    plot_actual_vs_predicted()
    plot_residuals()
    plot_feature_importance()