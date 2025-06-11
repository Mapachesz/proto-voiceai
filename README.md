# Proto Voice AI

This project simulates a simple phone call. It listens to the microphone, uses Whisper to transcribe speech, sends the text to OpenAI, and reads the response with Coqui TTS.

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
3. Provide your OpenAI key in a `.env` file:
   ```
   OPENAI_API_KEY=your_key_here
   ```

## Usage

Run the main program and speak. Press `Ctrl+C` to end the call:
```bash
python main.py
```
