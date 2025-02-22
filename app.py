import streamlit as st

# Set up Streamlit page (this should be at the very top of app.py)
st.set_page_config(page_title="Ultimate AI-Powered Toolkit", layout="wide")

# Main app title
st.title("🚀 Ultimate AI-Powered Toolkit")

# Sidebar with options 
st.sidebar.title("Select a Functionality")
option = st.sidebar.radio("Choose an option:", 
                          ["📄 Multi-PDF Chat", "📊 Database Querying", "🎥 YouTube Transcribe"])

# Main Content based on option selection
if option == "📄 Multi-PDF Chat":
    # st.subheader("📄 Chat with Multiple PDFs")
    # Execute pdfchat.py script with utf-8 encoding
    try:
        exec(open("PDFChat.py", encoding="utf-8").read())  # Load and execute PDFChat functionality
    except Exception as e:
        st.error(f"⚠️ Error loading PDFChat functionality: {str(e)}")

elif option == "📊 Database Querying":
    # st.subheader("📊 Query a Database using SQL")
    # Execute sql.py script with utf-8 encoding
    try:
        exec(open("sql.py", encoding="utf-8").read())  # Load and execute SQL functionality
    except Exception as e:
        st.error(f"⚠️ Error loading SQL functionality: {str(e)}")

elif option == "🎥 YouTube Transcribe":
    # st.subheader("🎥 Transcribe YouTube Videos")
    # Execute youtube.py script with utf-8 encoding
    try:
        exec(open("youtube.py", encoding="utf-8").read())  # Load and execute YouTube transcription functionality
    except Exception as e:
        st.error(f"⚠️ Error loading YouTube transcription functionality: {str(e)}")
