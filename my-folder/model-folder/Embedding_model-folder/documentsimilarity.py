from langchain.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Hugging Face Embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Documents to embed
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# Get embeddings for documents and query
doc_embeddings = embedding.embed_documents(documents)
query = "Tell me about Virat Kohli"
query_embedding = embedding.embed_query(query)

# Compute cosine similarity
similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find the most similar document
best_match_index = similarities.argmax()
best_match_score = similarities[best_match_index]

# Print results
print("Query:", query)
print("Best Matching Document:", documents[best_match_index])
print("Similarity Score:", best_match_score)
