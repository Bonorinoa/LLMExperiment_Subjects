
from langchain_community.tools import Tool
from langchain_community.utilities import GoogleSearchAPIWrapper

from dotenv import load_dotenv
import os

import html2text
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncHtmlLoader

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ["GOOGLE_CSE_ID"] = os.getenv('GOOGLE_CSE_ID')
os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

async def do_webscraping(link):
    '''
    Function to search a link asynchronously. Returns a JSON load with extracted HTML objects parsed from each link.
    Parameters
        link: A single url to search. We pass several link in a loop so that we can do it async
    Returns:
        doc: A JSON (python dictionary) object with relevant information parsed from the HTML scraped from the link.
    '''
    try:
        urls = [link]
        loader = AsyncHtmlLoader(urls)
        docs = loader.load()

        html2text_transformer = Html2TextTransformer()
        docs_transformed = html2text_transformer.transform_documents(docs)

        if docs_transformed != None and len(docs_transformed) > 0:
            metadata = docs_transformed[0].metadata
            title = metadata.get('title', '')
            content = docs_transformed[0].page_content

            doc = {
                    'title': title,
                    'metadata': metadata,
                    'page_content': html2text.html2text(content)
                }
            return doc
        else:
            return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def search_tool():
    search = GoogleSearchAPIWrapper()

    # k has to be a default parameter so we can build a tool with it. Change to get more or less sources
    def topk_results(query, k=5):
        return search.results(query, k)

    # alternatively, we can just use search.run and retrieve the first result from a google search given query
    # But using search.results gives us access to the link
    tool_sources = Tool(
        name="Google Search Sources",
        description="Search Google for recent results and information relevant to user query.",
        func=topk_results,
    )

    return tool_sources

async def get_results2(prompt):

    results = search_tool().run(prompt)

    structured_response = []

    for link in [result['link'] for result in results]:
        print(link)
        response = await do_webscraping(link)
        if response != None:
            structured_response.append(response)

    return structured_response

async def get_results(prompt):
    return "Test"


