import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Dictionary for prediction interpretation (example)
dict_pred = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

# Streamlit app
st.title("Iris Flower Prediction App")

st.header("Enter the flower measurements:")

# Input fields for the features
sl = st.number_input("Sepal Length (cm):", min_value=0.0, format="%.2f")
sw = st.number_input("Sepal Width (cm):", min_value=0.0, format="%.2f")
pl = st.number_input("Petal Length (cm):", min_value=0.0, format="%.2f")
pw = st.number_input("Petal Width (cm):", min_value=0.0, format="%.2f")

# Button to make predictions
if st.button("Predict"):
    try:
        # Make prediction
        pred = model.predict([[sl, sw, pl, pw]])
        result = dict_pred[pred[0]]
        
        # Display the result
        st.success(f"The predicted species is: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
