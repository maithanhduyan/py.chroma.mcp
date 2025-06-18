from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

embed_fn = DefaultEmbeddingFunction()
text = ["Văn bản 1", "Văn bản 2"]
vectors = embed_fn(text)

print(vectors)  # List[List[float]]
