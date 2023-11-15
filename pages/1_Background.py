import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
  col4, col5, col6 = st.columns(3)
  with col4:
    st.image('4da0cbeab3bad859bc79b726c136725f-ribbon-stroke-health.png')
with col2:
  st.image('line.png')
    
'## Personal History'
st.write('In late May 2023, my grandfather suffered a hemorrhagic stroke, displaying classic symptoms that, unfortunately, went unrecognized by my family due to our lack of awareness. A month prior, he began experiencing double vision in both eyes, a sign we now know we should have taken more seriously. About a month before he had the stroke, my grandpa started having double vision in both eyes. The doctors noticed blood, but assumed that it would eventually reabsorb back into the brain.')
st.write('Towards the end of May, he developed a severe migraine out of nowhere. My grandparents decided to give it few days to resolve itself, but the turning point was when my grandpa forgot how to dress himself for work and dropped his sandwich unknowingly while walking into the office. After arriving to the ER, he was eventually given surgery to remove some of the blood on one side of his head. For two weeks in the ICU, he seemed in a vegetative state. Though he briefly woke up, doctors were not optimistic, prompting funeral arrangements and a decision to transfer him to hospice.')
st.write('This is where the story takes a turn. While in hospice, he woke up, started talking, swallowed food for the first time and moved his supposedly paralyzed arm and leg. We could not believe it! After a week in hospice, my grandpa started therapy and was back home within a month.')
st.write('Nowdays he is able to walk on his own and his personality remains the same. However, any minor infection triggers symptoms. While grateful for the positive outcome, I cannot help but wonder if early recognition could have prevented this.')
st.write('Witnessing the impact on both my grandpa and grandma, I do not want anyone to go through something like this. Therefore, I hope to create awareness of the symptoms and signs of a stroke with this app!')
  
