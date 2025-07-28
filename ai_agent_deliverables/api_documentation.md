# 📘 API Documentation

## Chat Service
- `POST /chat`  
  → Send user query and receive answer

- `GET /chat/<chat_id>`  
  → Get chat history for a session

## Knowledge Base
- `POST /query`  
  → Search from knowledge base using embedded query

- `POST /ingest`  
  → Add new knowledge to the KB

## Search Service
- `GET /search?query=your_text`  
  → Web search fallback for unanswered queries

## History Service
- `POST /history`  
  → Save message history

- `GET /history/<chat_id>`  
  → Retrieve message history by ID

## PDF
- `GET /download_pdf/<chat_id>`  
  → Download PDF of chat history
