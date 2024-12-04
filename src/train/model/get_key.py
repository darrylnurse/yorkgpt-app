import os

def get_key(name):

    # get api key file
    api_key_file = os.getenv(f'{name}', f'/run/secrets/{name}')
    
    # read secret from the file
    try:
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
        return api_key
    except FileNotFoundError:
        raise RuntimeError(f"API key file {api_key_file} not found.")