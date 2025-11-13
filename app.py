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
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
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

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0E1117 0%, #1E2228 100%);
    }
    .stChatMessage {
        background-color: rgba(30, 34, 40, 0.5);
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    h1 {
        background: linear-gradient(90deg, #10A37F 0%, #1a7f64 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    .subtitle {
        color: #10A37F;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #10A37F 0%, #1a7f64 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #1a7f64 0%, #10A37F 100%);
        box-shadow: 0 4px 12px rgba(16, 163, 127, 0.4);
        transform: translateY(-2px);
    }
    .chat-container {
        max-width: 900px;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

# App header with improved styling
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.title("🤖 AI Chat Assistant")
    st.markdown('<p class="subtitle">💬 Powered by OpenAI GPT • Ask me anything!</p>', unsafe_allow_html=True)
    st.markdown("---")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🧑‍💻" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("💭 Type your message here...", key="chat_input"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant", avatar="🤖"):
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
    st.markdown("## ⚙️ Settings")
    
    # Clear chat button with better styling
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    
    # About section with enhanced styling
    st.markdown("### 📖 About")
    st.info("""
    **AI Chat Assistant** uses OpenAI's GPT-3.5-turbo model to provide intelligent, 
    context-aware responses to your questions.
    """)
    
    # Features with icons
    st.markdown("### ✨ Features")
    st.markdown("""
    - ⚡ Real-time streaming responses
    - 💾 Persistent conversation history
    - 🔒 Secure API key management
    - 🎨 Modern, responsive UI
    - 🌙 Dark mode optimized
    """)
    
    st.markdown("---")
    
    # Configuration status
    st.markdown("### 🔧 Configuration")
    
    # Check for API key in both Streamlit secrets and environment
    api_key_configured = False
    try:
        if st.secrets.get("OPENAI_API_KEY"):
            api_key_configured = True
    except (KeyError, FileNotFoundError):
        if os.getenv("OPENAI_API_KEY"):
            api_key_configured = True
    
    if api_key_configured:
        st.success("✅ API Key Configured")
    else:
        st.error("❌ API Key Not Found")
    
    if st.session_state.messages:
        st.metric("💬 Messages", len(st.session_state.messages))
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; color: #10A37F; font-size: 0.9rem;'>
    Made with ❤️ using Streamlit & OpenAI
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
