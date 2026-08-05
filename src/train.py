"""
Model Training Module
"""

import joblib
from sklearn.linear_model import LinearRegression

from src.preprocess import preprocess_data
from src.config import MODEL_DIR, MODEL_FILE

def train_model():

    # Get preprocessed data
    X_train, X_test, y_train, y_test = preprocess_data()

    # Create Model
    model = LinearRegression()

    # Train
    model.fit(X_train, y_train)

    # Create model directory
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    # Save model
    joblib.dump(model, MODEL_FILE)

    return model, X_test, y_test