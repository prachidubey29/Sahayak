from ingestion.load_pdf import load_pdf_by_page
from ingestion.chunk_text import chunk_pages
from rag.vector_store import create_vector_store
from rag.rag_answer import format_context
from rag.build_prompt import build_prompt
from rag.llm_client import call_llm
from memory.redis_memory import save_message, format_history_for_prompt

pages = load_pdf_by_page("data/Annual-Report-2024-25.pdf")
chunks = chunk_pages(pages)
collection = create_vector_store(chunks)

def answer_question(question: str, session_id: str) -> str:
    history = format_history_for_prompt(session_id)

    results = collection.query(
        query_texts=[question],
        n_results=3
    )
    docs = results["documents"][0]
    metas = results["metadatas"][0]

    context = format_context(docs, metas)
    prompt = build_prompt(question, context, history)
    response = call_llm(prompt)

    save_message(session_id, "user", question)
    save_message(session_id, "assistant", response)

    return response