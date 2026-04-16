import hashlib
import pdfplumber
import io

from app.RAG.embedding import embed_texts
from app.db.vector_store import get_collection
from app.utils.chunker import chunk_text



# this function decides if the user  has input a folder or a single file
def process_input(files,client_id):

    # single file
    if len(files) == 1:
        file = files[0]

        return process_document(file["bytes"], file["name"], client_id)


    #Multiple files (folder)
    else:
        total_chunks=0

        for file in files:
            chunks = process_document(file["bytes"], file["name"], client_id)
            total_chunks+=chunks

        return total_chunks






# this function extracts text from files and embed them in the database
def process_document(file_bytes, file_name, client_id):

    collection = get_collection(client_id)

    file_hash = get_file_hash(file_bytes)

    #check duplicate
    existing = collection.get(
        where={"file_hash":file_hash}
    )

    if existing["ids"]:
        return 0    #already exist


    #extract text
    if file_name.endswith(".pdf"):
        text = extract_pdf(file_bytes)
    else:
        text = file_bytes.decode("utf-8",errors="ignore")

    chunks = chunk_text(text)

    embed_texts(chunks, file_name, file_hash, client_id)

    return len(chunks)






# file hashing
def get_file_hash(file_bytes):
    return hashlib.md5(file_bytes).hexdigest()


#pdf text extract
def extract_pdf(file_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return text
