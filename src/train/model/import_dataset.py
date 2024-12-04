from unsloth.chat_templates import get_chat_template
from model_init import get_model_and_tokenizer
from datasets import load_dataset

def import_dataset():
    model, tokenizer = get_model_and_tokenizer()

    tokenizer = get_chat_template(
        tokenizer,
        chat_template = "phi-3",
        mapping = {"role" : "from", "content" : "value", "user" : "human", "assistant" : "gpt"},
    )

    def formatting_prompts_func(examples):
        convos = examples["conversations"]
        texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
        return { "text" : texts, }
    pass

    dataset = load_dataset("darrylnurse/york-share-gpt", split = "train")
    return dataset.map(formatting_prompts_func, batched = True,)