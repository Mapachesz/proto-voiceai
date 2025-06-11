import openai
from utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def ask_openai(prompt, chat_history=None, model="gpt-3.5-turbo"):
    """Send prompt plus optional history to OpenAI and return the reply."""
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not set")
    history = chat_history or []
    messages = [{"role": m["role"], "content": m["content"]} for m in history]
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(model=model, messages=messages)
    answer = response.choices[0].message.content.strip()
    history += [{"role": "user", "content": prompt}, {"role": "assistant", "content": answer}]
    return answer, history
