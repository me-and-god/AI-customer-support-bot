# 🤖 AI Support Agent (RAG-based)

An AI-powered document assistant that allows users to upload files (PDF, TXT, DOCX) and ask questions based on their content. The system uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers with source references.

---

##  Features

* 📂 Upload single or multiple files (folder support)
* 📄 Supports PDF, TXT, DOCX
* 🧠 Context-aware Q&A using RAG pipeline
* 🔍 Returns answers with **source references**
* ♻️ Duplicate file detection (no reprocessing)
* 👥 Multi-client support (data isolation per user)
* ⚡ Built with Streamlit for fast interaction

---

##  Tech Stack

* **Frontend + Backend:** Streamlit
* **Vector DB:** ChromaDB
* **Document Parsing:** pdfplumber, python-docx

---

##  Project Structure

```
ai-support-agent/

streamlit_app.py              # Streamlit UI

app/
rag_pipeline.py              # Retrieval + LLM logic
embed.py                     # Embedding + storage
chunker.py                     # Text chunking
process.py                   # File processing

db/
vector_store.py               # Vector DB setup

.env
requirements.txt
```

---

##  Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ai-support-agent.git
cd ai-support-agent
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

##  Run the App

```bash
streamlit run app.py
```

---

## 🧪 How to Use

1. Enter a `client_id` (any unique name)
2. Upload files or a folder
3. Click **Process Files**
4. Ask questions based on uploaded documents
5. View:

   * ✅ Answer
   * 📄 Source references

---

##  How It Works (RAG Flow)

```
Upload Files
   ↓
Extract Text (PDF/TXT/DOCX)
   ↓
Chunk Text
   ↓
Generate Embeddings
   ↓
Store in Vector DB (Chroma)
   ↓
User Query
   ↓
Retrieve Relevant Chunks
   ↓
LLM Generates Answer
   ↓
Return Answer + Sources
```

---

## 🛡️ Key Design Decisions

* **Metadata storage** → enables source tracking
* **File hashing** → prevents duplicate processing
* **Client-based collections** → avoids data mixing
* **Chunk overlap** → improves context accuracy

---

## ⚠️ Limitations

* Not optimized for very large documents
* No authentication (client_id is manual)
* Streamlit is not ideal for large-scale production

---

##  Future Improvements

* 🔐 Authentication & user management
* 💬 Chat history (conversation memory)
* 📊 Better UI (ChatGPT-style interface)
* ☁️ Cloud storage for documents
* ⚡ Faster retrieval (hybrid search)

---

## ⭐ If you found this useful

Give the repo a star ⭐ and feel free to contribute!
