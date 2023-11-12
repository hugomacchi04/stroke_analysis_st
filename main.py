import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

train, test = train_test_split(df, test_size=0.2)

st.write(test)
