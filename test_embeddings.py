from extractor import extract
from chunker import chunk_documents
from embeddings import create_embeddings

documents = extract("data/documents/AI.pdf")
chunks = chunk_documents(documents)

texts = [chunk["text"] for chunk in chunks]

embeddings = create_embeddings(texts)

print("Chunks:", len(chunks))
print("Embeddings:", len(embeddings))
print("Vector size:", len(embeddings[0]))