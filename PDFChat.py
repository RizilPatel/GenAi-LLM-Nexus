import streamlit as st
from PyPDF2 import PdfReader
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from deep_translator import GoogleTranslator
from dotenv import load_dotenv

# Load environment variables 
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("⚠️ GOOGLE_API_KEY not found. Make sure it's set in your environment variables.")
    st.stop()

# Configure Google Gemini API
genai.configure(api_key=API_KEY)

# Initialize Translator for Multi-Language Support
translator = GoogleTranslator()

# List of Supported Languages
LANGUAGES = {
    "English": "en",
    "Hindi (हिन्दी)": "hi",
    "Marathi (मराठी)": "mr",
    "French (Français)": "fr",
    "Russian (Русский)": "ru",
    "Spanish (Español)": "es",
    "German (Deutsch)": "de",
    "Chinese (中文)": "zh-cn",
    "Japanese (日本語)": "ja",
    "Arabic (العربية)": "ar"
}

# Function to extract text from PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        with pdfplumber.open(pdf) as pdf_reader:
            for page in pdf_reader.pages:
                text += page.extract_text() or ""  # Ensure None does not break processing
    return text if text.strip() else None

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

# Function to create FAISS vector store
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Function to load QA chain
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in the provided context, respond with:
    "Answer is not available in the context." Do not make up an answer.

    Context:\n {context}?\n
    Question:\n {question}\n
    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)

# Function to handle user queries
def user_input(user_question, selected_language):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    try:
        # Fix: Enable FAISS deserialization
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(user_question)

        if not docs:
            st.warning("No relevant information found in the uploaded PDFs.")
            return

        chain = get_conversational_chain()
        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

        generated_text = response.get("output_text", "No response generated.")

        # Translate output to the selected language
        translated_response = GoogleTranslator(source="auto", target=LANGUAGES[selected_language]).translate(generated_text)

        st.write(f"💬 **Reply ({selected_language}):** ", translated_response)

    except Exception as e:
        st.error(f"⚠️ Error processing query: {str(e)}")

def main():
    # st.set_page_config(page_title="Chat PDF", layout="wide")

    # Header
    st.header("📄 Chat with PDF using Gemini 💁")

    # Language Selection Dropdown
    selected_language = st.selectbox("🌍 Choose a language for responses:", list(LANGUAGES.keys()))

    # User input field
    user_question = st.text_input("🔍 Ask a question about the PDF files:")
    if user_question:
        user_input(user_question, selected_language)

    # Sidebar for PDF upload
    with st.sidebar:
        st.title("📂 Upload PDFs")
        pdf_docs = st.file_uploader("📄 Upload PDF files & click Submit", accept_multiple_files=True)

        if st.button("🚀 Submit & Process"):
            with st.spinner("Processing PDFs..."):
                raw_text = get_pdf_text(pdf_docs)
                if not raw_text:
                    st.error("⚠️ No text extracted from the PDFs. Try another file.")
                    return

                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("✅ PDFs processed successfully!")

if __name__ == "__main__":
    main()
