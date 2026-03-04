# 🤖 Customer Support RAG Assistant

An AI-powered **Customer Support Assistant** built using **Retrieval-Augmented Generation (RAG)**.
The system retrieves relevant information from a knowledge base and uses **OpenAI models** to generate accurate and contextual responses.

This project demonstrates how to build a **smart support chatbot** that can answer questions using company documentation or FAQs.

---

# 🚀 Features

* 🔎 **Retrieval-Augmented Generation (RAG)**
* 📚 Document search using **FAISS vector database**
* 🤖 AI responses powered by **OpenAI**
* ⚡ Fast semantic search
* 🔒 Secure API key management using `.env`
* 🧠 Context-aware answers from stored documents

---

# 🛠 Tech Stack

* **Python**
* **FAISS** (vector similarity search)
* **OpenAI API**
* **LangChain** *(optional depending on your code)*
* **dotenv** for environment variables

---

# 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/amineaitalioffpro-rgb/CUSTUMOR-SUPPORT.git
cd CUSTUMOR-SUPPORT
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

⚠️ **Never commit your ****`.env`**** file to GitHub.**

---

# ▶️ Run the Project

```bash
python cust_supp.py
```

The assistant will retrieve relevant documents from the vector database and generate responses using the OpenAI API.

---

# 📁 Project Structure

```
CUSTUMOR-SUPPORT/
│
├── cust_supp.py
├── requirements.txt
├── .gitignore
├── .env.example
│
├── vector_db/
│   ├── index.faiss
│   └── index.pkl
│
└── README.md
```

 

## 🧠 RAG Pipeline

The system answers customer questions using a **Retrieval-Augmented Generation (RAG)** pipeline.

```
Customer Question
      ↓
Embedding Model
      ↓
Vector Search (FAISS)
      ↓
Retrieve Relevant Documents
      ↓
LLM Generates Answer

```

### How it works

1. A **customer asks a question**.
2. The system converts the question into an **embedding vector**.
3. The vector is used to perform a **semantic search in the FAISS vector database**.
4. The most **relevant documents are retrieved**.
5. These documents are provided as **context to the LLM**.
6. The **LLM generates the final answer** based on the retrieved information.

  

---

# 🔮 Future Improvements

* 🌐 Web interface (Streamlit / Gradio)
* 💬 Chat history and memory
* 📄 Multi-document ingestion
* 📊 Analytics for customer questions
* 🧠 Better retrieval optimization

---

# 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

# 📄 License

MIT License
