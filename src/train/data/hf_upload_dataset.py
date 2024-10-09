from datasets import Dataset
from dataset import create_dataset
import huggingface_hub

yorkgpt_data = create_dataset()

dataset = Dataset.from_list(yorkgpt_data)

dataset.push_to_hub("yorkgpt/yorkgpt")
huggingface_hub.create_tag("yorkgpt/yorkgpt", tag="1.0", repo_type="dataset")