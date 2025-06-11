import signal

from llm.hf_handler import ask_model
from stt.vosk_handler import listen_and_transcribe
from tts.tts_handler import speak_text


def run_call():
    """Run a simple voice call loop until interrupted."""
    conversation = []
    print("Starting call. Press Ctrl+C to hang up.")
    try:
        while True:
            user_text = listen_and_transcribe()
            if not user_text:
                continue
            print(f"User: {user_text}")
            response, conversation = ask_model(user_text, conversation)
            print(f"Assistant: {response}")
            speak_text(response)
    except KeyboardInterrupt:
        print("\nCall ended.")


if __name__ == "__main__":
    run_call()
