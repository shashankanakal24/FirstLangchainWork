# 🚀 FirstLangchainWork  

This repository demonstrates **LangChain** integration with **Google Gemini** and **Hugging Face**, utilizing **FAISS** for vector search and **LLM-powered chat models**. The project enables querying via **remote API-based models** and **locally downloaded models** from Hugging Face.  

---

## 📌 Features  
- **🔗 LangChain Integration** – Seamlessly connects to LLMs.  
- **🤖 Google Gemini LLM** – Utilizes `models/embedding-001` for embeddings.  
- **📚 Hugging Face Chat Model** – Supports both API-based remote models and locally downloaded models.  
- **⚡ FAISS Vector Store** – Efficient similarity search implementation.  
- **📝 Query Processing** – Computes cosine similarity for best responses.  

---

## 📂 Project Structure  
```plaintext
FirstLangchainWork/
│── venv/                     # Virtual environment (not tracked in Git)
│── .gitignore                 # Ignores venv and .env files
│── .env                       # Environment variables (DO NOT COMMIT)
│── main.py                    # Main script
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation

```
##Create and Activate Virtual Environment
# Windows  
```plaintext
python -m venv venv  
venv\Scripts\activate  
```

# macOS/Linux  
```plaintext
python3 -m venv venv  
source venv/bin/activate
```

##  Install Dependencies
```plaintext
pip install -r requirements.txt
```

## Set Up Environment Variables
```plaintext
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

## Run the script:
```plaintext
python main.py
```
