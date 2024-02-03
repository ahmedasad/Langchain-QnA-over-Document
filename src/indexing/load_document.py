from typing import List
from langchain.document_loaders.text import TextLoader
from langchain.document_loaders.directory import DirectoryLoader
from langchain.document_loaders.pdf import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


'''
    - Class written to Load either PDF or Txt documents
    - It takes directory and go through the whole directory
    - it can also accept the pdf urls
    - It does accept text splitting models
'''


class LoadDocument():
    def __init__(self, directory, text_splitter=RecursiveCharacterTextSplitter()):
        self.directory = directory
        self.text_splitter = text_splitter

    def load_text_file(self) -> List[Document]:
        docs = DirectoryLoader(
            self.directory, glob="**/*txt", loader_cls=TextLoader, show_progress=True)
        return docs.load_and_split(self.text_splitter)

    def load_pdf_files_and_chunks(self) -> List[Document]:
        docs = DirectoryLoader(
            self.directory, glob="**/*pdf", loader_cls=PyPDFLoader, show_progress=True)
        return docs.load_and_split(self.text_splitter)

    def load_file_from_url(self):
        PyPDFLoader("example_data/layout-parser-paper.pdf").load_and_split()
        
        PyPDFLoader
        pass
