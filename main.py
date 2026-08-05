from src.train import train_model


def main():

    model, X_test, y_test = train_model()

    print("=" * 50)
    print("Model Training Completed")
    print("=" * 50)

    print(model)


if __name__ == "__main__":
    main()