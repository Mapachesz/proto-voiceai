import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
from utils.config import WHISPER_MODEL_SIZE

_model = WhisperModel(WHISPER_MODEL_SIZE)


def listen_and_transcribe(duration=5, sample_rate=16000):
    """Record audio from the microphone and return the transcribed text."""
    print("Listening...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    audio = recording.flatten()
    segments, _ = _model.transcribe(audio, language="es")
    text = " ".join(segment.text for segment in segments)
    return text.strip()
