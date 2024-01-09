import streamlit as st
from joblib import load
import numpy as np
import pandas as pd

# Load the pre-trained Gradient Boosting model
gb_model = load('gradient_boosting_model.joblib')

# Function to scale the income
def scale_income(income):
    return np.log(income + 1)  # Log scaling for income

# Streamlit app structure
def main():
    st.title('Heart Attack Risk Prediction')
    st.sidebar.title('Features')

    # Sidebar - User input features
    sedentary_hours = st.sidebar.slider('Sedentary Hours Per Day', 0, 24, 8, 1)
    bmi = st.sidebar.slider('BMI', 10, 50, 25, 1)
    exercise_hours = st.sidebar.slider('Exercise Hours Per Week', 0, 40, 3, 1)
    income = st.sidebar.slider('Income', 0, 200000, 50000, 500)

    # Scale the income
    scaled_income = scale_income(income)

    # Make predictions using the loaded model
    user_input = np.array([[sedentary_hours, bmi, exercise_hours, scaled_income]])
    prediction = gb_model.predict(user_input)

    # Display prediction result with larger font size
    st.write('Predicted Heart Attack Risk:', f"<span style='font-size:36px'>{prediction[0]}</span>", unsafe_allow_html=True)

    # Display the scaled income value separately
    st.write('Scaled Income:', scaled_income)

if __name__ == '__main__':
    main()
