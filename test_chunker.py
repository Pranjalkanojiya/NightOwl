from extractor import extract
from chunker import chunk_documents

documents = extract("data/documents/AI PROBLEM STATEMENTS 2.pdf")
chunks = chunk_documents(documents)

print(f"Pages: {len(documents)}")
print(f"Chunks: {len(chunks)}")

for chunk in chunks[:5]:
    print("\n" + "=" * 60)
    print(f"Source: {chunk['source']}")
    print(f"Page: {chunk['page']}")
    print(f"Chunk: {chunk['chunk_id']}")
    print(chunk["text"][:300])