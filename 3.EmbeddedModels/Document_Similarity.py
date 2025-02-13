# "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership. "
    # "MS Dhoni, a former Indian captain, is famous for his calm demeanor and finishing skills. "
    # "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records. "
    # "Rohit Sharma is known for his elegant batting and record-breaking double centuries. "
    # "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv

load_dotenv()

# Load Gemini Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", dimensions=300)

# Store all information as individual Documents
documents = [
    Document(page_content="Virat Kohli is an Indian cricketer known for his aggressive batting and leadership."),
    Document(page_content="MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills."),
    Document(page_content="Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records."),
    Document(page_content="Rohit Sharma is known for his elegant batting and record-breaking double centuries."),
    Document(page_content="Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."),
]

# Extract only the text for embeddings
document_texts = [doc.page_content for doc in documents]

query = 'Tell me about Bumrah'

# Generate embeddings
doc_embeddings = embeddings.embed_documents(document_texts)  
query_embedding = embeddings.embed_query(query)

# Ensure proper shape for cosine similarity
doc_embeddings = np.array(doc_embeddings)
query_embedding = np.array(query_embedding).reshape(1, -1)

# Compute similarity scores
scores = cosine_similarity(query_embedding, doc_embeddings)[0]
best_match_idx = np.argmax(scores)  # Get index of highest similarity
best_match_score = scores[best_match_idx]

print(f"Query: {query}")
print(f"Most Similar Document: {documents[best_match_idx].page_content}")
print(f"Similarity Score: {best_match_score:.4f}")

# Create FAISS Vector Store
vector_db = FAISS.from_documents(documents, embeddings)
