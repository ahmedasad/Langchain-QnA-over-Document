
from src.chain.chain import QAChain
from typing import List
from src.indexing.database_remote import Database
from src.indexing.embedding import EmbeddingUtility
from src.indexing.load_document import LoadDocument

class Main():
    """
    This class initiate backend of the app

    """

    def __init__(self):
        """
        First it will initiate the DB and check if collection and data doesnot exist then it will:
        - Create collections
        - Load documents 
        - Create embedding
        - Then store data and embeddings in collections
        """
        self.database = Database()
        self.embeddings = EmbeddingUtility()
        self.chain = QAChain()

        self.database.get_or_create_colletion()
        if not self.check_if_data_exist():

            loaded_document_chunks = self.load_documents()

            print(f"Total Document length is {len(loaded_document_chunks)}")
            text_doc_list = [
                text.page_content for text in loaded_document_chunks]

            embeddings = self.create_embeddings(text_doc_list)

            self.store_data_and_embeddings(embeddings, text_doc_list)

    def check_if_data_exist(self):
        """
        This functions checks the count of items in the collection 

        return: if 0 then Falst otherwise True
        """
        result = False if self.database.get_colletion_items_count() == 0 else True
        print("IF DB EXIST OR NOT: ", result)
        return result

    def load_documents(self):
        """
        This function load the documents and also create the CHUNKS

        return: List of Documents 
        """
        document_loader = LoadDocument('./data')
        return document_loader.load_pdf_files_and_chunks()

    def create_embeddings(self, text_doc_list: List[str]):
        """
        This function create the embeddings against the list provided

        args: text_doc_list: List[str]

        return: embeddings of list of documents:str
        """
        return self.embeddings.embed_list_of_documents(text_doc_list)

    def store_data_and_embeddings(self, embeddings, text_document_list):
        """
        This functions stores embeddings and list of strings in collections.

        args: embeddings:List[float]
              text_document_list: List[str]

        """
        self.database.add_data_into_collection(embeddings, text_document_list)

    def get_documents_from_db(self, query):
        """
        This functions process query and perform query on DB

        args: query:str
        """
        
        retrieve_docs = self.database.query_data(
            query)
        return retrieve_docs
        
    
    def invoke_chain(self,documents,query):
        self.chain.invoke_chain(documents,query)

    def process_query(self,query: str):
        """
        This function Simply fetch the data from docuemnts and pass into chain with query

        args: Query: str

        return: returns response from chain
        """
        
        documents = self.get_documents_from_db(query)
        return self.invoke_chain(documents,query)
        
m = Main()

# m.database.chroma_client.delete_collection(m.database.collection_name)


# query = "When Did book, Introduction to Computer Science, was published"
# docs = m.process_query(query)
# m.invoke_chain(docs,query)
# query = "who is shahid afridi."
# docs = m.process_query(query)
# m.start_chain(docs,query)