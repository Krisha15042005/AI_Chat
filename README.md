# AI Chat Assistant

This project is a backend implementation of a microservice-based AI assistant that handles chat queries using Cohere, Knowledge Base, Web Search, and MongoDB session storage.

#### Project Structure

ai_agent_chatgpt_final_fixed/
├── app.py
├── cohere_handler.py
├── knowledge_base.py
├── search_fallback.py
├── database.py
├── routes/
│   ├── chat.py
│   ├── history.py
│   ├── clear.py
│   └── pdf_download.py


## 🛠️ Setup Instructions

1. Clone or download the project
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Start your MongoDB server (local or Atlas)
4. Add your Cohere API Key in `cohere_handler.py`:

```
COHERE_API_KEY = "Ktcs8hTzcykhR1e978yzrcNBj6j8u4s1hHhOViSn "
```

5. Run the server:

```
python app.py
```

## 🧠 Features

- Chat using Cohere
- Store & retrieve session history
- Knowledge base fallback
- Web search fallback (DuckDuckGo)
- Export conversation to PDF
