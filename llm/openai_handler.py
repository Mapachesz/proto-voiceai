import openai
from utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def ask_openai(prompt, chat_history=None, model="gpt-3.5-turbo"):
    """Send a prompt to OpenAI and return the assistant's reply.

    Parameters
    ----------
    prompt: str
        Text to send as the latest user message.
    chat_history: list, optional
        Previous chat history formatted as a list of message dicts.
    model: str, optional
        OpenAI chat model to use.
    """
    messages = chat_history[:] if chat_history else []
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(model=model, messages=messages)
    answer = response.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": answer})
    return answer, messages
