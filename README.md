# Proto Voice AI

This project simulates a simple phone call. It listens to the microphone using Whisper, sends the transcript to OpenAI's chat API, and speaks the response with Coqui TTS.

## Installation

1. (Optional) create a Python 3.11 virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API key and Whisper model size:
   ```
   OPENAI_API_KEY=your-key-here
   WHISPER_MODEL_SIZE=small
   ```

## Usage

Run the main program and speak. Press `Ctrl+C` to end the call:
```bash
python main.py
```
