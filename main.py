import streamlit as st
import pandas as pd

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

st.table(df)
