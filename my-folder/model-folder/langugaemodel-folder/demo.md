
# Language Model Folder

This folder contains the implementation of a language model using the `langchain_groq` library.

## File: `llmgroq.py`

### Description

This Python script initializes and invokes a language model using the `ChatGroq` class from the `langchain_groq` library. The model is configured to generate text based on the provided input prompt.

### Setup

1. **Environment Variables**:
   - Ensure you have a `.env` file with the required environment variables.
   - The script uses the `dotenv` library to load environment variables.

2. **API Key**:
   - Place your Groq API key in the `.env` file or directly in the script (use with caution).

### Usage

1. **Initialize the Model**:
   - The model is initialized with specific parameters such as `model_name`, `groq_api_key`, `temperature`, and `max_tokens`.

2. **Invoke the Model**:
   - The `invoke` method is used to generate text based on the input prompt.

3. **Output**:
   - The generated text is printed to the console.

### Example

```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Hardcoded API Key (Use with caution)
groq_api_key = "Your api key "

# Initialize Groq LLM (Chat-based model)
llm = ChatGroq(model_name="mixtral-8x7b-32768", groq_api_key=groq_api_key, temperature=0.3, max_tokens=50)

# Invoke the model
result = llm.invoke("write the 5 line poem on cricket?")

# Print the result
print(result.content)
Dependencies
langchain_groq
dotenv
os
