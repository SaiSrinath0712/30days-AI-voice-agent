from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class AudioUrlInput(BaseModel):
    audio_url: str
