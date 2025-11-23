import streamlit as st
import os
from dotenv import load_dotenv
from utils import get_ephemeral_token
from ui_components import render_voice_receptionist_ui

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Bella | Live Assistant",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit's default elements for a cleaner look
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

def main():
    # 1. API Key Setup
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Simple fallback if .env is not set
    if not api_key:
        st.warning("No API Key found in .env")
        api_key = st.text_input("Enter OpenAI API Key", type="password")

    if not api_key:
        return
        
    # 2. Get Token
    token = get_ephemeral_token(api_key)
    
    # 3. Render UI (No extra arguments needed)
    if token:
        render_voice_receptionist_ui(token)
    else:
        st.error("Failed to connect to OpenAI. Check your API Key.")

if __name__ == "__main__":
    main()