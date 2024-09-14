from PyPDF2 import PdfFileReader
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

import streamlit as st
from PIL import Image
import io
from transformers import pipeline

# Load pre-trained QA model
qa_pipeline = pipeline("question-answering")

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        for page in range(reader.numPages):
            text += reader.getPage(page).extract_text()
    return text

def embed_text(text):
    sentences = text.split('\n')  # Simple splitting; use more sophisticated methods in production
    embeddings = model.encode(sentences)
    return embeddings, sentences

def save_embeddings(embeddings, sentences):
    # Save embeddings to FAISS or another vector database
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, sentences


def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']



st.title("Interactive QA Bot")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with open("uploaded_document.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.write("PDF uploaded successfully!")

    # Process document
    text = extract_text_from_pdf("uploaded_document.pdf")
    embeddings, sentences = embed_text(text)
    index, sentences = save_embeddings(embeddings, sentences)

    # User query
    query = st.text_input("Ask a question based on the document:")
    if query:
        # Perform query and get answer
        # Here you would need to use your stored embeddings to find the relevant context
        relevant_context = "..."  # Fetch relevant context using FAISS or another method
        answer = answer_question(query, relevant_context)
        st.write("Answer:", answer)
        st.write("Relevant text:", relevant_context)
