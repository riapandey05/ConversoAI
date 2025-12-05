import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

# langchain tracking
os.environ["LANGCHAIN_TRACKING_V2"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]=True
os.environ["LANGCHAIN_PROJECT"] = "ConversoAI"


# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_reponse(question,api_key,llm,temperature,max_tokens):
    ChatGroq.groq_api_key=api_key
    llm = ChatGroq(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question": question})


