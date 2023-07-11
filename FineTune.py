from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()

import llama_index
import os
from llama_index import (
    GPTKeywordTableIndex,
    SimpleDirectoryReader,
    LLMPredictor,
    ServiceContext
)

from llama_index import GPTVectorStoreIndex
from langchain.llms import OpenAI


documents = SimpleDirectoryReader('data').load_data()

# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(model_name='text-davinci-003', temperature=0, max_tokens=256))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
#service_context = ServiceContext.from_defaults()


# build index
index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
query_engine = index.as_query_engine()
#query = input("Enter your query: ")
#response = query_engine.query(query)
#print(response)

 
# Get input from the user 
while True: 
    inp = input("Enter a query (enter 'q' to quit): ") 
    if inp == 'q': 
        break 
    #inputs.append(inp) 
    response = query_engine.query(inp)
    print(response)