# 🤖 AI-Powered Skills.md Generator with Intelligent Chatbot

An AI-powered document analysis application that generates structured **Skills.md** files from uploaded documents and provides an intelligent chatbot for both document-based and general AI conversations.

The application is built using **FastAPI**, **LangChain**, **Ollama**, **HTML/CSS/JavaScript**, and **Docker**.

---

## 📌 Features

- 📄 Upload business documents (TXT, PDF, DOCX)
- 🤖 AI-powered Skills.md generation
- 💬 Intelligent chatbot
  - Answers questions about uploaded documents
  - Supports general AI conversations
- 📥 Download generated Skills.md files
- ⚡ FastAPI REST APIs
- 🧠 LangChain + Ollama integration
- 🐳 Docker support
- 🌐 Frontend and backend communication over REST APIs

---

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- FastAPI
- Python

### AI
- LangChain
- Ollama

### Tools
- Git
- GitHub
- Docker
- VS Code

---

## 📂 Project Structure

```
skills-md-generator/
│
├── app/
│   ├── main.py
│   └── config.py
│
├── agents/
│   ├── extraction_agent.py
│   ├── skills_generator.py
│   └── chat_agent.py
│
├── uploads/
│
├── generated/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Workflow

1. Upload a document.
2. Backend extracts the document content.
3. AI generates a structured **Skills.md** file.
4. Download the generated markdown file.
5. Chat with the AI about the uploaded document.
6. Ask general AI questions through the chatbot.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/` | Home |
| POST | `/upload` | Upload document |
| POST | `/generate-skills` | Generate Skills.md |
| POST | `/chat` | AI Chat |
| GET | `/download/{filename}` | Download generated file |
| GET | `/health` | Health check |

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

cd YOUR_REPOSITORY
```

---

### Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Start Ollama

Ensure Ollama is installed and the required model is available.

Example:

```bash
ollama run llama3.2
```

---

### Run Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

### Run Frontend

Open

```
frontend/index.html
```

or use **VS Code Live Server**.

---

## 🐳 Docker

### Build Image

```bash
docker build -t skills-generator .
```

### Run Container

```bash
docker run -p 8000:8000 skills-generator
```

---

### Generate

The AI automatically creates:

```
# Skill Name

## Purpose

## Capabilities

## Required Knowledge

## Workflow

## Inputs

## Outputs
```

---

### Chat Examples

Document-based:

```
Summarize this document.

What are the capabilities?

Explain the workflow.

Who are the stakeholders?
```

General AI:

```
What is FastAPI?

Explain Docker.

What is LangChain?

Write a Python function to reverse a linked list.
```

---

## 🔮 Future Enhancements

- User Authentication
- Database Integration
- Chat History
- Multi-user Support
- Cloud Deployment
- Vector Database (RAG)
- Conversation Memory
- Multiple File Uploads

---

This project is intended for educational and internship purposes.