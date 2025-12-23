from langchain.memory import VectorStoreRetrieverMemory
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings

def create_shared_memory():
    embeddings = FakeEmbeddings(size=768)
    vectorstore = FAISS.from_texts(
        ["Initial shared memory"], embedding=embeddings
    )

    return VectorStoreRetrieverMemory(
        retriever=vectorstore.as_retriever()
    )
