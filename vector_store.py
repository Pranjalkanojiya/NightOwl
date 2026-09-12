import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension=384):
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add(self, chunks, embeddings):
        vectors = np.asarray(embeddings, dtype="float32")
        faiss.normalize_L2(vectors)

        self.index.add(vectors)
        self.chunks.extend(chunks)

    def search(self, embedding, k=5, threshold=0.40):
        if not self.chunks:
            return []

        vector = np.asarray([embedding], dtype="float32")
        faiss.normalize_L2(vector)

        scores, indices = self.index.search(
            vector,
            min(k, len(self.chunks))
        )

        results = []

        for score, index in zip(scores[0], indices[0]):
            if index == -1:
                continue

            if score >= threshold:
                results.append({
                    "chunk": self.chunks[index],
                    "score": float(score)
                })

        return results