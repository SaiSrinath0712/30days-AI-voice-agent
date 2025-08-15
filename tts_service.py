import httpx
import logging

logger = logging.getLogger(__name__)

async def generate_tts(api_key: str, text: str, voice_id="en-IN-alia", format="mp3") -> str:
    murf_endpoint = "https://api.murf.ai/v1/speech/generate"
    headers = {"api-key": api_key, "Content-Type": "application/json"}
    payload = {"text": text, "voice_id": voice_id, "audio_format": format}

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(murf_endpoint, json=payload, headers=headers)
        if response.status_code != 200:
            logger.error(f"Murf API error: {response.text}")
            raise RuntimeError(f"Murf API error: {response.text}")
        
        data = response.json()
        url = data.get("audioFile") or data.get("audio_url")
        if not url:
            raise RuntimeError("No audio URL returned from Murf API")
        return url
