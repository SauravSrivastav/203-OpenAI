# Set Hugging Face API token
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Import HuggingFaceHub class
from langchain.llms import HuggingFaceHub

# Instantiate model from Hugging Face Hub
llm = HuggingFaceHub(repo_id="google/flan-t5-large")  

# Query the model
query = "What is DevOps?"  
completion = llm(query)

print(completion)