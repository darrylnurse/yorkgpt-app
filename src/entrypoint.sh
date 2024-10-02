#!/bin/bash

# increase system swappiness
echo 90 > /proc/sys/vm/swappiness

# start ollama
ollama serve &

# give ollama serve some time to take effect
sleep 5

# manually clear cache
echo 3 > /proc/sys/vm/drop_caches

# pull model
ollama pull yorkgpt/yorkgpt

# clear disk cache
echo 3 > /proc/sys/vm/drop_caches

sleep 5

cron -f -l 2

# increase process memory limit to 12GB and start server
ulimit -v 12582912 && exec python3 /app/src/api/server.py
