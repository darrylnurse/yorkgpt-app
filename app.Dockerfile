FROM ubuntu:22.04

WORKDIR /app

# install curl, python3, python package installer, cron and dos2unix (used to change file from CRLF to LF)
RUN apt-get update \
    && apt-get install -y curl python3 python3-pip cron dos2unix \
    && apt-get clean 

# install ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# copy files into app
COPY /src /app/src

# install python packages
RUN pip3 install --upgrade pip \
    && pip3 install -r /app/src/requirements/app_requirements.txt \
    && pip3 install -r /app/src/requirements/train_requirements.txt

RUN chmod +x 

# copy cron file to the cronjob directory
ADD /src/cronjobs /etc/cronjobs

# for the cron file, there must be an empty line at the end of the file (LF)
RUN dos2unix /etc/cronjobs

# make sure the cron job file has executable permissions
RUN chmod 0644 /etc/cronjobs

# apply the cron job
RUN crontab /etc/cronjobs
    
EXPOSE 3000

ENTRYPOINT ["/app/src/entrypoint.sh"]