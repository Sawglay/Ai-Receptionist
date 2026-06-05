import openai
from src.config import settings

class TTSService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

    async def generate_speech(self, text: str, output_path: str):
        """Generates voice response using OpenAI TTS."""
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        response.stream_to_file(output_path)