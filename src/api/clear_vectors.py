from sqlalchemy.orm import Session
from sqlalchemy import text, inspect
from vectorstore import get_vectorstore

# unfortunately Langchain Postgress doesnt have a way to clear all the vectors in a collection without deleting said collection
# so we must use a separate orm
def clear_vectors():
    vectorstore = get_vectorstore()

    # open a session for the vectorstore connection
    with Session(vectorstore._engine) as session:

        # we have to check if the collection exists first before attampting to clear it
        inspector = inspect(vectorstore._engine)

        if vectorstore.collection_name not in inspector.get_table_names():
            print(f"Collection '{vectorstore.collection_name}' does not exist, and thus will be created.")
            
            # recreate the table 
            vectorstore.create_tables_if_not_exists()
        else:
            print(f"Collection '{vectorstore.collection_name}' exists, clearing vectors.")

            # delete all vectors in the vectorstore collection
            session.execute(text(f"DELETE FROM {vectorstore.collection_name};"))

            # commit the changes to save them
            session.commit()