from src.config import RAW_DATA_PATH
from src.utils import load_dataset

def main():

    # Load the dataset
    df = load_dataset(RAW_DATA_PATH)

    print("=" * 50)
    print("House Price Prediction Project")
    print("=" * 50)

    # Display the first few rows of the dataset
    print(df.head())

if __name__ == "__main__":
    main()

