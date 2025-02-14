from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Hardcoded API Key (Use with caution)
groq_api_key = "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"

# Initialize Groq LLM (Chat-based model)
llm = ChatGroq(model_name="mixtral-8x7b-32768", groq_api_key=groq_api_key)

# Invoke the model
result = llm.invoke("What is the capital of france?")

# Print the result
print(result.content)
