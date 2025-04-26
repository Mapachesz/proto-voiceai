from dotenv import load_dotenv
import os

# Cargar automáticamente variables del archivo .env
load_dotenv()

# Configuración
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WHISPER_MODEL_SIZE = "tiny"
TTS_MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"
