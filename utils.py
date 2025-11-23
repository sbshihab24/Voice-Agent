import requests
import streamlit as st

def get_ephemeral_token(openai_api_key):
    """
    Exchanges the long-lived API key for a temporary ephemeral token.
    """
    if not openai_api_key:
        return None
    
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-4o-realtime-preview-2024-10-01",
        "voice": "shimmer",
        # Enable transcription to show user text
        "input_audio_transcription": {
            "model": "whisper-1"
        },
        "instructions": (
            "You are Bella, a super cute, sweet, and bubbly AI receptionist. "
            "Your voice should sound smiling, lively, and warm. "
            "Do not be robotic; be very natural, like a friendly human receptionist. "
            "If the user connects, greet them warmly immediately. "
            "Keep responses concise (1-2 sentences) but very friendly."
        )
    }
    
    try:
        response = requests.post(
            "https://api.openai.com/v1/realtime/sessions",
            headers=headers,
            json=payload
        )
        if response.status_code == 200:
            return response.json()['client_secret']['value']
        else:
            st.error(f"Error getting token: {response.text}")
            return None
    except Exception as e:
        st.error(f"Connection error: {e}")
        return None