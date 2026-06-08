from fastapi import FastAPI, UploadFile, File
from src.services.stt import STTService
from src.services.tts import TTSService
from src.agents.receptionist import ReceptionistAgent
import os

app = FastAPI(title="AI Receptionist API")

stt_service = STTService()
tts_service = TTSService()
agent = ReceptionistAgent()

@app.post("/voice-chat")
async def voice_chat(file: UploadFile = File(...)):
    # 1. Save uploaded audio
    temp_input = "temp_input.wav"
    with open(temp_input, "wb") as buffer:
        buffer.write(await file.read())
    
    # 2. Transcribe
    user_text = await stt_service.transcribe_audio(temp_input)
    
    # 3. Get AI Response
    ai_response_text = await agent.process_input(user_text)
    
    # 4. Generate Speech
    temp_output = "static/response.mp3"
    await tts_service.generate_speech(ai_response_text, temp_output)
    
    return {
        "user_said": user_text,
        "ai_response": ai_response_text,
        "audio_url": "/static/response.mp3"
    }

@app.get("/health")
def health_check():
    return {"status": "online"}
