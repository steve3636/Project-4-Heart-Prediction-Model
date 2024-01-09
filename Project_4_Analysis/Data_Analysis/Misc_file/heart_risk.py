import pandas as pd
import streamlit as st
from joblib import load
from PIL import Image
import numpy as np

# Load the trained models
rf_model = load('random_forest_model.joblib')
logistic_model = load('logistic_regression_model.joblib')

# Function to perform prediction using the models
def predict(rf_model, logistic_model, features):
    rf_prediction = rf_model.predict(features)
    logistic_prediction = logistic_model.predict(features)
    return rf_prediction, logistic_prediction

# Streamlit app structure
def main():
    st.title('Heart Attack Risk Prediction')
    st.sidebar.title('Features')

    # Sidebar - User input features
    age = st.sidebar.slider('Age', 18, 100, 40)
    # Add other feature sliders or input components here

    # Create a feature DataFrame
    features = pd.DataFrame({
        'Age': [age],  # Update this with other feature values
        # Add other features similarly
    })

    # Make predictions
    if st.button('Predict'):
        rf_pred, logistic_pred = predict(rf_model, logistic_model, features)

        st.write('Random Forest Prediction:', rf_pred[0])
        st.write('Logistic Regression Prediction:', logistic_pred[0])

if __name__ == '__main__':
    main()
