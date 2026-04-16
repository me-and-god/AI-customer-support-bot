from app.db.vector_store import get_collection
from app.utils.ai_client import ask_ai
from app.utils.helpers import embed_model

model = embed_model()


def generate_answer(query, client_id):

    collection = get_collection(client_id)

    results = collection.query(
        query_embeddings = [model.encode(query)],
        n_results = 3
    )

    docs = results["documents"][0]
    meta = results["metadatas"][0]

    context = "\n".join(docs)

    prompt = build_prompt(query,context)
    answer = ask_ai(prompt)

    sources = list(set([m["file_name"] for m in meta]))

    return {
        "answer":answer,
        "sources": sources
    }







#-------- BUILD prompt
def build_prompt(query,context):
    prompt = f"""
    Answer ONLY from the context below but a little more explanation.
    If not found, say 'Not found in the given sources'.

    context:
    {context}

    Question:
    {query}
    """
    return prompt

