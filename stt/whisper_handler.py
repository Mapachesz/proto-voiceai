import numpy as np
import sounddevice as sd

try:
    from faster_whisper import WhisperModel
except ImportError as e:
    raise ImportError("faster_whisper is required for Whisper STT") from e

from utils.config import WHISPER_MODEL_SIZE

_model = WhisperModel(WHISPER_MODEL_SIZE)


def listen_and_transcribe(duration=5, sample_rate=16000):
    """Record audio and transcribe it with Whisper."""
    print("Listening...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    audio = recording.flatten().astype(np.float32) / 32768.0
    segments, _ = _model.transcribe(audio, language="es")
    text = " ".join(seg.text for seg in segments).strip()
    return text
