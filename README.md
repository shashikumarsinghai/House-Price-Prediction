# 🏠 House Price Prediction

A complete Machine Learning project that predicts house prices based on property features using multiple regression models and a Streamlit web application.

---

## 📌 About the Project

This project demonstrates an end-to-end Machine Learning workflow for house price prediction.

The project covers:

- Data loading
- Data preprocessing
- Categorical feature encoding
- Train-test splitting
- Multiple machine learning models
- Model evaluation
- Data visualization
- House price prediction
- Streamlit web application

The trained models are saved and can be used for making predictions through the prediction module and web application.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Prepare and preprocess the housing dataset.
2. Train multiple regression models.
3. Compare model performance using evaluation metrics.
4. Visualize model predictions and feature importance.
5. Build a reusable prediction module.
6. Create an interactive Streamlit application.

---

## 📊 Dataset

The project uses a housing dataset containing **545 records and 10 columns**.

### Features

| Feature | Description |
|---|---|
| `area` | Area of the house in square feet |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `stories` | Number of stories |
| `mainroad` | Whether the house is connected to the main road |
| `guestroom` | Whether the house has a guest room |
| `basement` | Whether the house has a basement |
| `hotwaterheating` | Whether hot water heating is available |
| `airconditioning` | Whether air conditioning is available |

### Target

`price` — House price.

---

## 🤖 Machine Learning Models

Three regression models are trained and evaluated:

### 1. Linear Regression

A simple and interpretable regression model used as the primary baseline model.

### 2. Decision Tree Regressor

A tree-based model that learns decision rules from the training data.

### 3. Random Forest Regressor

An ensemble model that combines multiple decision trees to improve generalization.

---

## 📈 Model Performance

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 1,029,305.71 | 1,413,204.62 | **0.6049** |
| Decision Tree | 1,282,696.27 | 1,832,966.88 | 0.3353 |
| Random Forest | 1,104,205.66 | 1,496,229.40 | 0.5571 |

Based on the current evaluation results, **Linear Regression achieved the highest R² score** among the tested models.

> Note: Model performance can vary depending on the dataset, preprocessing, and training configuration.

---

## 📊 Visualizations

The project generates the following visualizations:

### Actual vs Predicted

Compares the actual house prices with the prices predicted by the model.

### Residual Plot

Shows the difference between actual and predicted prices.

### Decision Tree Feature Importance

Shows the relative importance of features used by the Decision Tree model.

### Random Forest Feature Importance

Shows the relative importance of features used by the Random Forest model.

Generated plots are stored in:

```text
outputs/plots/
```

---

## 📁 Project Structure

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
│   ├── linear_regression.pkl
│   ├── decision_tree.pkl
│   └── random_forest.pkl
│
├── notebooks/
│
├── outputs/
│   ├── metrics/
│   └── plots/
│
├── src/
│   ├── __init__.py
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
```

---

## ⚙️ Technologies Used

- **Python**
- **Pandas** — Data processing
- **NumPy** — Numerical operations
- **Scikit-learn** — Machine Learning
- **Matplotlib** — Data visualization
- **Joblib** — Model saving and loading
- **Streamlit** — Web application

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the project directory

```bash
cd House-Price-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Machine Learning Pipeline

Run the complete training and evaluation pipeline:

```bash
python main.py
```

This will:

1. Load the dataset.
2. Preprocess the data.
3. Train the models.
4. Save the trained models.
5. Evaluate the models.
6. Display the evaluation metrics.

---

## 📊 Generate Visualizations

Run:

```bash
python -m src.visualize
```

The generated plots will be saved inside:

```text
outputs/plots/
```

---

## 🔮 Make a Prediction Using Python

The prediction module can be tested with:

```bash
python -c "from src.predict import predict_price; print(predict_price([7420, 4, 2, 3, 1, 0, 0, 0, 1]))"
```

The input features must be provided in this order:

```text
area
bedrooms
bathrooms
stories
mainroad
guestroom
basement
hotwaterheating
airconditioning
```

For categorical features:

```text
1 = Yes
0 = No
```

---

## 🌐 Run the Streamlit Web Application

Start the application using:

```bash
python -m streamlit run app/app.py
```

The application provides an interactive interface where users can enter house details and receive a predicted house price.

### Application Features

- 🏠 House details input
- ✅ Input validation
- 🔮 Price prediction
- 💰 Predicted price display
- 🖥️ Interactive Streamlit interface

---

## 🔄 Machine Learning Workflow

```text
Housing Dataset
       ↓
Data Loading
       ↓
Data Preprocessing
       ↓
Categorical Encoding
       ↓
Train / Test Split
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Visualization
       ↓
Prediction
       ↓
Streamlit Web Application
```

---

## 📌 Future Improvements

Possible improvements for future versions include:

- Hyperparameter tuning
- Cross-validation
- Feature engineering
- Trying additional regression algorithms
- Improving model accuracy
- Adding more visualizations
- Deploying the Streamlit application online
- Adding automated testing

---

## 👨‍💻 Author

**Shashi Kumar Singh**

Engineering / AI & ML Student

---

## ⭐ Project Status

**Current Status: Completed Core ML Pipeline + Streamlit Application**

The project currently includes data preprocessing, multiple machine learning models, evaluation, visualization, prediction functionality, and an interactive Streamlit application.