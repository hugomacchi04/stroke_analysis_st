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

# change df values
df.loc[df["work_type"] == "Govt_job", "work_type"] = "Government"
df.loc[df["work_type"] == "children", "work_type"] = "Children"
df.loc[df["work_type"] == "Never_worked", "work_type"] = "Never Worked"

# clean dataframe
df['gender_code'], genders = pd.factorize(df['gender'])
df['married_code'], married = pd.factorize(df['ever_married'])
df['work_code'], works = pd.factorize(df['work_type'])
df['residence_code'], residences = pd.factorize(df['Residence_type'])
df['smoking_code'], smokes = pd.factorize(df['smoking_status'])

columns_to_drop = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
df = df.drop(columns=columns_to_drop)

df = df.dropna()

x = df.drop('stroke', axis=1)  # features
y = df['stroke']  # stroke

# split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# build a Gaussian Naive Bayes Classifier
model = GaussianNB()

# model training
model.fit(x_train, y_train)

# create x_test
with st.form("stroke_form"):
    st.selectbox(
        'What is your gender?',
        genders
    )
    st.selectbox(
        'Have you ever been married?',
        married
    )
    st.selectbox(
        'What is your work type?',
        works
    )
    st.selectbox(
        'Do you live in an urban or rural area?',
        residences
    )
    st.selectbox(
        'Do you smoke?',
        smokes
    )

    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Response successfully submitted")




