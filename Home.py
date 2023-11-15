import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
  col4, col5, col6 = st.columns(3)
  with col4:
    st.image('4da0cbeab3bad859bc79b726c136725f-ribbon-stroke-health.png')

'## What is a stroke?'
st.write('Stroke accounts for 5% of annual deaths in the United States, equating to 1 in 20 fatalities.')
st.write('A stroke may happen when there is a blockage in the blood flow to the brain or if there is sudden bleeding within the brain. There are two types of strokes: ischemic strokes and hemorrhagic strokes.')
st.write('Ischemic strokes are the most common kind of strokes. These occur when blood flow to the brain is blocked. Hemorrhagic strokes occur when the brain bleeds; this usually involves a blood vessel bursting, creating pressure in the nearby brain tissue.')

'## What are symptoms of a stroke?'
st.write('•  Sudden numbness or weakness in the face, arm, or leg, especially on one side of the body.')
st.write('•  Sudden confusion, trouble speaking, or difficulty understanding speech.')
st.write('•  Sudden trouble seeing in one or both eyes.')
st.write('•  Sudden trouble walking, dizziness, loss of balance, or lack of coordination.')
st.write('•  Sudden severe headache with no known cause.')

'## Who has a higher probability of having a stroke?'
st.write('There are a slew of factors that contribute to a higher likelihood of having a stroke. Some of these factors can be changed whereas others cannot.')
st.write('Some factors include gender, race, age, high blood pressure, heart disease, smoking, obesity and so on. Men are more likely to have a stroke especially as they get older. There is an even higher risk in African Americans due to high blood pressure.')

'## What are prevention methods?'
st.write('As mentioned in the previous section, some stroke factors can be eliminated with the right lifestyle choices. Here are a few prevention methods:')
st.write('•  Choose healthy foods')
st.write('•  Excersice regularly')
st.write('•  Avoid smoking')

'### Additional Resources'
st.write('CDC Information on Strokes: https://www.cdc.gov/stroke/index.htm')
st.write('American Stroke Association: https://www.stroke.org/en/')

st.markdown("""---""")
'##### References'
st.write('https://www.nhlbi.nih.gov/health/stroke')
st.write('https://www.cdc.gov/stroke/signs_symptoms.htm')
st.write('https://www.hopkinsmedicine.org/health/conditions-and-diseases/stroke')
st.write('https://www.cdc.gov/stroke/prevention.htm')

