import streamlit as st
from app.RAG.document_processor import process_document, process_input
from app.RAG.rag_pipeline import generate_answer

st.title("AI Support Agent")

# set page layout
st.set_page_config(page_title="AI CUSTOMER SUPPORT AGENT",layout="wide")


# -------------------------
# CLIENT ID
# -------------------------
client_id = st.text_input("Client ID", value="test_user")

# -------------------------
# FILE UPLOAD
# -------------------------
st.header("Upload Files / Folder")

files = st.file_uploader(
    "Upload PDF, TXT, DOCX",
    accept_multiple_files=True
)

if st.button("Process Files"):
    file_data=[]

    for file in files:
        file_bytes = file.getvalue()

        file_data.append(
            {
                "name":file.name,
                "bytes":file_bytes
            }
        )

    total_chunks = process_input(file_data, client_id)
    st.success(f"Total chunks created: {total_chunks}")
# -------------------------
# CHAT SECTION
# -------------------------
st.header("Ask Questions")

query = st.text_input("Enter your question")

if st.button("Ask"):
    if query:
        result = generate_answer(query, client_id)

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Sources")
        st.write(result["sources"])