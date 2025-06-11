from TTS.api import TTS
import sounddevice as sd
from utils.config import TTS_MODEL_NAME

_tts = TTS(TTS_MODEL_NAME)


def speak_text(text):
    """Speak the given text using Coqui TTS."""
    waveform = _tts.tts(text)
    sd.play(waveform, samplerate=_tts.synthesizer.output_sample_rate)
    sd.wait()
