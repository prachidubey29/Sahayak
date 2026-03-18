# 🤖 Agentic Enterprise Assistant

A reliability-first AI assistant that combines **Retrieval-Augmented Generation (RAG)** with lightweight **agentic routing** and **Redis-based memory persistence** to answer enterprise document queries with page-level citations and generate structured JSON outputs for workflow automation.

---

## 🚀 Key Features

* 📄 Citation-grounded document question answering
* 🛡️ Hallucination guardrails for safe responses
* 🔀 Intent-based routing (Information vs Action mode)
* 🧾 Deterministic JSON outputs for enterprise workflows
* 🧠 **Memory persistence using Redis for context-aware conversations**
* ⚡ Fast and scalable architecture
* 🎯 Simple Streamlit-based UI

---

## 🧠 Memory Architecture (Redis)

To enable **context-aware and stateful interactions**, the system integrates **Redis as an in-memory session store**.

### 🔧 How it works

* Each user session is assigned a **unique key**
* Conversation history and relevant context are stored in **Redis**
* On every query:

  * Previous interactions are retrieved from Redis
  * Combined with the current query before processing
* Updated context is written back to Redis

### 📈 Benefits

* ⚡ Low-latency memory retrieval
* 🔄 Persistent conversational context
* 📊 Scalable for multiple concurrent users
* 🧩 Clean separation of memory and AI logic

---

## 🛠️ Tech Stack

* **IDE**: GitHub Codespaces
* **UI**: Streamlit
* **PDF Parsing**: PyPDF
* **Chunking**: LangChain Text Splitters
* **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
* **Vector Database**: ChromaDB
* **LLM**: Hugging Face Inference API (**Qwen/Qwen2.5-7B-Instruct**)
* **Memory Store**: Redis
* **Agent Logic**: Custom Python routing

---

## 📂 Project Structure

```
agentic-enterprise-assistant/
├── app.py                 # Streamlit UI
├── requirements.txt       # Dependencies
├── data/                  # PDF documents
├── ingestion/             # PDF loading and chunking
├── rag/                   # Vector store and RAG pipeline
├── agent/                 # Intent router and controller
├── actions/               # Action prompts and handlers
├── memory/                # Redis integration (session storage)
└── README.md              # Project summary
```

---

## ⚙️ Setup

### 1️⃣ Open in Codespaces

Open the repository in **GitHub Codespaces**

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add secrets

```bash
HF_TOKEN=<your_huggingface_token>
REDIS_URL=<your_redis_connection_string>
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🏗️ System Architecture

```
┌─────────────────────────────┐
│        Streamlit UI         │
│   (User Query Interface)    │
└──────────────┬──────────────┘
               │ User Input
               ▼
┌─────────────────────────────┐
│      Intent Router          │
│ (Info Query / Action Mode)  │
└───────┬───────────┬─────────┘
        │           │
        │           │
        ▼           ▼
┌──────────────┐   ┌────────────────┐
│   RAG Mode   │   │  Action Mode   │
│ (Doc Search │   │ (JSON Generator│
│  + Citation)│   │  via LLM)       │
└──────┬───────┘   └────────┬───────┘
       │                    │
       ▼                    ▼
┌──────────────────┐   ┌──────────────────┐
│  ChromaDB Vector │   │ HuggingFace LLM  │
│  Store (Embeds)  │   │ (Qwen2.5-7B)     │
└──────┬───────────┘   └────────┬─────────┘
       │ Retrieved Chunks        │ JSON Output
       ▼                         ▼
┌─────────────────────────────┐
│ Citation Answer OR Action   │
│ JSON + Context from Redis   │
└─────────────────────────────┘
```

---

## 🔄 How It Works

1. User enters a query in the Streamlit interface
2. **Intent router** classifies query:

   * Informational → RAG pipeline
   * Action → JSON action generator
3. Redis retrieves **previous session context**
4. RAG retrieves relevant chunks from ChromaDB
5. LLM generates:

   * Citation-grounded answer OR
   * Structured JSON action
6. Updated context is stored back in Redis

---

## 💡 Demo Queries

### 📄 Document Queries

* What are the key risks mentioned in the report?
* What initiatives are mentioned for digital transformation?

### ⚙️ Action Commands

* Schedule a meeting with HR tomorrow at 3 PM
* Create an IT ticket for laptop not turning on, high priority

### 🛡️ Hallucination Guardrail

* Who is the CEO of Google?

---

## 📤 Output Examples

### Citation-Grounded Answer

```
"The report identifies key risks including global economic uncertainty and market volatility, discussed on Pages 45 and 46."
```

### Action JSON

```json
{
  "action": "create_it_ticket",
  "issue": "Laptop not turning on",
  "priority": "High"
}
```

---

## 📈 Future Improvements

* ⏳ TTL-based memory expiration in Redis
* 🧠 Long-term vs short-term memory separation
* 🔍 Vector-based semantic memory retrieval
* 📊 Monitoring & analytics dashboard

---

## 🧾 Conclusion

The Agentic Enterprise Assistant demonstrates an **enterprise-ready AI system** combining:

* Reliable RAG pipelines
* Deterministic agentic workflows
* Scalable Redis-based memory

to deliver **accurate, transparent, and context-aware AI interactions**.

---
