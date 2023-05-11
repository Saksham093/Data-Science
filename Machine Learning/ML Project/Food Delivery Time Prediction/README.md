# **Food Delivery Time Prediction**

## **Introduction**

This app is a simple web application that predicts the delivery time for food delivery based on various factors such as `age`, `rating`, and `delivery distance` of the delivery person.

## **Installation**

To run this app, you will need to have the following packages installed:

```cli
- streamlit
- numpy
- pandas
- sklearn
- keras
```

## **Demo**

<img src="code/style/Time%20Prediction.jpg"  width="600">

## **Usage**

Use the sliders to input the age, ratings, and distance of delivery and press the "Predict" button to get the predicted delivery time.

## **Data**

The data used to train the model is a simple dataset consisting of the `age`, `ratings`, `distance`, and `delivery time` of multiple delivery persons. The data is loaded from a `.txt` file.

## **Model**

The model used in this app is a simple **LSTM Neural Network** created using Keras. The model is trained on the data and used for prediction, based on input data.

## **Limitations**

Please note that the predictions made by this app are based on a simple dataset and may not be entirely accurate. The app and the model are intended for demonstration purposes only.

## **Contributing**

Contributions are welcome! If you find any issues with the script or have suggestions for improvements, please open an issue or submit a pull request.

## **License**

This project is not under any license. Open for all.
