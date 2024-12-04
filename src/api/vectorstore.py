from langchain_cohere import CohereEmbeddings
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
from get_key import get_key

# global vectorstore variable
_vectorstore = None

db_connection_string = 'postgresql+psycopg://rag:langchain@vectordb:5432/vectordb'

# the vectorstore is only created when needed
def get_vectorstore():
    try:
        global _vectorstore
        if _vectorstore is None:
            # initialize database options
            connection = db_connection_string
            embeddings = CohereEmbeddings(
                cohere_api_key = get_key('embedding_api_key'),
                model = "embed-english-light-v3.0"
            )
            
            _vectorstore = PGVector(
                embeddings = embeddings,
                collection_name = "rag_data",
                connection = connection,
                use_jsonb = True,
            )

            _vectorstore.create_vector_extension()
            _vectorstore.create_tables_if_not_exists()
        
            print('Vectorstore created successfully.')
            
        return _vectorstore
    except:
        print('Vectorstore creation failed.')


