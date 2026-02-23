import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    """
    Returns the Groq LLM instance.
    Make sure GROQ_API_KEY is set in your .env file.
    """
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.5,
        max_retries=3,
    )