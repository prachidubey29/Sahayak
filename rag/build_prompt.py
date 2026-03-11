from rag.rag_prompt import SYSTEM_PROMPT

def build_prompt(question: str, context: str, history: str = "") -> str:
    return f"""
{SYSTEM_PROMPT}

{history}
Context:
{context}

Question:
{question}

Answer:
"""