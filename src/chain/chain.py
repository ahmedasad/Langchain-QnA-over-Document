from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from .. import config


class QAChain():
    def __init__(self):
        self.llm_model = llm_model = config.LLM_MODEL
        self.chat = ChatOpenAI(
            # Temperature is used to control the randomness of generation
            temperature=0.3, model=llm_model, openai_api_key=config.OPENAI_API_KEY)        
        self.promp_template = """You are a teacher having conversation with student.
                        You will be given some knowledge as context and check if the given knowledge answers the question then explain the answer to the question specific in summarized format
                        otherwise tell the user that you don't have knowledge in book.

{context}

{chat_history}

Human: {question}
teacher:
"""
        self.prompt = PromptTemplate(input_variables=["chat_history", "question", "context"],template=self.promp_template)
        self.memory = ConversationBufferMemory(memory_key="chat_history", input_key="question")
        self.chain = load_qa_chain(llm=self.chat,                                              
                                              chain_type="stuff",
                                              memory= self.memory,
                                              prompt = self.prompt, 
                                              verbose=True)

    def invoke_chain(self, documents, query):
        result = self.chain.invoke({"input_documents": documents, "question":query},return_onty_outputs=True)
        return result['output_text']