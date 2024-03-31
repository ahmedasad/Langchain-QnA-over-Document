# Talk to Your Book

## Introduction

Created a **Course Instructor** Chatbot for the course **Introduction to Computer Science**.
Where Students can ask question related to the against the given knowledge to the chatbot

## Prompt
"""You are a teacher having conversation with student.\
            Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. \
                otherwise tell the student that you don't have this knowledge in book.

Human: {question}
{context}
teacher:
"""
## Demo
https://github.com/ahmedasad/Langchain-QnA-over-Document/assets/20832655/e1ecf2df-99e6-43bf-82f8-1623fb7a3ce4


## Kick-start 

- docker pull chromadb/chroma
- docker run -p 8000:8000 /Users/<user_name>/<directory_name>/chroma/:/chroma/chroma chromadb/chroma
- pip install -r requirements.txt

### Libraries and Tools used:
  - Python 3.9.6
  - openAI: we used the "gpt-3.5-turbo"
  - Langchain: document_loaders, to load/read and chunks making of the docuemnts
  - Langchain: OpenAIEmbedding, to create embeddings of chunks
  - Chroma Vector DB: To store vector embedding
  - streamlit for Chat UI
  - dotenv
