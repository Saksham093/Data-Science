import streamlit as st
import numpy as np
import pandas as pd
# from PIL import Image
import os
from keras.models import load_model

# Load data
data = pd.read_csv("C:/Users/M.SAKSHAM/Desktop/Py/Machine Learning/ML Project/Food Delivery Time Prediction/code/data.txt")

# Load Image
# image = Image.open('C:/Users/M.SAKSHAM/Desktop/Py/Machine Learning/ML Project/Food Delivery Time Prediction/code/image.jpg')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("C:/Users/M.SAKSHAM/Desktop/Py/Machine Learning/ML Project/Food Delivery Time Prediction/code/style/style.css")

model = load_model("C:/Users/M.SAKSHAM/Desktop/Py/Machine Learning/ML Project/Food Delivery Time Prediction/code/model.h5")

# _, col2, _ = st.columns([1, 2, 1])

st.title("Delivery Time Prediction")
# with col2:
#     st.image(image, width=350)

st.markdown("### This app uses a predictive model to estimate the delivery time for your food order.")
st.write("Please input the following information to predict the delivery time:")

# Use widgets to get user input
age = st.sidebar.slider("Age of Delivery Person", 18, 45, 24)
ratings = st.sidebar.slider("Ratings of Delivery Person", 1, 5, 3)
distance = st.sidebar.slider("Distance (in Km)", 1, 30, 5)
# Create a predict button
if st.button("Predict"):
    delivery_info = np.array([[age, ratings, distance]])
    predicted_time = model.predict(delivery_info)
    st.write("The predicted delivery time is: ", predicted_time[0][0], " minutes")

# st.write("Dataset used: ")
# st.dataframe(data.head())

# Add a disclaimer
st.write("Note: The model is trained on the given dataset and may not be accurate for all scenarios.")
