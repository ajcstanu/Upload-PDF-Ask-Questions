from flask import Flask, request, jsonify, render_template
import os
import sqlite3
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
DATABASE = "askme.db"
UPLOAD_FOLDER = "uploads"
vector_store = None

# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Database initialization
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pdf_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Save PDF record to database
def save_pdf_record(filename):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pdf_records (filename) VALUES (?)", (filename,))
    conn.commit()
    conn.close()

# Load PDF and extract text
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    return texts

# Create vector store
def create_vector_store(texts):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(texts, embeddings)
    return vector_store

# Ask question to LLM
def ask_question(query, vector_store):
    llm = OpenAI()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())
    response = qa.run(query)
    return response

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_pdf():
    global vector_store
    file = request.files['file']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        try:
            file.save(file_path)
            texts = load_pdf(file_path)
            vector_store = create_vector_store(texts)
            save_pdf_record(file.filename)
            return jsonify({"message": "PDF uploaded and processed successfully."})
        except Exception as e:
            return jsonify({"error": f"Error processing file: {str(e)}"}), 500
    return jsonify({"error": "No file uploaded."}), 400

@app.route('/ask', methods=['POST'])
def ask():
    global vector_store
    if vector_store is None:
        return jsonify({"error": "No PDF uploaded yet."}), 400
    query = request.json.get("query")
    if query:
        try:
            response = ask_question(query, vector_store)
            return jsonify({"answer": response})
        except Exception as e:
            return jsonify({"error": f"Error answering question: {str(e)}"}), 500
    return jsonify({"error": "No query provided."}), 400

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
