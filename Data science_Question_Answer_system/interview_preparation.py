from openai import OpenAI
import streamlit as st

#read the API Key and setup an OpenAI Client
f= open("keys/open_ai_keys.txt")
key = f.read()
client = OpenAI(api_key=key)
st.title("AI Data Science Interview Question and Answer Assitance")

prompt = st.text_input("📑AI Data Science")

# if the button is clicked generate Response
if st.button("Generate")==True:
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    message=[
        {"role": 'system', "content": "You are a helpful assistant. Given a Data Science topic you always generate interview answer with correct answer in points"},
        {   "role":"user","content":prompt    }
    ]   
    )
   
    st.write(response.choices[0].message.content)

