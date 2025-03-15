from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
import os

def load_pdf(pdf_path):
    """Loads a PDF, splits it into chunks, and returns the texts."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found at: {pdf_path}")
    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        texts = text_splitter.split_documents(documents)
        return texts
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None  # Or raise the exception, depending on your needs

def create_vector_store(texts, ollama_model="llama2"): # add a default value to the model.
    """Creates a FAISS vector store from the given texts."""
    try:
        embeddings = OllamaEmbeddings(model=ollama_model) #added model parameter.
        vector_store = FAISS.from_documents(texts, embeddings)
        return vector_store
    except Exception as e:
        print(f"Error creating vector store: {e}")
        return None # Or raise the exception, depending on your needs.

#Example usage.
if __name__ == "__main__":
    pdf_file_path = "example.pdf" #replace with your pdf file.

    try:
        texts = load_pdf(pdf_file_path)
        if texts:
            vector_store = create_vector_store(texts)
            if vector_store:
                print("Vector store created successfully.")
    except FileNotFoundError as e:
        print(e)
