import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# read in data
df = pd.read_csv('healthcare-dataset-stroke-data.csv')

df = df.drop('id', axis=1)
             
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

# build a Logistic Regression Classifier
model = LogisticRegression(random_state=42)

# train the model
model.fit(x_train, y_train)

# create test
with st.form("stroke_form"):
    st.markdown('<p style="color:Blue; font-size: 20px;">Stroke Prediction Quiz</p>', unsafe_allow_html=True)
    gender = st.selectbox('What is your gender?', genders)
    age = st.number_input('What is your age?', min_value=0)
    has_hypertension = st.selectbox('Do you have hypertension?', ('Yes', 'No'))
    has_heart_disease = st.selectbox('Do you have heart disease?', ('Yes', 'No'))
    married_status = st.selectbox('Have you ever been married?', married)
    work_type = st.selectbox('What is your work type?', works)
    residence_type = st.selectbox('Do you live in an urban or rural area?', residences)
    average_glucose = st.number_input('What is your average glucose level?', min_value=0)
    bmi = st.number_input('What is your BMI?', min_value=0)
    smoking_status = st.selectbox('Do you smoke?', smokes[:-1])
    
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        gender_code = genders.get_loc(gender)
        married_code = married.get_loc(married_status)
        work_code = works.get_loc(work_type)
        residence_code = residences.get_loc(residence_type)
        smoking_code = smokes.get_loc(smoking_status)

        if has_hypertension == "Yes":
            hypertension = 1
        else:
            hypertension = 0

        if has_heart_disease == "Yes":
            heart_disease = 1
        else:
            heart_disease = 0

        user_data = pd.DataFrame([[gender_code, age, hypertension, heart_disease, married_code, work_code, residence_code, average_glucose, bmi, smoking_code]], columns=x.columns)

        prediction = model.predict(user_data)

        '### Prediction:'
        if prediction[0] == 1:
            st.write('You have a high probability of having a stroke.')
        else:
            st.write('You have a low probability of having a stroke.')

col1, col2, col3 = st.columns(3)

with col2:
  col4, col5, col6 = st.columns(3)
  with col5:
    st.image('4da0cbeab3bad859bc79b726c136725f-ribbon-stroke-health.png')


