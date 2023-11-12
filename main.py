import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
)

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

# Assuming 'stroke' is the column you want to predict
x = df.iloc[:, :-1]  # Features
y = df.iloc[:, -1] 

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Build a Gaussian Naive Bayes Classifier
model = GaussianNB()

# Model training
model.fit(x_train, y_train)

# Predict Output
y_pred = model.predict(x_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
