from langchain_cohere import CohereEmbeddings
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
from reset_vectors import reset_vectors
from get_key import get_api_key

# global vectorstore variable
_vectorstore = None

# the vectorstore is only created when needed
def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        # initialize database options
        connection = "postgresql+psycopg://rag:langchain@vectordb:5432/vectordb"
        embeddings = CohereEmbeddings(
            cohere_api_key=get_api_key('embedding'),
            model="embed-english-light-v3.0"
        )
        
        _vectorstore = PGVector(
            embeddings=embeddings,
            collection_name="rag_data",
            connection=connection,
            use_jsonb=True,
        )

        # create vectors in the database
        reset_vectors()

    return _vectorstore


