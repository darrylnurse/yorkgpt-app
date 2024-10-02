import requests
from langchain_core.documents import Document

def rag_data():
    base_url = "https://www.york.cuny.edu/++api++/events"
    def fetch(url):
        response = requests.get(url)
        data = response.json()
        return data

    items = fetch(base_url).get('items', [])

    # the first item is just metadata
    events=items[1:len(items)]

    # turn each url into the api version
    def apifyUrl(url):
        return url.replace('/events', "/++api++/events")

    # we need all the urls to get data from
    event_urls = []
    for event in events:
        event_url = event['@id']
        event_urls.append(apifyUrl(event_url))

    # visit each url to extract metadata:
    # title, description, datetime, and location
    event_docs = []
    for event_url in event_urls:
        event_info = {}
        data = fetch(event_url)
        event_info['description'] = data.get('description')
        event_info['location'] = data.get('location')
        doc = Document(
            page_content=data.get('title'),
            metadata=event_info
        )
        event_docs.append(doc)

    return event_docs


