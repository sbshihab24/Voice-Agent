# 🎙️ Bella | Live Voice Assistant

A next-generation, real-time AI voice receptionist built with **Python**, **Streamlit**, and the **OpenAI Realtime API**.

---

## 📖 Overview

**Bella** is more than a chatbot — she is a **human-like, real-time voice receptionist**.  
Unlike traditional bots that record → transcribe → reply, Bella uses **WebRTC** to stream audio directly to **GPT-4o** for:

- ⚡ **Zero-latency conversation**
- 🔄 **Full interruptibility** (you can talk over her and she responds naturally)
- 🎧 **Continuous, fluid, human-style interaction**

The UI is built with a modern glassmorphism design, responsive layout, and animated visualizers.

---

## ✨ Key Features

### ⚡ Real-Time Voice Interaction  
Powered by **gpt-4o-realtime-preview** using WebRTC.

### 🗣️ Auto-Greeting  
Bella speaks the moment the call connects — no silent waiting.

### 🎨 Premium UI  
A full-screen, modern interface featuring:

- Glassmorphism layout  
- Fixed professional background  
- Live audio visualizers for both user and AI  
- Active speaker glow effects  

### 📝 Live Transcription  
Both user and assistant speech appear instantly as chat bubbles.

### 📄 Smart Call Summary  
When the call ends, Bella automatically generates a **bullet-point summary**.

### 🎭 Custom Personality  
Bella uses a **sweet, friendly, professional** persona tuned with the **Shimmer** voice model.

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, JavaScript (WebRTC, Web Audio API), Tailwind CSS  
- **Backend:** Python, Streamlit  
- **AI:** OpenAI Realtime API  
- **Deployment:** Streamlit Cloud / Localhost  

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python **3.10+**
- OpenAI API Key with Realtime API access

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/voice-receptionist.git
cd voice-receptionist

### 3. Install Dependencies
```bash
pip install -r requirements.txt

### 4. Configure Environment
```bash
OPENAI_API_KEY=sk-proj-your-api-key-here


