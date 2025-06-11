from dotenv import load_dotenv
import os

# Cargar automáticamente variables del archivo .env
load_dotenv()

# Configuration
HF_MODEL_NAME = os.getenv("HF_MODEL_NAME", "microsoft/DialoGPT-medium")
VOSK_MODEL_PATH = os.getenv("VOSK_MODEL_PATH", "model")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WHISPER_MODEL_SIZE = os.getenv("WHISPER_MODEL_SIZE", "small")
TTS_MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"
