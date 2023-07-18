import os
import pinecone

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone


class PineconeClient:
    def docsearch():
        # Set pinecone credentials
        PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
        PINECONE_ENVIRONMENT = os.environ["PINECONE_ENVIRONMENT"]

        # load documents and split them.
        loader = TextLoader("domain/source_knowledge/savings_accounts.txt")
        documents = loader.load()

        # Segment the documents and generate their embeddings.
        text_splitter = CharacterTextSplitter(chunk_size=3000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()

        # initialize pinecone
        pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

        index_name = "savings-accounts"

        # Store the documents and embeddings in the pinecone vectorstore.
        index_name = "savings-accounts"
        docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

        return docsearch
