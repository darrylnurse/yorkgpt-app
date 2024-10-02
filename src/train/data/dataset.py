from website_text import get_text_data
import requests
import json
import time
import os

api_url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

def create_payload(text):
  return {
      "model": "llama3.1:8b",
      "prompt": f"""For the given text, which is an answer, please generate an appropriate question to match the text, in the following JSON format, also known as the ShareGPT format:
      {{ \"conversations\": [ {{ \"from\": \"human\", \"value\": \"<insert question here>\" }}, {{ \"from\": \"gpt\", \"value\": \"{text}\" }} ] }}
      The text is: {text}.
      Please generate a question that an Undergraduate College Student would ask, and is related to the associated text.""",
      "stream": False,
      "options": {
          "temperature": 0.1, # we want out output to be more factual than creative
          "seed": 26 # this param makes the model generate the same output for the same input more often
      },
      "format": "json"
  }

text_data = get_text_data()

data = []
rate_limit_seconds = 2
text_data_length = len(text_data)
for index, text in enumerate(text_data):
  payload = create_payload(text)

  response = requests.post(api_url, headers=headers, data=json.dumps(payload))

  if response.status_code == 200:
      model_response = json.loads(response._content)
      datapoint = json.loads(model_response['response'])
      print(f'{index + 1}/{text_data_length}', datapoint)
      data.append(datapoint)

  else:
      print(f"Error {response.status_code}: {response.text}")
      break

  time.sleep(rate_limit_seconds)

file_name = 'yorkgpt-dataset.json'
dir_path = os.path.dirname(os.path.realpath(__file__))
output_path = os.path.join(dir_path, file_name)
with open (output_path, 'w') as file:
  json.dump(data, file)