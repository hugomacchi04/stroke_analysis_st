import streamlit as st
import pandas as pd

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

train = df[:80]
test = df[80:]

st.table(test)
