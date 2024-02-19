from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.document_loaders import DirectoryLoader, PDFMinerLoader
from langchain.chains import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings

from dotenv import load_dotenv
import os


load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ["GOOGLE_CSE_ID"] = os.getenv('GOOGLE_CSE_ID')
os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

def chunk_and_index(texts):

    # we'll create chunks of 2000 tokens each, with the last 200 tokens of each chunk overlapping with the next to capture context a bit better
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000, chunk_overlap=200,
        add_start_index=True, separators = ['\n', '\\', '####']
    )

    docs = [x['page_content'] for x in texts]

    chunks = text_splitter.create_documents(docs)
    print(f"There are {len(chunks)} chunks")

    BGEembeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en",
                                             model_kwargs={"device": "cpu"},
                                             encode_kwargs={"normalize_embeddings": True})

    vectorstore = Chroma.from_documents(documents=chunks,
                                        embedding=BGEembeddings)

    print("Documents created and indexed to ChromaDB")

    # set up a retriver from the vector store
    # let's have it return the 10 chunk most similar (proxy for relevant) to the given a query.
    retriever = vectorstore.as_retriever(search_type="similarity",
                                        search_kwargs={"k": 10})

    return retriever