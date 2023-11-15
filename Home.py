import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
  col4, col5, col6 = st.columns(3)
  with col4:
    st.image('4da0cbeab3bad859bc79b726c136725f-ribbon-stroke-health.png')

'## What is a stroke?'
st.write('Strokes account for 5% of annual deaths in the United States, equating to 1 in 20 fatalities.')
st.write('A stroke may happen when there is a blockage in the blood flow to the brain or if there is sudden bleeding within the brain. There are two types of strokes: ischemic strokes and hemorrhagic strokes.')
st.write('Ischemic strokes are the most common kind of strokes; these occur when blood flow to the brain is blocked. Hemorrhagic strokes occur when the brain bleeds; this usually involves a blood vessel bursting, creating pressure in the nearby brain tissue.')

'## What are symptoms of a stroke?'
st.write('•  Sudden numbness or weakness in the face, arm, or leg, especially on one side of the body.')
st.write('•  Sudden confusion, trouble speaking, or difficulty understanding speech.')
st.write('•  Sudden trouble seeing in one or both eyes.')
st.write('•  Sudden trouble walking, dizziness, loss of balance, or lack of coordination.')
st.write('•  Sudden severe headache with no known cause.')

'## Who has a higher probability of having a stroke?'
st.write('TThere are several factors that contribute to a higher likelihood of having a stroke. Some of these factors can be changed, while others cannot.')
st.write('These factors include gender, race, age, high blood pressure, heart disease, smoking, obesity, and so on. Men, especially as they age, are more likely to have a stroke. There is an even higher risk among African Americans due to high blood pressure.')

'## What are prevention methods?'
st.write('As mentioned in the previous section, some stroke factors can be eliminated with the right lifestyle choices. Here are a few prevention methods:')
st.write('•  Choose healthy foods')
st.write('•  Excersice regularly')
st.write('•  Avoid smoking')

'## Personal History'
st.write('In late May 2023, my grandfather suffered a hemorrhagic stroke, displaying classic symptoms that, unfortunately, went unrecognized by my family due to our lack of awareness. A month prior, he began experiencing double vision in both eyes, a sign we now know we should have taken more seriously. About a month before he had the stroke, my grandpa started having double vision in both eyes. The doctors noticed blood, but assumed that it would eventually reabsorb back into the brain.')
st.write('Towards the end of May, he developed a severe migraine out of nowhere. My grandparents decided to give it few days to resolve itself, but the turning point was when my grandpa forgot how to dress himself for work and dropped his sandwich unknowingly while walking into the office. After arriving to the ER, he was eventually given surgery to remove some of the blood on one side of his head. For two weeks in the ICU, he seemed in a vegetative state. Though he briefly woke up, doctors were not optimistic, prompting funeral arrangements and a decision to transfer him to hospice.')
st.write('This is where the story takes a turn. While in hospice, he woke up, started talking, swallowed food for the first time and moved his supposedly paralyzed arm and leg. We could not believe it! After a week in hospice, my grandpa started therapy and was back home within a month.')
st.write('Nowdays he is able to walk on his own and his personality remains the same. However, any minor infection triggers symptoms. While grateful for the positive outcome, I cannot help but wonder if early recognition could have prevented this.')
st.write('Witnessing the impact on both my grandpa and grandma, I do not want anyone to go through something like this. Therefore, I hope to create awareness of the symptoms and signs of a stroke with this app!')
      


'### Additional Resources'
st.write('CDC Information on Strokes: https://www.cdc.gov/stroke/index.htm')
st.write('American Stroke Association: https://www.stroke.org/en/')

st.markdown("""---""")
'##### References'
st.write('https://www.nhlbi.nih.gov/health/stroke')
st.write('https://www.cdc.gov/stroke/signs_symptoms.htm')
st.write('https://www.hopkinsmedicine.org/health/conditions-and-diseases/stroke')
st.write('https://www.cdc.gov/stroke/prevention.htm')

