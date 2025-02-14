# Embedding Model Folder

This folder contains scripts for implementing and testing embedding models using the `langchain` library.

## Files

### documentsimilarity.py
- **Description**: This script demonstrates how to use Hugging Face embeddings to find the most similar document to a given query.
- **Key Functions**:
  - Initializes the `HuggingFaceEmbeddings` model with the `sentence-transformers/all-MiniLM-L6-v2` model.
  - Embeds a list of documents and a query.
  - Computes cosine similarity between the query embedding and document embeddings.
  - Finds and prints the most similar document to the query along with the similarity score.

### hf.py
- **Description**: This script demonstrates how to use Hugging Face embeddings to embed a single text input.
- **Key Functions**:
  - Initializes the `HuggingFaceEmbeddings` model with the `sentence-transformers/all-MiniLM-L6-v2` model.
  - Embeds a single text input.
  - Prints the resulting embedding.

### readme.md
- **Description**: Placeholder README file for the `Embedding_model-folder`.

## Usage

Each script can be run independently. Ensure you have the necessary dependencies installed before running the scripts. Follow the documentation within each script for specific instructions on how to use them.

## Dependencies

- `langchain`
- `scikit-learn`

Ensure you have the required dependencies installed by running:
```bash
pip install langchain scikit-learn
