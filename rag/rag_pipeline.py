from ingestion.load_pdf import load_pdf_by_page
from ingestion.chunk_text import chunk_pages
from rag.vector_store import create_vector_store
from rag.rag_answer import format_context
from rag.build_prompt import build_prompt
from rag.llm_client import call_llm


# Build vector store once at startup
pages = load_pdf_by_page("data/Annual-Report-2024-25.pdf")
chunks = chunk_pages(pages)
collection = create_vector_store(chunks)

def answer_question(question: str) -> str:
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    context = format_context(docs, metas)
    prompt = build_prompt(question, context)

    response = call_llm(prompt)
    return response
