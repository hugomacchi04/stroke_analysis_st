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
df['married_code'], married = pd.factorize(df['ever_married'])
df['work_code'], works = pd.factorize(df['work_type'])
df['residence_code'], residences = pd.factorize(df['Residence_type'])
df['smoking_code'], smokes = pd.factorize(df['smoking_status'])

columns_to_drop = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
df = df.drop(columns=columns_to_drop)

df = df.dropna()

# Assuming 'stroke' is the column you want to predict
x = df.drop('stroke', axis=1)  # Features
y = df['stroke']  # Target variable

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Build a Gaussian Naive Bayes Classifier
model = GaussianNB()

# Model training
model.fit(x_train, y_train)

# User input form
gender = st.selectbox('Gender', df['gender'].unique())
married = st.selectbox('Ever Married', df['ever_married'].unique())
work_type = st.selectbox('Work Type', df['work_type'].unique())
residence_type = st.selectbox('Residence Type', df['Residence_type'].unique())
smoking_status = st.selectbox('Smoking Status', df['smoking_status'].unique())

# Convert user input to match the factorized values
gender_code = genders.get_loc(gender)
married_code = married.get_loc(married)
work_code = works.get_loc(work_type)
residence_code = residences.get_loc(residence_type)
smoking_code = smokes.get_loc(smoking_status)

# Make a prediction
user_data = pd.DataFrame([[gender_code, married_code, work_code, residence_code, smoking_code]], columns=features)
prediction = model.predict(user_data)

# Display the prediction
st.subheader('Prediction:')
if prediction[0] == 1:
    st.write('The model predicts that the user might have a stroke.')
else:
    st.write('The model predicts that the user might not have a stroke.')


