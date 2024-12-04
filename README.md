# Prereqesuites
- Have a computer.
- Please have Docker installed. You can install Docker on your Machine [here](https://docs.docker.com/get-started/get-docker/).
- Have a computer with 16 or more (preferrably more) GB of memory. Having a GPU is even better.
- Get a Finegrained Huggingface Access Token [here](https://huggingface.co/settings/tokens). Finegrained means it has Read and Write access.
- You will also need a [Cohere Embeddings API Key](https://dashboard.cohere.com/api-keys).

# Installation
Pull the repo using ```git clone```.

You will need to create three files with these *exact* names:
- ```huggingface_token.txt```
- ```embedding_api_key.txt```

Place the Huggingface Token in ```huggingface_token.txt```.

Place the Cohere Embedding API Key in ```embedding_api_key.txt```.

Then, make sure your Docker Engine is started by opening your Docker Desktop. If not, you will get an Error saying: "Is the Docker Engine running?".

In the directory of the project, run ```docker compose up -d```.

Check the yorkgpt-server container and make sure the model is downloaded. It will say "100%" and success. 

When it says "Server is running on Port 3000.", you can make requests! Try:

```curl -X POST http://localhost:3000/yorkgpt -H "Content-Type: application/json" -d "{\"question\": \"Where is York College?\"}"```
