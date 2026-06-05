import openai
from src.config import settings

class STTService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

    async def transcribe_audio(self, audio_file_path: str) -> str:
        """Transcribes audio using OpenAI Whisper."""
        with open(audio_file_path, "rb") as audio:
            transcript = self.client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio
            )
        return transcript.text