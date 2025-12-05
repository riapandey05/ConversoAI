# import streamlit as st
# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

# import os
# from dotenv import load_dotenv
# load_dotenv()

# # langchain tracking
# # os.environ["LANGCHAIN_TRACKING_V2"] = os.getenv("LANGCHAIN_API_KEY")
# # os.environ["LANGCHAIN_TRACKING_V2"]="true"
# # os.environ["LANGCHAIN_PROJECT"] = "ConversoAI"



# # prompt template
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system","You are a helpful assistant.Please response to the user queries"),
#         ("user","Question:{question}")
#     ]
# )

# def generate_reponse(question,api_key,llm,temperature,max_tokens):
#     if not api_key:
#         st.error("Please enter a valid Groq API Key in the sidebar.")
#         return ""
#     api_key=api_key
#     llm = ChatGroq(model=llm)
#     output_parser = StrOutputParser()
#     chain = prompt|llm|output_parser
#     answer = chain.invoke({"question": question})
#     temperature=temperature
#     max_tokens=max_tokens
#     return answer

# # Let us build the web app now
# st.title("ConversoAI - Chat with LLMs")
# api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

# # drop down to select various models
# llm = st.sidebar.selectbox(
#     "Select LLM Model",
#     ("groq/compound","groq/compound-mini")
# )
# temperature = st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.7)
# max_tokens = st.sidebar.slider("Select Max Tokens", 50, 300, 150)

# st.write("## Ask a question to the LLM")
# user_input = st.text_input("You:")

# if user_input:
#     response = generate_reponse(user_input,api_key,llm,temperature,max_tokens)
#     st.write("### Response from LLM:")
#     st.write(response)
# else:
#     st.write("Please enter a question to get a response.")


import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}"),
    ]
)


def generate_reponse(question, api_key, model_name, temperature, max_tokens):
    if not api_key:
        return "Please enter your Groq API Key in the sidebar."

    llm = ChatGroq(
        api_key=api_key,          # 👈 IMPORTANT
        model=model_name,         # or model_name="..."
        temperature=temperature,
        max_tokens=max_tokens,
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer


# ----- Streamlit UI -----

st.title("ConversoAI - Chat with LLMs")

api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

llm = st.sidebar.selectbox(
    "Select LLM Model",
    (
        # use real Groq model IDs; e.g.:
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
    ),
)

temperature = st.sidebar.slider("Select Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Select Max Tokens", 50, 300, 150)

st.write("## Ask a question to the LLM")
user_input = st.text_input("You:")

if user_input:
    response = generate_reponse(user_input, api_key, llm, temperature, max_tokens)
    st.write("### Response from LLM:")
    st.write(response)
else:
    st.write("Please enter a question to get a response.")
