from unsloth import FastLanguageModel
from api.get_key import get_key
import threading

max_seq_length = 2048
_model = None
_tokenizer = None
_model_lock = threading.Lock()

def get_model_and_tokenizer():
    global _model, _tokenizer
    with _model_lock: # ensure that model is only loaded once with thread locking
        if _model is None or _tokenizer is None:
            _model, _tokenizer = FastLanguageModel.from_pretrained(
                model_name="unsloth/Phi-3-mini-4k-instruct",
                max_seq_length=max_seq_length,
                dtype=None,
                load_in_4bit=True,
                token=get_key('huggingface_token')
            )

            _model = FastLanguageModel.get_peft_model(
                _model,
                r = 16,
                target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj",],
                lora_alpha = 16,
                lora_dropout = 0,
                bias = "none",
                use_gradient_checkpointing = True,
                random_state = 3407,
                use_rslora = False,
                loftq_config = None,
            )

    return _model, _tokenizer
