# Upload-PDF-Ask-Questions
# LLM-Based AskMe

## Overview
LLM-Based AskMe is a Flask-based application that enables users to upload PDF files and ask natural language questions about their contents. It uses **Ollama** for LLM processing, **LangChain** for document retrieval, and **FAISS** for efficient vector-based search.

## Features
- Upload PDF documents
- Extract and process text using **LangChain**
- Store embeddings using **FAISS**
- Query PDFs using **Ollama** LLM
- Simple web interface for interaction

## Technologies Used
- **Python** (Backend)
- **Flask** (Web Framework)
- **LangChain** (Document Processing & Retrieval)
- **FAISS** (Vector Storage)
- **Ollama** (LLM Model)
- **SQLite** (Database)
- **HTML, JavaScript** (Frontend)

## Installation
### Prerequisites
Ensure you have Python installed. Then, install the required dependencies:

```sh
pip install flask langchain ollama pypdf faiss-cpu
```

## How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/llm-askme.git
   cd llm-askme
   ```
2. Run the application:
   ```sh
   python app.py
   ```
3. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
4. Upload a PDF and start asking questions!

## Project Structure
```
/llm-askme
│── app.py          # Main Flask application
│── database.py     # Database initialization
│── process_pdf.py  # PDF processing functions
│── query_llm.py    # LLM interaction functions
│── templates/
│   └── index.html  # Frontend HTML
│── static/
│   └── styles.css  # CSS styling (optional)
│── uploads/        # Folder to store uploaded PDFs
```

## API Endpoints
### Upload PDF
**Endpoint:** `POST /upload`
- **Request:** Multipart form-data (`file` as PDF)
- **Response:** JSON with success or error message

### Ask a Question
**Endpoint:** `POST /ask`
- **Request:** JSON `{ "query": "Your question here" }`
- **Response:** JSON `{ "answer": "Generated response" }`

## Future Enhancements
- Add support for multiple PDF uploads
- Implement authentication for user sessions
- Improve UI with better styling and interactivity

## License
This project is open-source and available under the MIT License.

