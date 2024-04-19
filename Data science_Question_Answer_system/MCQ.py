from openai import OpenAI
import streamlit as st

# Load OpenAI client and API key

f= open("keys/open_ai_keys.txt")
key = f.read()
client = OpenAI(api_key=key)
def generate_code_refactor(prompt):
    # Generate code refactor using OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":'''You are a helpful assistant. 
             Given a Data Science topic you always generate 3 MCQ questions and answers for the test."""},.'''
             },
            {"role": "system", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI with CSS styling for text input
st.title('Data Science MCQ Question and Answer Chatpot')
prompt = st.text_area("Enter a code")  # Apply CSS style for height

if st.button("Generate"):
    code_refactor = generate_code_refactor(prompt)
    st.write(code_refactor)
