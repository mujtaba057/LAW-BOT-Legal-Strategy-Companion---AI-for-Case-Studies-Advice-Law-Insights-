import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS 
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from dotenv import load_dotenv
import os





def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        Pdf_reader = PdfReader(pdf)
        for page in Pdf_reader.pages:
            
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
        
    )
    return conversation_chain


def handle_userinput(user_question):

    response = st.session_state.conversation({'question': user_question})
 
    system_message = "You're a very knowledgeable in indian constitution,  who provides accurate and eloquent answers to law related questions and give  defensive statements for particular case only."

    # st.write(response)
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    system_message = "You're a very knowledgeable in indian constitution,  who provides accurate and eloquent answers to law related questions and give  defensive statements for particular case only."
    st.set_page_config(page_title="Legal Minds", page_icon=":Judge:")
    
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = None

    st.header("Legal Strategy Companion - AI for Case Studies Advice & Law Insights :books:")
    user_question = st.text_input("Ask a question about your Case Studies documents:")
    
    if user_question:
        handle_userinput(user_question)

    # st.write(user_template.replace("{{MSG}}","Hello robot"), unsafe_allow_html=True)
    # st.write(bot_template.replace("{{MSG}}","Hello Human"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Case documents")
        pdf_docs =  st.file_uploader("upload your Case PDF here and click on:books: 'Studies Case documents'",accept_multiple_files=True)
        if st.button("Studies Case documents"):
           with st.spinner("Processing"):
               raw_text = get_pdf_text(pdf_docs)
            #    st.write(raw_text) 


               text_chunks = get_text_chunks(raw_text)
            #    st.write(text_chunks) 

               vectorstore = get_vectorstore(text_chunks)
               
               st.session_state.conversation = get_conversation_chain(vectorstore)

    # st.session_state.conversation        
if __name__ == '__main__':
    main()
