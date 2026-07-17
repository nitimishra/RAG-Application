# RAG-Application
# 📄 RAG Chatbot — Retrieval-Augmented Generation Application

A end-to-end **Retrieval-Augmented Generation (RAG)** application that lets you chat with your own documents. It ingests text files, stores them as embeddings in a vector database, retrieves the most relevant chunks for a user's question, and generates a grounded, history-aware answer using an LLM — all wrapped in a simple Streamlit chat interface.

---

## ✨ Features

- **Document Ingestion Pipeline** – Loads `.txt` files, splits them into chunks, and stores them as vector embeddings.
- **Semantic Retrieval** – Uses vector similarity search (cosine distance) to find the most relevant document chunks for a query.
- **Answer Generation** – Generates natural-language answers grounded in retrieved context.
- **History-Aware Conversations** – Reformulates follow-up questions using chat history so the retriever understands context across turns.
- **Streamlit Chat UI** – Clean, interactive web interface to ask questions and view retrieved sources alongside the final answer.
- **Dockerized** – Ready-to-run container setup for easy deployment.

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌───────────────────┐
│   docs/ (.txt)   │ --> │  Ingestion        │ --> │  Chroma Vector DB  │
│  raw documents   │     │  Pipeline         │     │  (embeddings)      │
└─────────────────┘     └──────────────────┘     └───────────────────┘
                                                            │
                                                            ▼
┌─────────────────┐     ┌──────────────────┐     ┌───────────────────┐
│  User Question   │ --> │  Retrieval        │ --> │  Relevant Chunks   │
│  (Streamlit UI)  │     │  Pipeline         │     │                    │
└─────────────────┘     └──────────────────┘     └───────────────────┘
                                                            │
                                                            ▼
                                                  ┌───────────────────┐
                                                  │  History-Aware     │
                                                  │  Answer Generation  │
                                                  │  (LLM)              │
                                                  └───────────────────┘
                                                            │
                                                            ▼
                                                  ┌───────────────────┐
                                                  │  Response shown    │
                                                  │  in Streamlit chat │
                                                  └───────────────────┘
```

---

## 📁 Project Structure

```
RAG-Application/
├── docs/                          # Place your source .txt documents here
├── 1_ingestion_pipeline.py        # Loads, chunks, and embeds documents into ChromaDB
├── 2_retrieval_pipeline.py        # Retrieves relevant chunks for a given query
├── 3_answer_generation.py         # Generates answers using retrieved context
├── 4_history_aware_generation.py  # Adds conversational memory / follow-up handling
├── app.py                         # Streamlit chat application (entry point)
├── Dockerfile                     # Container build configuration
├── .dockerignore
├── .gitignore
├── requirements.txt                # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Orchestration | [LangChain](https://www.langchain.com/) / [LangGraph](https://www.langchain.com/langgraph) |
| Vector Store | [ChromaDB](https://www.trychroma.com/) |
| Embeddings | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` |
| LLM | OpenAI (via `langchain-openai`) |
| Web UI | [Streamlit](https://streamlit.io/) |
| Language | Python 3 |
| Containerization | Docker |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- An OpenAI API key (or your preferred LLM provider key)
- Docker (optional, for containerized deployment)

### 1. Clone the repository

```bash
git clone https://github.com/nitimishra/RAG-Application.git
cd RAG-Application
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Add your documents

Place your `.txt` files inside the `docs/` folder. These are the documents the chatbot will answer questions about.

### 5. Run the ingestion pipeline

This loads your documents, splits them into chunks, generates embeddings, and stores them in a local ChromaDB vector store.

```bash
python 1_ingestion_pipeline.py
```

### 6. Launch the chatbot

```bash
streamlit run app.py
```

Open the URL shown in your terminal (typically `http://localhost:8501`) and start asking questions about your documents.

---

## 🐳 Running with Docker

Build the image:

```bash
docker build -t rag-application .
```

Run the container:

```bash
docker run -p 8501:8501 --env-file .env rag-application
```

Then visit `http://localhost:8501` in your browser.

---

## 🧠 How It Works

1. **Ingestion** (`1_ingestion_pipeline.py`) — Documents are loaded from `docs/`, split into overlapping chunks, converted to embeddings using a HuggingFace sentence-transformer model, and persisted to a local ChromaDB store.
2. **Retrieval** (`2_retrieval_pipeline.py`) — For a given user query, the most semantically similar chunks are retrieved from the vector store using cosine similarity.
3. **Answer Generation** (`3_answer_generation.py`) — The retrieved chunks are passed as context to an LLM, which generates a grounded answer.
4. **History-Aware Generation** (`4_history_aware_generation.py`) — Conversation history is incorporated so follow-up questions are correctly understood in context, not just in isolation.
5. **Streamlit App** (`app.py`) — Ties everything together into an interactive chat interface, displaying both the retrieved source documents and the final answer.

---

## 📌 Roadmap / Ideas for Improvement

- [ ] Support for additional file types (PDF, DOCX, Markdown)
- [ ] Swap in alternative LLM providers (Anthropic, local models, etc.)
- [ ] Add citation highlighting in the UI
- [ ] Add evaluation metrics for retrieval and answer quality
- [ ] Deploy demo on Streamlit Community Cloud / Hugging Face Spaces

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or file an issue.

---

## 📄 License

This project currently has no license specified. Consider adding one (e.g., MIT) if you plan to share or accept contributions.

---

## 👤 Author

**Niti Mishra**
[GitHub](https://github.com/nitimishra)
