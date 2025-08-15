import os
import shutil
import tempfile
import logging
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException, Path as ApiPath
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from models.requests import TextInput
from models.responses import TTSResponse, ChatResponse, TranscriptionResponse
from services import stt_service, tts_service, llm_service, chat_history

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load env vars
load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
MURF_API_KEY = os.getenv("MURF_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not all([ASSEMBLYAI_API_KEY, MURF_API_KEY, GEMINI_API_KEY]):
    raise RuntimeError("Missing required API keys in .env")

# Init FastAPI app
app = FastAPI()

# Init STT transcriber
transcriber = stt_service.init_stt(ASSEMBLYAI_API_KEY)

# Paths
UPLOADS_DIR = Path("uploads"); UPLOADS_DIR.mkdir(exist_ok=True)
STATIC_DIR = Path("static"); STATIC_DIR.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
async def root():
    return FileResponse(STATIC_DIR / "index.html")

@app.post("/generate-audio", response_model=TTSResponse)
async def generate_audio(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty")
    audio_url = await tts_service.generate_tts(MURF_API_KEY, input.text.strip())
    return {"audio_url": audio_url}

@app.post("/agent/chat/{session_id}", response_model=ChatResponse)
async def chat_with_history(session_id: str = ApiPath(...), file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(dir=UPLOADS_DIR, suffix=".wav", delete=False) as temp_audio:
        shutil.copyfileobj(file.file, temp_audio)
        temp_path = temp_audio.name
    logger.debug(f"Uploaded file saved at {temp_path}")

    try:
        user_text = stt_service.transcribe_file(transcriber, temp_path)
    finally:
        os.unlink(temp_path)

    chat_history.add_message(session_id, "user", user_text)
    llm_reply = await llm_service.call_gemini(GEMINI_API_KEY, chat_history.build_contents(session_id))
    chat_history.add_message(session_id, "model", llm_reply)

    audio_url = await tts_service.generate_tts(MURF_API_KEY, llm_reply)
    return {"audio_url": audio_url, "llm_text": llm_reply}
