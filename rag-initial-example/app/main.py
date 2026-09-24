from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from app.vector_store import retriever


def main():
    model = OllamaLLM(model="qwen2.5")
    prompt = ChatPromptTemplate.from_template(
        """You answer questions about a pizza restaurant using customer reviews.

Relevant reviews:
{reviews}

Question: {question}

Answer from the reviews. If they do not contain enough information, say so."""
    )
    chain = prompt | model

    while True:
        question = input("Ask your question (q to quit): ").strip()
        if question.lower() in {"q", "quit"}:
            break

        reviews = retriever.invoke(question)
        context = "\n\n".join(document.page_content for document in reviews)
        answer = chain.invoke({"reviews": context, "question": question})
        print(f"\n{answer}\n")


if __name__ == "__main__":
    main()
