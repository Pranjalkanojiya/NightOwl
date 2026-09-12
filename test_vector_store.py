from extractor import extract
from chunker import chunk_documents
from embeddings import create_embeddings
from vector_store import VectorStore

documents = extract("data/documents/AI.pdf")
chunks = chunk_documents(documents)

embeddings = create_embeddings([chunk["text"] for chunk in chunks])

store = VectorStore()
store.add(chunks, embeddings)

question = "What is binary search?"

question_embedding = create_embeddings([question])[0]

results = store.search(question_embedding, k=5)

print("\nSEARCH RESULTS\n")

for result in results:
    chunk = result["chunk"]

    print("=" * 60)
    print("Source:", chunk["source"])
    print("Page:", chunk["page"])
    print("Distance:", round(result["distance"], 4))
    print("Text:", chunk["text"][:300])