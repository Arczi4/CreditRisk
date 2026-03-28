import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

from app.core.logging_config import get_logger

load_dotenv()

logger = get_logger(__name__)


class RetrieverService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        self.current_dir = Path(__file__).parent
        self.docs_path = self.current_dir / "docs"
        self.db_path = self.current_dir / "chrome_db"
        self.collection_name = "knowledge-base"

        # TODO: store it in config
        self.chunk_size = 1000
        self.chunk_overlap = 200
        self.search_kwargs = 5

        self.add_documents = False if os.path.exists(self.db_path) else True
        self.vector_store = self.__setup_chroma()

    def __setup_chroma(self) -> Chroma:
        if self.add_documents:
            loader = DirectoryLoader(
                path=self.docs_path,
                glob="**/*.md",
                loader_cls=TextLoader,
                loader_kwargs={"encoding": "utf-8"},
                show_progress=True,
            )

            docs = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap,
                add_start_index=True,
            )
            chunks = splitter.split_documents(docs)

            logger.info(f"Loaded {len(chunks)} chunks to Chroma")

            return Chroma.from_documents(
                documents=chunks,
                collection_name=self.collection_name,
                embedding=self.embeddings,
                persist_directory=self.db_path,
            )
        else:
            logger.info("Chroma already created. Did not load any document to Chroma.")
            return Chroma(
                collection_name=self.collection_name,
                embedding_function=self.embeddings,
                persist_directory=self.db_path,
            )

    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs={"k": self.search_kwargs})


retriever_service = RetrieverService()
