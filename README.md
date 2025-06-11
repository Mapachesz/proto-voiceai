# Proto Voice AI

This project simulates a simple phone call. It listens to the microphone, uses [Vosk](https://alphacephei.com/vosk/) to transcribe speech, generates a reply with a local HuggingFace model, and reads the response with Coqui TTS.

## Installation

1. (Optional) create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download a Vosk model (e.g. `vosk-model-small-es-0.42`) and set the path in a `.env` file if different:
   ```
   VOSK_MODEL_PATH=/path/to/vosk-model
   ```

## Usage

Run the main program and speak. Press `Ctrl+C` to end the call:
```bash
python main.py
```
