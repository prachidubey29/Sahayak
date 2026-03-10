from rag.rag_prompt import SYSTEM_PROMPT
def build_prompt(question: str, context: str) -> str:
    return f"""
{SYSTEM_PROMPT}
Context:
{context}
Question:
{question}
Answer:
"""
