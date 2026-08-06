"""
Main Entry Point

AUTHOR: Shashi Kumar Singh
PROJECT: House Price Prediction
"""

from src.train import train_model
from src.evaluate import evaluate_model


def main():

    print("=" * 60)
    print("🏠 House Price Prediction Pipeline")
    print("=" * 60)

    # Train all models
    print("\nTraining Models...\n")
    train_model()

    # Evaluate all models
    print("\nEvaluating Models...\n")
    results = evaluate_model()

    print("=" * 60)
    print("MODEL PERFORMANCE")
    print("=" * 60)

    for model_name, metric in results.items():

        print(f"\n{model_name}")
        print("-" * 30)
        print(f"MAE  : {metric['MAE']:.2f}")
        print(f"MSE  : {metric['MSE']:.2f}")
        print(f"RMSE : {metric['RMSE']:.2f}")
        print(f"R²   : {metric['R2']:.4f}")

    print("\n✅ Pipeline Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()