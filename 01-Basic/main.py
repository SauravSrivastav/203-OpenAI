# Set OpenAI API key 
import os
os.environ["OPENAI_API_KEY"] = "sk-" 

# Import OpenAI class from langchain
from langchain.llms import OpenAI

# Instantiate OpenAI model
llm = OpenAI(model_name="text-davinci-003")  

# Query the model
query = "What is DevSecOps?"
completion = llm(query)

print(completion)

