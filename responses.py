from pydantic import BaseModel

class TTSResponse(BaseModel):
    audio_url: str

class TranscriptionResponse(BaseModel):
    transcription: str

class ChatResponse(BaseModel):
    audio_url: str
    llm_text: str
