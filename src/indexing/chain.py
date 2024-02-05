from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from .database_remote import Database
import config


class QAChain():
    def __init__(self):
        self.llm_model = llm_model = config.LLM_MODEL
        self.database = Database()
        self.chat = ChatOpenAI(
            # Temperature is used to control the randomness of generation
            temperature=0.0, model=llm_model, openai_api_key=config.OPENAI_API_KEY)
        self.promp_template = """You are a teacher having conversation with student.\
            Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. \
                otherwise tell the student that you don't have this knowledge in book.

Human: {question}
{context}
teacher:
"""
        self.prompt = PromptTemplate.from_template(template=self.promp_template)
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", input_key="question")
        self.chain = RetrievalQA.from_chain_type(llm=self.chat,
                                                 chain_type="stuff",
                                                #  memory=self.memory,
                                               return_source_documents=True,
                                               retriever = self.database.langchain_chroma.as_retriever(),
                                                 chain_type_kwargs={
                                                     "prompt": self.prompt},
                                                 verbose=True
                                                 )

    def invoke_chain(self, query):
        result = self.chain({"query": query})
        print("CHAIN RESULT: ", result)
        return result["result"]
