import os

def get_api_key(name):

    uppercase_name = name.upper()

    # get api key file
    api_key_file = os.getenv(f'{uppercase_name}_API_KEY_FILE', f'/run/secrets/{name}_api_key')
    
    # read secret from the file
    try:
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
        return api_key
    except FileNotFoundError:
        raise RuntimeError(f"API key file {api_key_file} not found.")
    

