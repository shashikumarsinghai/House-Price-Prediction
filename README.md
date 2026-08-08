\# 🏠 House Price Prediction

A Machine Learning project that predicts house prices based on different property features.


\## 📌 Project Overview


This project implements a complete Machine Learning pipeline for house price prediction.

The project includes:


\- Data preprocessing

\- Multiple Machine Learning models

\- Model evaluation

\- Data visualization

\- House price prediction

\- Streamlit web application


\## 🤖 Machine Learning Models


The following models are trained and evaluated:

1\. Linear Regression

2\. Decision Tree Regressor

3\. Random Forest Regressor


Based on the evaluation results, \*\*Linear Regression\*\* currently provides the best performance among the tested models.


\## 📊 Model Performance


| Model | MAE | RMSE | R² Score |

|---|---:|---:|---:|

| Linear Regression | 1,029,305.71 | 1,413,204.62 | 0.6049 |

| Decision Tree | 1,282,696.27 | 1,832,966.88 | 0.3353 |

| Random Forest | 1,104,205.66 | 1,496,229.40 | 0.5571 |



\## 📁 Project Structure



```text

House-Price-Prediction/

│

├── app/

│   └── app.py

│

├── data/

│   ├── raw/

│   │   └── Housing.csv

│   └── processed/

│

├── models/

│   ├── linear\_regression.pkl

│   ├── decision\_tree.pkl

│   └── random\_forest.pkl

│

├── notebooks/

│

├── outputs/

│   ├── metrics/

│   └── plots/

│

├── src/

│   ├── \_\_init\_\_.py

│   ├── config.py

│   ├── evaluate.py

│   ├── model.py

│   ├── predict.py

│   ├── preprocess.py

│   ├── train.py

│   ├── utils.py

│   └── visualize.py

│

├── .gitignore

├── LICENSE

├── main.py

├── README.md

└── requirements.txt



\# Dataset Features

The model uses the following features:

Area

Bedrooms

Bathrooms

Stories

Main Road

Guest Room

Basement

Hot Water Heating

Air Conditioning



The target variable is:

Price

⚙️ Installation

Clone the repository and open the project folder.



Create a virtual environment: python -m venv .venv

Activate the environment on Windows: .venv\\Scripts\\Activate.ps1

Install the required dependencies: pip install -r requirements.txt

🚀 Run the Machine Learning Pipeline

From the project root: python main.py


This runs the training and evaluation pipeline.


📈 Generate Visualizations

Run: python -m src.visualize

The generated plots are saved inside: outputs/plots/

Generated visualizations include: Actual vs Predicted

Residual Plot

Decision Tree Feature Importance

Random Forest Feature Importance

🔮 Make a Prediction

The prediction module can be tested using:
python -c "from src.predict import predict\_price; print(predict\_price(\[7420, 4, 2, 3, 1, 0, 0, 0, 1]))"

🌐 Run the Streamlit App

Start the web application: python -m streamlit run app/app.py

The application allows users to enter house details and get a predicted house price.

\# 🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Joblib

Streamlit

👨‍💻 Author

Shashi Kumar Singh



📄 License

This project is for educational and learning purposes.

