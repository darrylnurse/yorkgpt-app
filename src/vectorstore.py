from langchain_cohere import CohereEmbeddings
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
from rag_data import rag_data

# lets start by connecting to the vector database container
connection = "postgresql+psycopg://rag:langchain@vectordb:5432/vectordb" 
embeddings = CohereEmbeddings(
    cohere_api_key='8mVqopwItZuTkLhfLY6LtMsBOajqYD9ECn9rSkuh',
    model="embed-english-light-v3.0"
)

# initialize database
vectorstore = PGVector(
    embeddings=embeddings,
    collection_name="rag_data",
    connection=connection,
    use_jsonb=True,
)

# pull current events from york website api and upsert to database
docs = rag_data()
vectorstore.add_documents(docs, ids=[i for i, doc in enumerate(docs)])

