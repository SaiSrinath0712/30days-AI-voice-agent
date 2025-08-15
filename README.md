**Project Overview**
This project is a Conversational AI Voice Agent built with:-
FastAPI backend (Python)
AssemblyAI for real-time speech-to-text transcription
Google Gemini API for advanced conversational AI replies
Murf API for text-to-speech, generating natural-sounding voice replies
HTML + JavaScript frontend for user interaction (microphone, chat UI)
Context-aware chat history per session (in-memory store)
Users interact via the browser microphone. The agent listens, understands conversational context, replies using Gemini, and speaks the answer using Murf.

**Features**
 Record voice queries using browser microphone
 Transcribe speech to text with AssemblyAI
 Send conversation history and get context-aware replies with Gemini
 Generate and play realistic voice replies via Murf
 Per-session chat history
 Stylish, responsive frontend with animated buttons and backgrounds


**TechStack**
  Component                 |         Technology 
 Backend (API)	            |          FastAPI  
 Speech-to-Text	            |          AssemblyAI
 LLM Conversation	          |          Google Gemini
 Text-to-Speech	            |          Murf API
 Frontend	                  |          HTML, CSS, JS 
 Environment Variables      |	         dotenv (.env file)


**Structure**
 project/
│
├── main.py                   # FastAPI app entry
├── requirements.txt          # Dependencies
├── README.md                 # Project description & usage
├── .env                     # Environment variables (API keys)
│
├── models/                   # Pydantic schemas for requests/responses
│   ├── __init__.py
│   ├── requests.py
│   └── responses.py
│
├── services/                 # Business logic for 3rd-party APIs
│   ├── __init__.py
│   ├── stt_service.py        # Speech-to-text logic (AssemblyAI)
│   ├── tts_service.py        # Text-to-speech logic (Murf)
│   ├── llm_service.py        # LLM API logic (Gemini)
│   └── chat_history.py       # Chat history management
│
├── static/                   # Frontend static files (index.html, CSS, JS)
│
└── uploads/                  # Temp audio file storage



Set Up Virtual Environment:-
python -m venv venv
venv\Scripts\activate      # Windows


**Install Dependencies**
#Step-1:
Add these to your requirements.txt:
fastapi
uvicorn
assemblyai
httpx
python-dotenv

#Step-2:
Then install:
pip install -r requirements.txt

**Run the Application**
uvicorn main:app --reload

**Workflow**
User presses “Start Recording” and speaks.
Browser sends recording to FastAPI backend.
Backend transcribes audio, sends chat history to Gemini, gets reply.
Reply is converted to speech (Murf), audio link & Gemini text returned.
Browser plays voice reply and shows text.
Repeat for contextual, multi-turn conversations.

**Notes & Limitations**
Chat history is currently in-memory — resets on server restart.
Murf API has character limits; long replies are split automatically.
AssemblyAI/Gemini/Murf API keys required.
All audio files are stored temporarily only.
