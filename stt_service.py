import assemblyai as aai
import logging

logger = logging.getLogger(__name__)

def init_stt(api_key: str):
    aai.settings.api_key = api_key
    logger.info("AssemblyAI STT initialized")
    return aai.Transcriber()

def transcribe_file(transcriber, file_path: str) -> str:
    logger.debug(f"Transcribing file: {file_path}")
    transcript = transcriber.transcribe(file_path)
    if transcript.error:
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    return transcript.text.strip()
