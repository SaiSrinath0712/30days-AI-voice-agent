# 30days-AI-voice-agent

A practical project to build and refine a conversational voice AI bot in 30 days!  
Combines speech-to-text, Google Gemini LLM, and text-to-speech APIs, with a modular backend and web frontend.

---

## Project Overview

This project is a Conversational AI Voice Agent built with:

- **FastAPI backend (Python)**
- **AssemblyAI** for real-time speech-to-text transcription
- **Google Gemini API** for advanced conversational AI replies
- **Murf API** for text-to-speech, generating natural-sounding voice replies
- **HTML + JavaScript frontend** for user interaction (microphone, chat UI)
- Context-aware chat history per session (in-memory store)

Users record voice queries, get intelligent replies, and hear spoken answers—all inside the browser.

---

## Features

- Record voice using your browser microphone
- Transcribe speech to text with AssemblyAI
- Get context-aware replies with Google Gemini LLM
- Generate and play realistic voice replies with Murf API
- Per-session chat history for multi-turn conversations
- Stylish and responsive frontend with animated buttons and backgrounds

---

## Tech Stack

| Component           | Technology             |
|---------------------|------------------------|
| Backend (API)       | FastAPI                |
| Speech-to-Text      | AssemblyAI             |
| LLM Conversation    | Google Gemini API      |
| Text-to-Speech      | Murf API               |
| Frontend            | HTML, CSS, JavaScript  |
| Environment Vars    | dotenv (.env file)     |

---

## Folder Structure

    your-project/
    ├── main.py # FastAPI app entry
    ├── requirements.txt # Python dependencies
    ├── README.md # Project overview and setup
    ├── .env # Environment variables (API keys)
    ├── models/ # Pydantic schemas for request/response
    │ ├── init.py
    │ ├── requests.py
    │ └── responses.py
    ├── services/ # Business logic for APIs (STT, TTS, LLM)
    │ ├── init.py
    │ ├── stt_service.py
    │ ├── tts_service.py
    │ ├── llm_service.py
    │ └── chat_history.py
    ├── static/ # Frontend static files (HTML, CSS, JS)
    ├── uploads/ # Temporary audio file storage

---

## Setup & Installation

### Step 1: Create and activate virtual environment

python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

### Step 2: Install dependencies

    Add these to `requirements.txt`:

    fastapi
    uvicorn
    assemblyai
    httpx
    python-dotenv
    pydantic

Then run:
pip install -r requirements.txt

### Step 3: Add API keys

Create a `.env` file in your project root and add:

      ASSEMBLYAI_API_KEY=your_assemblyai_key
      MURF_API_KEY=your_murf_key
      GEMINI_API_KEY=your_gemini_key

### Step 4: Start the FastAPI server

    uvicorn main:app --reload

---

## Usage Workflow

1. User clicks “Start Recording” and speaks through the browser.
2. Audio is sent to the FastAPI backend.
3. Backend transcribes audio via AssemblyAI, sends chat history to Gemini LLM, and gets a reply.
4. Reply text is converted to speech using Murf API.
5. Browser plays the speech reply and displays the text.
6. Repeat for multi-turn contextual conversation.

---

## Notes & Limitations

- Chat history is stored in memory and resets when the server restarts.
- Make sure to never commit `.env` or API keys to public repos.
- All 3rd-party service APIs require valid keys.
- The project demonstrates modular code with separation of concerns.

 

Feel free to customize this README further as you enhance your project!

If you want, I can help you generate the exact `requirements.txt` or `.gitignore` next.

