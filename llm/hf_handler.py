from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from utils.config import HF_MODEL_NAME

_tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_NAME)
_model = AutoModelForCausalLM.from_pretrained(HF_MODEL_NAME)


def ask_model(prompt, chat_history=None, max_new_tokens=50):
    """Generate a reply using a local HuggingFace model."""
    history = chat_history or []
    history_text = " ".join(f"{m['role']}: {m['content']}" for m in history)
    full_prompt = f"{history_text} user: {prompt}\nassistant:" if history_text else f"user: {prompt}\nassistant:"
    input_ids = _tokenizer.encode(full_prompt, return_tensors="pt")
    output_ids = _model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        pad_token_id=_tokenizer.eos_token_id,
    )
    answer = _tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True).strip()
    history += [{"role": "user", "content": prompt}, {"role": "assistant", "content": answer}]
    return answer, history
