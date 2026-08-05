""" 
Project configuration file.
AUTHOR: Shashi Kumar Singh
PROJECT: House Price Prediction

"""
 

from pathlib import Path

# PROJECT ROOT DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

#===============================#
# Data paths
#===============================#

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_DATA_PATH = RAW_DATA_DIR / "Housing.csv"

PROCESSED_DATA_PATH = PROCESSED_DATA_DIR / "housing_processed.csv"

#===============================#
# Model paths
#===============================#

MODEL_DIR = BASE_DIR / "models"

MODEL_FILE = MODEL_DIR / "house_price_model.pkl"

#===============================#
# Outputs
#===============================#

OUTPUT_DIR = BASE_DIR / "outputs"

PLOT_DIR = OUTPUT_DIR / "plots"

METRICS_DIR = OUTPUT_DIR / "metrics"