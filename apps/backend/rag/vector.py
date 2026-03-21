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

load_dotenv()

current_dir = Path(__file__).parent
docs_path = current_dir / "docs"
db_path = current_dir / "chrome_db"
print(f"Docs path: {docs_path}, ChromaDB path: {db_path}")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

add_documents = False if os.path.exists(db_path) else True

if add_documents:
    loader = DirectoryLoader(
        path=docs_path,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True,
    )

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    chunks = splitter.split_documents(docs)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="knowledge-base",
        persist_directory=db_path,
    )

    print(f"Loaded {len(chunks)} chunks to Chroma")
else:
    print("Did not load any document to Chroma. Chroma already created")
    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_path,
        embedding_function=embeddings,
    )

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
