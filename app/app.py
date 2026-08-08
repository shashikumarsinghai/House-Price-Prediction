"""
House Price Prediction - Streamlit App

AUTHOR: Shashi Kumar Singh
PROJECT: House Price Prediction
"""

import streamlit as st
from src.predict import predict_price

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered",
)

# Title
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict its price.")

# User input
st.subheader("House Details")

area = st.number_input(
    "Area (sq ft)",
    min_value=1,
    value=7420,
    step=100,
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    value=4,
    step=1,
)

bathrooms =st.number_input(
    "Bathrooms",
    min_value=1,
    value=2,
    step=1,
)

stories = st.number_input(
    "Stories",
    min_value=1,
    value=3,
    step=1,
)

# Yes / No inputs
mainroad = st.selectbox(
    "Main Road",
    ["Yes", "NO"],
)

guestroom = st.selectbox(
    "Guest Room",
    ["Yes", "NO"],
)

basement = st.selectbox(
    "Basement",
    ["Yes", "NO"],
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["Yes", "NO"],
)

airconditioning = st.selectbox(
    "Air Conditionong",
    ["Yes", "NO"],
)

# Convert Yes / No to 1 / 0
mainroad_value = 1 if mainroad == "Yes" else 0
guestroom_value = 1 if guestroom == "Yes" else 0
basement_value = 1 if basement == "Yes" else 0
hotwaterheating_value = 1 if hotwaterheating == "Yes" else 0
airconditioning_value = 1 if airconditioning == "Yes" else 0

# Prediction
if st.button("🔮 Predict House Price"):

    # validation
    if area <=0:
        st.error("Area must be greater than 0.")

    elif bedrooms <= 0:
        st.error("Bedrooms must be greater than 0.")

    elif bathrooms <= 0:
        st.error("Bathrooms must be greater than 0.")

    elif stories <= 0:
        st.error("Stories must be greater than 0.")

    else:
        features = [
            area,
            bedrooms,
            bathrooms,
            stories,
            mainroad_value,
            guestroom_value,
            basement_value,
            hotwaterheating_value,
            airconditioning_value,
        ]

    try :
        predicted_price = predict_price(features)

        st.success("Prediction completed successfully!")

        st.metric(
            "Predicted House Price",
            f"₹{predicted_price:,.2f}",
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")