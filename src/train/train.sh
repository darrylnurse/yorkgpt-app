#!/bin/bash

python3 data/hf_upload_dataset.py

# make sure following script waits for dataset upload completion

python3 model/finetune.py

ollama create -f /app/src/train/output/model/Modelfile yorkgpt/yorkgpt

# might not be needed as we already added the public key
cat ~/.ollama/id_ed25519.pub

ollama push yorkgpt/yorkgpt