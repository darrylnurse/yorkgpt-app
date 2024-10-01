from rag_data import rag_data
from vectorstore import get_vectorstore

# this script will run once a day
# and will update the RAG with current events

def reset_vectors ():
    # pull current events from york website api
    docs = rag_data()

    # call the vectorstore, and upsert into database
    vectorstore = get_vectorstore()

    # clear all vectors from the previous day
    vectorstore.drop_tables()

    # upsert vectors into database
    vectorstore.add_documents(docs, ids=[i for i, doc in enumerate(docs)])


reset_vectors()