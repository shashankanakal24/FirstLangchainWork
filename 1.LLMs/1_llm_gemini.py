from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()


# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Create a prompt message
messages = [HumanMessage(content="Tell me a fun fact about space.")]

# Get LLM response
response = llm.invoke(messages)

# Print the response
print(response.content)
