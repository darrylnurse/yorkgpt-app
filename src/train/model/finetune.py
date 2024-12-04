from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported
from model_init import get_model_and_tokenizer, max_seq_length
from import_dataset import import_dataset
from get_key import get_key

model, tokenizer = get_model_and_tokenizer()

dataset = import_dataset()

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False,
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 60,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "../output",
    ),
)

trainer_stats = trainer.train()

print(f"{trainer_stats.metrics['train_runtime']} seconds used for training.")
print(f"{round(trainer_stats.metrics['train_runtime']/60, 2)} minutes used for training.")

# save model locally
model.save_pretrained_gguf("../output/model", tokenizer, quantization_method = "f16")

# save model to huggingface
model.push_to_hub_gguf(
        "darrylnurse/yorkgpt", 
        tokenizer,
        quantization_method = ["q4_k_m", "q8_0", "q5_k_m",],
        token = get_key('huggingface_token')
    )