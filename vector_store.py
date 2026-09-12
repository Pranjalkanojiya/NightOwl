import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension=384):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def add(self, chunks, embeddings):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.chunks.extend(chunks)

    def search(self, embedding, k=5):
        vector = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(vector, min(k, len(self.chunks)))

        results = []

        for distance, index in zip(distances[0], indices[0]):
            if index != -1:
                results.append({
                    "chunk": self.chunks[index],
                    "distance": float(distance)
                })

        return results