import httpx
import logging

logger = logging.getLogger(__name__)

async def call_gemini(api_key: str, contents: list) -> str:
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(endpoint, json={"contents": contents}, headers=headers, params=params)
        if response.status_code != 200:
            logger.error(f"Gemini API error: {response.text}")
            raise RuntimeError(f"Gemini API error: {response.text}")

        data = response.json()
        candidates = data.get("candidates", [])
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            if parts:
                return parts[0].get("text", "").strip()
        raise RuntimeError("No reply from Gemini")
