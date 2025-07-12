import streamlit as st
from mistralai import Mistral

model = "mistral-small-latest"

client = Mistral(api_key="HvZSvpKxX6eUBWOhYAHWaBJRkQUPJufa")

st.title("AI career advisor")

name =  st.text_input('Name')
age = st.text_input('Age')
job = st.text_input('Job & Designation')
yoe = st.text_input('Years of Experience')
skills = st.text_input('Skill Set')
short = st.text_input('Short term goal')
long = st.text_input('Long term goal')
interest = st.text_input('Future Career interest')
quali = st.text_input('Qualifications')

prompt = f"""Please give the person, future career advice based on the following inputs :
name : {name},
Age : {age},
Job & Designation : {job},
Years of Experience: {yoe},
Skill Set : {skills},
Short term goal: {short},
Long term goal: {long},
Future Career interest : {interest} ,
Qualifications : {quali}

Make it structured well. list down all the things he/she should learn for surviving in
the upcoming world.
"""

if st.button('Submit'):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )

    st.write(chat_response.choices[0].message.content)
