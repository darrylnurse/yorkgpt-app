#!/bin/bash

# make sure dependencies are installed in order
# unsloth requires torch

pip install torch requests datasets huggingface-hub wheel ninja setuptools
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install xformers --no-dependencies --no-build-isolation
pip install "trl<0.9.0" peft accelerate bitsandbytes