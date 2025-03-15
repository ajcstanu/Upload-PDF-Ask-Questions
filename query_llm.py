from langchain.chains import RetrievalQA
from langchain.llms import Ollama

def ask_question(query, vector_store, ollama_model="mistral"): #added model parameter, and default value.
    """Asks a question using RetrievalQA with Ollama."""
    try:
        retriever = vector_store.as_retriever()
        llm = Ollama(model=ollama_model)
        qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever) #Use from_chain_type for more control.
        response = qa_chain.run(query)
        return response
    except ValueError as ve: #Catch value errors, such as a model not being available.
        print(f"Ollama model error: {ve}")
        return "Error: Ollama model issue."
    except Exception as e:
        print(f"Error asking question: {e}")
        return "Error: An unexpected error occurred."

# Example Usage (assuming you have a vector_store):
if __name__ == "__main__":
    # Assuming vector_store is already created.
    # replace with your actual vector store.
    class MockVectorStore:
        def as_retriever(self):
            return None
    vector_store = MockVectorStore()

    query = "What is the capital of France?"
    answer = ask_question(query, vector_store)
    print(answer)
