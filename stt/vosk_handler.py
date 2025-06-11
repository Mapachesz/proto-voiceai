import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

from utils.config import VOSK_MODEL_PATH

_model = Model(VOSK_MODEL_PATH)


def listen_and_transcribe(duration=5, sample_rate=16000):
    """Record audio from the microphone and return the transcribed text."""
    print("Listening...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    rec = KaldiRecognizer(_model, sample_rate)
    rec.AcceptWaveform(recording.tobytes())
    result = json.loads(rec.Result())
    return result.get("text", "").strip()
