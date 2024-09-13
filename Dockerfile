FROM ubuntu:22.04

WORKDIR /app

# install curl, python3, and python package installer
RUN apt-get update \
    && apt-get install -y curl python3 python3-pip \
    && apt-get clean 

# install ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

COPY . /app

# install pip requirements
RUN pip3 install --upgrade pip \
    && pip3 install -r /app/requirements.txt

# install node version 18.*
# RUN curl -sL https://deb.nodesource.com/setup_18.x -o /tmp/nodesource_setup.sh \ 
#     && bash /tmp/nodesource_setup.sh \
#     && apt-get install -y nodejs \
#     && node -v

# install node packages
# RUN --mount=type=bind,source=package.json,target=package.json \
#     --mount=type=bind,source=package-lock.json,target=package-lock.json \
#     --mount=type=cache,target=/root/.npm \
#     npm ci --omit=dev

EXPOSE 3000

ENTRYPOINT ["/app/entrypoint.sh"]