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

df.loc[df["smoking_status"] == "formerly smoked", "smoking_status"] = "Formerly Smoked"
df.loc[df["smoking_status"] == "never smoked", "smoking_status"] = "Never Smoked"
df.loc[df["smoking_status"] == "smokes", "smoking_status"] = "Smokes"

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
    '## Stroke Probability Quiz'
    gender = st.selectbox('What is your gender?', genders)
    age = st.number_input('What is your age?', min_value=0)
    married_status = st.selectbox('Have you ever been married?', married)
    work_type = st.selectbox('What is your work type?', works)
    residence_type = st.selectbox('Do you live in an urban or rural area?', residences)
    smoking_status = st.selectbox('Do you smoke?', smokes[:-1])

    
    submitted = st.form_submit_button("Submit")
    if submitted:
        gender_code = genders.get_loc(gender)
        married_code = married.get_loc(married_status)
        work_code = works.get_loc(work_type)
        residence_code = residences.get_loc(residence_type)
        smoking_code = smokes.get_loc(smoking_status)

        user_data = pd.DataFrame([[gender_code, age, married_code, work_code, residence_code, smoking_code]], columns=x)

        prediction = model.predict(user_data)

        st.subheader('Prediction:')
        if prediction[0] == 1:
            st.write('The model predicts that you might have a stroke.')
        else:
            st.write('The model predicts that you might not have a stroke.')


