FROM ubuntu:22.04

ENV OLLAMA_HOST=http://0.0.0.0:11434
ENV OLLAMA_KEEP_ALIVE=24h
ENV OLLAMA_INTEL_GPU=true
ENV OLLAMA_MAX_LOADED_MODELS=2
ENV OLLAMA_MODELS=/root/.ollama/models

WORKDIR /app

# install curl, python3, python package installer, cron and dos2unix (used to change file from CRLF to LF)
RUN apt-get update \
    && apt-get install -y curl python3 python3-pip cron dos2unix \
    && apt-get clean 

# install ollama
RUN curl -fsSL https://ollama.com/install.sh | OLLAMA_VERSION=0.3.13 sh

# copy files into app
COPY /src /app/src

# install python packages
RUN pip3 install --upgrade pip \
    && pip3 install -r /app/src/api/api_requirements.txt 

# install the train requirements this way because they are more complex
RUN chmod +x /app/src/train/train_requirements.sh
RUN /app/src/train/train_requirements.sh 

# copy cron file to the cronjob directory
ADD /src/cronjobs /etc/cronjobs

# for the cron file, there must be an empty line at the end of the file (LF)
RUN dos2unix /etc/cronjobs

# make sure the cron job file has executable permissions
RUN chmod 0644 /etc/cronjobs

# apply the cron job
RUN crontab /etc/cronjobs
    
EXPOSE 3000

RUN chmod +x /app/src/entrypoint.sh

ENTRYPOINT ["sh", "/app/src/entrypoint.sh"]