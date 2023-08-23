import os
import streamlit as st
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "sk-" 
st.set_page_config(page_title='OpenAI QA', page_icon=':robot:') 

st.title('OPEN AI Question Answering 🤖')

with st.expander('How to use this app '):
     st.write("""
         - Type your question in the text box below  
         - Click the Get Answer button to get 's response
         - Questions should be factual and answerable by a AI assistant
     """)

llm = OpenAI(model_name="text-davinci-003")  

question = st.text_input('Enter your question:')
if question:
    with st.spinner('Thinking...'):
        answer = llm(question)

    st.success(answer)

st.button('Get Answer', on_click=None, help='Click to get OPENAI-T5\'s answer')