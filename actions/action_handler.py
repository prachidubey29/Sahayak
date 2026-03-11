from actions.action_prompt import ACTION_SYSTEM_PROMPT
from rag.llm_client import call_llm
from memory.redis_memory import save_message, format_history_for_prompt

def handle_action(user_input: str, session_id: str = None) -> str:
    # Fetch memory context if session_id provided
    history = ""
    if session_id:
        history = format_history_for_prompt(session_id)

    prompt = f"""
{ACTION_SYSTEM_PROMPT}

{history}
User Request:
{user_input}

JSON:
"""
    response = call_llm(prompt)

    # Save to Redis memory if session_id provided
    if session_id:
        save_message(session_id, "user", user_input)
        save_message(session_id, "assistant", response)

    return response