import os
import streamlit as st
from langchain.llms import HuggingFaceHub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

st.set_page_config(page_title='Flan-T5 QA', page_icon=':robot:') 

st.title('Flan-T5 Question Answering 🤖')

with st.expander('How to use this app '):
     st.write("""
         - Type your question in the text box below  
         - Click the Get Answer button to get Flan-T5's response
         - Questions should be factual and answerable by a AI assistant
     """)

llm = HuggingFaceHub(repo_id="google/flan-t5-large")

question = st.text_input('Enter your question:')
if question:
    with st.spinner('Thinking...'):
        answer = llm(question)

    st.success(answer)

st.button('Get Answer', on_click=None, help='Click to get Flan-T5\'s answer')