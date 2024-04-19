from openai import OpenAi
import streamlit as st

# Load OpenAI client and API key
with open("keys/api_key.txt") as f:
    api_key = f.read().strip()

client = OpenAi(key=api_key)

def generate_code_refactor(prompt):
    # Generate code refactor using OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":'''You are a helpful assistant. 
             Given a code, check whether it is correct or not. 
             If not, then generate it in JSON format and recorrect it and display on a new panel.'''
             },
            {"role": "system", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI with CSS styling for text input
st.title('AI code refactor')
prompt = st.text_input("Enter a code", style={'height': '200px'})  # Apply CSS style for height

if st.button("Generate"):
    code_refactor = generate_code_refactor(prompt)
    st.write(code_refactor)
