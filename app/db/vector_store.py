import chromadb

client = chromadb.Client(
    settings = chromadb.config.Settings(
        persist_directory="./chroma_db"
    )
)

def get_collection(client_id):
    return client.get_or_create_collection(name=f"client_{client_id}")



