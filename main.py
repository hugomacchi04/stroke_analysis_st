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

df['gender_code'], genders = pd.factorize(df['gender'])

st.write(df)


