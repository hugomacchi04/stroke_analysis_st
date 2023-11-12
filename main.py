import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import (
  GaussianNB,
  accuracy_score,
  confusion_matrix,
  ConfusionMatrixDisplay,
  f1_score,
)

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

train, test = train_test_split(df, test_size=0.2)

# Build a Gaussian Classifier
model = GaussianNB()

# Model training
model.fit(train, train)

# Predict Output
predicted = model.predict(test)
accuracy = accuracy_score(predicted, test)
f1 = f1_score(predicted, test, average="weighted")

st.write(accuracy)
