from typing import List
import chromadb
from langchain_core.documents.base import Document


class Database(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Database,cls).__new__(cls)
        return cls.instance
            
    def __init__(self):
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.get_or_create_collection(name="itcs_book_2024")

    def add_data_into_collection(self,embeddings,documents:List[str]):
        """Add new data into db in new or existing collection.

        Args:
            embeddings: Vector values of documents.
            documents: list of strings
            
        Returns:
            This function returns nothing
        """
        
        # Mock Ids and metadata (HAS TO BE IMPLEMENTED AS PER STANDARDS)
        ids = [f"id{i}" for i in range(1,len(documents)+1)]
        metaData = [{"source": "my_source"} for i in range(1,len(documents)+1)]
        
        self.collection.add(ids=ids,embeddings=embeddings,documents=documents,metadatas=metaData)
        
    def query_data(self, query:str,embedding):
        """Retrieve data from Database

        Args:
            query: strings
            embedding: Vector values of query string.
            
        Returns:
            the response object from Chroma DB
        """
        
        result = self.collection.query(query_embeddings=[embedding],n_results=1)
        print(f"Response from db:\n {result}")