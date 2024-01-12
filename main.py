from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(find_dotenv())

llm = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Richard Feynman, teaching science. People from all ages and background should understand the "
               "topics clearly."),
    ("user", "{input}"),
])
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

response = chain.invoke({"input": "why is the sky blue?"})
print(response)
