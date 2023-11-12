import streamlit as st
import pandas as pd
from sklearn.metrics import r2_score

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

train = df[:80]
test = df[80:]

mymodel = numpy.poly1d(numpy.polyfit(train, train, 4))

r2 = r2_score(test, mymodel(test))

st.write(r2)
