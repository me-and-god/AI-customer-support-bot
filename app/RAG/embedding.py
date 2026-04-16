from app.db.vector_store import get_collection
from app.utils.helpers import embed_model

model = embed_model()

def embed_texts(chunks,file_name, file_hash, client_id):

    collection = get_collection(client_id)

    for i, chunk in enumerate(chunks):

        collection.add(
            ids = [f"{file_hash}_{i}"],
            documents = [chunk],
            embeddings = [model.encode(chunk)],
            metadatas = [
                {
                    "file_name": file_name,
                    "file_hash": file_hash,
                    "chunk_index": i
                }
            ]
        )



