# For Fast API
from fastapi import FastAPI, HTTPException

# Maps API
import requests, json, os
from dotenv import load_dotenv
load_dotenv()

# OpenAI
import numpy as np
import pandas as pd
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.conversation.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain

app = FastAPI()

@app.get("/")
async def docs_redirect():
    return Response("Opening the docs UI", status_code=302, headers={"location": "/docs"})

# Define the places to hold
@app.get("/greet")
def greet():
    return {"Welcome to the first API version!"}
