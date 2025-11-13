"""
Streamlit OpenAI Chatbot Application

A web-based chatbot interface using Streamlit and OpenAI's API.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="OpenAI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    """Initialize and cache the OpenAI client"""
    # Try to get API key from Streamlit secrets first, then fall back to environment variables
    api_key = None
    
    # First, try Streamlit secrets (for cloud deployment)
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
    except (KeyError, FileNotFoundError):
        # Fall back to environment variable (for local development)
        api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        st.error("⚠️ OPENAI_API_KEY not found. Please add it to Streamlit secrets (cloud) or .env file (local).")
        st.stop()
    
    return OpenAI(api_key=api_key)

client = get_openai_client()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# App title and description
st.title("🤖 OpenAI Chatbot")
st.markdown("Ask me anything! I'm powered by OpenAI's GPT model.")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    *[{"role": m["role"], "content": m["content"]} 
                      for m in st.session_state.messages]
                ],
                stream=True
            )
            
            # Stream the response
            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            error_message = f"Error: {str(e)}"
            message_placeholder.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# Sidebar with options
with st.sidebar:
    st.header("Options")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    st.markdown("### About")
    st.markdown("""
    This chatbot uses OpenAI's GPT-3.5-turbo model to provide intelligent responses.
    
    **Features:**
    - Real-time streaming responses
    - Conversation history
    - Secure API key management
    """)
    
    st.divider()
    
    st.markdown("### Configuration")
    # Check for API key in both Streamlit secrets and environment
    api_key_configured = False
    try:
        if st.secrets.get("OPENAI_API_KEY"):
            api_key_configured = True
    except (KeyError, FileNotFoundError):
        if os.getenv("OPENAI_API_KEY"):
            api_key_configured = True
    
    api_key_status = "✅ Configured" if api_key_configured else "❌ Not Found"
    st.markdown(f"**API Key:** {api_key_status}")
    
    if st.session_state.messages:
        st.markdown(f"**Messages:** {len(st.session_state.messages)}")
