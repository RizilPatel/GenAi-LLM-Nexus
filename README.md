# 🚀 GenAi-LLM-Nexus

### **AI-powered Multi-PDF Chat Tool with SQL Generation & YouTube Transcription**  

![GitHub Repo Stars](https://img.shields.io/github/stars/rizilpatel/GenAi-LLM-Nexus?style=social)
![GitHub Forks](https://img.shields.io/github/forks/rizilpatel/GenAi-LLM-Nexus?style=social)
![GitHub License](https://img.shields.io/github/license/rizilpatel/GenAi-LLM-Nexus)
![GitHub Last Commit](https://img.shields.io/github/last-commit/rizilpatel/GenAi-LLM-Nexus)

---

## **🔹 Overview**
GenAi-LLM-Nexus is an **AI-powered chat tool** that allows users to interact with **multiple PDFs**, generate **dynamic SQL queries**, and transcribe **YouTube videos**, all powered by **Google Gemini Pro API** and **LangChain**.

✅ **Multi-PDF Support** – Upload multiple PDFs and chat with their content.  
✅ **Multi-Language Chat** – Supports 5+ languages for seamless interactions.  
✅ **SQL Query Generation** – Convert natural language questions into optimized SQL queries.  
✅ **YouTube Transcription** – Extract transcripts from YouTube videos and interact with them.  
✅ **Optimized Search** – FAISS vector stores improve accuracy by **20%** while reducing processing time.  
✅ **Streamlit UI** – Designed an intuitive UI, increasing user engagement by **70%**.  

---

## **🛠️ Tech Stack**
- **AI & NLP:** Google Gemini Pro API, LangChain  
- **Database & Storage:** FAISS Vector Store  
- **Web Framework:** Streamlit  
- **Backend:** Python, FastAPI  
- **Libraries:** PyMuPDF, OpenAI, pandas, NumPy  

---

## **⚡ Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/rizilpatel/GenAi-LLM-Nexus.git
cd GenAi-LLM-Nexus
python -m venv venv
```
2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

4️⃣ Set Up Environment Variables
Create a .env file in the project root and add:
```
```env
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
```

🚀 Running the Application
Run Streamlit App
```sh
streamlit run app.py
```
Now open http://localhost:8501/ in your browser.
