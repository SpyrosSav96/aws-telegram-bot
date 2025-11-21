from locale import LC_MONETARY
from langchain_core import embeddings
from langchain_core.tools import create_retriever_tool, retriever
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from functools import lru_cache

from aws_telegram_bot.config import settings
from aws_telegram_bot.infrastructure.clients.qdrant import get_qdrant_client

@lru_cache(maxsize=1)
def get_retrieval_tool():
    embeddings = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL, api_key=settings.OPENAI_API_KEY)

    vector_store = QdrantVectorStore(
        client=get_qdrant_client(),
        collection_name="aws_telegram_bot_collection",
        embedding=embeddings
    )

    retriever = vector_store.as_retriever()

    retriever_tool = create_retriever_tool(
        retriever=retriever,
        name="retrieve_aws_telegram_bot_information_tool",
        description="Retrieve information about the Telegram Agents backgroung, academic journey, professional experience, major projects, philosophy, values, hobbies and personal interests"
    )

    return retriever_tool