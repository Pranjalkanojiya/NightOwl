def chunk_documents(documents, chunk_size=1000, overlap=150):
    chunks = []

    for document in documents:
        text = document["text"].strip()

        if not text:
            continue

        start = 0
        chunk_id = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "source": document["source"],
                    "page": document["page"],
                    "type": document["type"],
                    "chunk_id": chunk_id
                })

                chunk_id += 1

            start += chunk_size - overlap

    return chunks