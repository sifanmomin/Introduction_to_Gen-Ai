from langchain.embeddings import HuggingFaceEmbeddings

# Initialize Hugging Face Embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Text to embed
text = "Delhi is the capital of India"

# Get embeddings
result = embedding.embed_query(text)

# Print the result
print(result)
