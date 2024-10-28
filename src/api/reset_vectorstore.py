from rag_data import rag_data
from vectorstore import get_vectorstore
from clear_vectors import clear_vectors

# this script will run once a day
# and will update the RAG with current events

def reset_vectorstore ():
    # pull current events from york website api
    docs = rag_data()

    # call the vectorstore, and upsert into database
    vectorstore = get_vectorstore()

    # clear all vectors from the previous day
    clear_vectors()

    # upsert vectors into database
    vectorstore.add_documents(docs, ids=[i for i, doc in enumerate(docs)])

    print('Vectorstore created successfully.')
