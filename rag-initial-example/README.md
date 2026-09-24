# Local Ollama RAG practice

A small local RAG example that retrieves relevant pizza reviews from ChromaDB and uses Ollama to answer questions.

## Project layout

- `app/main.py` runs the interactive question and answer loop.
- `app/vector_store.py` loads review data, creates embeddings, and configures ChromaDB retrieval.
- `data/pizza_reviews.csv` contains the practice reviews.
- `chroma_langchain_db/` is generated locally and ignored by Git.

## Run

From this directory, make sure Ollama is running and the `qwen2.5` and `qwen3-embedding` models are available. Then run:

```bash
uv run python -m app.main
```
