from website_text import get_text_data
from data_helpers import DataHelper
import requests
import json
import time

api_url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

def create_payload(text, context): # currently, context param is unused (format of response json skews the models output format)
  return {
      "model": "llama3.1:8b",
      "prompt": f"""
      For the given text, which is an answer, please generate an appropriate question to match the text, always in the following JSON format, also known as the ShareGPT format:
      {{ "conversations": [ {{ "from": "human", "value": "<insert question here>" }}, {{ "from": "gpt", "value": "{text}" }} ] }}
      Do not deviate from this format when constructing your response.

      The text is: {text}. This text is the answer to the question you generate, and was taken from the CUNY York College Website.
      Please generate a question that an Undergraduate College Student would ask, and is closely related to the associated text.
      
      The following are some questions to help generate the response:
      1. What kind of question could this answer respond to?
      2. Is there a broader topic in the context that should shape the question?
      3. Does the answer contain specific details that might encourage a more targeted or clarifying question?

      Example:
      Text: 'York College offers financial aid through a variety of grants, scholarships, and federal work-study programs.'
      Response: {{ "conversations": [ {{ "from": "human", "value": "What types of financial aid does York College offer?" }}, {{ "from": "gpt", "value": "York College offers financial aid through a variety of grants, scholarships, and federal work-study programs.'" }} ] }}
      """,
      "stream": False,
      "options": {
          "temperature": 0.1, # we want out output to be more factual than creative
          "seed": 26 # this param makes the model generate the same output for the same input more often
      },
      "format": "json"
  }

def create_dataset():
    text_data = get_text_data()

    dataset = []
    rate_limit_seconds = 2
    text_data_length = len(text_data)
    for index, data in enumerate(text_data):
        payload = create_payload(data['text'], data['context'])

        response = requests.post(api_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            model_response = json.loads(response._content)
            datapoint = json.loads(model_response['response'])
            print(f'{index + 1}/{text_data_length}', datapoint)
            dataset.append(datapoint)

        else:
            print(f"Error {response.status_code}: {response.text}")
            break

        time.sleep(rate_limit_seconds)

    return data