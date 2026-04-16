from sentence_transformers import SentenceTransformer


def embed_model():
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return model


