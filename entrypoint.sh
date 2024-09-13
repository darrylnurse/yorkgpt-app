#!/bin/bash

echo 90 > /proc/sys/vm/swappiness

ollama serve &

# give ollama serve some time to take effect
sleep 5

echo 3 > /proc/sys/vm/drop_caches

ollama pull yorkgpt/yorkgpt

# clear disk cache
echo 3 > /proc/sys/vm/drop_caches

sleep 5

# exec node --max-old-space-size=12288 /app/server.mjs

ulimit -v 12582912 && exec python3 /app/server.py
