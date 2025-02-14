from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Hardcoded API Key (Use with caution)
groq_api_key = "Your api key "

# Initialize Groq LLM (Chat-based model)
llm = ChatGroq(model_name="mixtral-8x7b-32768", groq_api_key=groq_api_key,temperature= 0.3,max_tokens=50)

# Invoke the model
result = llm.invoke("write the 5 line poem on cricket?")

# Print the result
print(result.content)
