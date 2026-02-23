import streamlit as st
from services.career_service import CareerAdvisorService
from utils.logger import logger

st.set_page_config(page_title="AI Career Advisor", layout="wide")

st.title(" AI Career Advisor (Powered by Groq)")

# Initialize the service
if "advisor" not in st.session_state:
    try:
        st.session_state.advisor = CareerAdvisorService()
    except Exception as e:
        st.error("Failed to initialize the Career Advisor service. Please check your configuration.")
        logger.error(f"Initialization error: {str(e)}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.header("Monitoring")
    st.write(f"Total Session Tokens: {st.session_state.advisor.get_token_stats()}")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask about your career..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = st.session_state.advisor.get_response(prompt)
    except Exception as e:
        response = "I encountered an unexpected error. Please try again."
        logger.error(f"UI layer error: {str(e)}")

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})