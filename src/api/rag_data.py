import requests
from datetime import datetime, timezone
from langchain_core.documents import Document

# call from @search endpoint
# get all events
# go to event endpoint
# check if event date > current date
# then add it to items

NUM_ENDPOINTS = 2500

def formatDate(iso_date: str) -> str:
        parsed_date = datetime.fromisoformat(iso_date)
        return parsed_date.strftime("%m %d, %Y at %I:%M %p")

def rag_data():

    url = f'https://www.york.cuny.edu/++api++/@search?fullobjects=1&b_size={NUM_ENDPOINTS}&portal_type=Event'

    event_docs = []
    current_date = datetime.now(timezone.utc)

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        if not response.headers.get('Content-Type') == 'application/json':
            raise Exception('Response was not JSON')
        
        data = response.json()
        items = data.get('items')
        for item in items:
            date_string = str(item['start'])
            given_date = datetime.fromisoformat(date_string)

            if given_date > current_date:
                doc = Document(
                        page_content = item['title'],
                        metadata = {
                        "description": item['description'],
                        "location": item['location'],
                        "start": formatDate(item['start']),
                        "end": formatDate(item['end'])
                        }
                )
                event_docs.append(doc)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
    
    return event_docs


