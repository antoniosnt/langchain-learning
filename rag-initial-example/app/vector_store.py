from pathlib import Path

import pandas as pd
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "pizza_reviews.csv"
DB_PATH = PROJECT_ROOT / "chroma_langchain_db"

embeddings = OllamaEmbeddings(model="qwen3-embedding")
vector_store = Chroma(
    collection_name="pizza_reviews",
    persist_directory=str(DB_PATH),
    embedding_function=embeddings,
)

# Load the CSV the first time this collection is created.
if not vector_store.get()["ids"]:
    df = pd.read_csv(DATA_PATH)
    documents = []
    ids = []

    for _, row in df.iterrows():
        review_id = str(row["review_id"])
        documents.append(
            Document(
                page_content=f"{row['restaurant']}: {row['review_text']}",
                metadata={
                    "review_id": review_id,
                    "rating": int(row["rating"]),
                    "date": str(row["date"]),
                },
                id=review_id,
            )
        )
        ids.append(review_id)

    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
