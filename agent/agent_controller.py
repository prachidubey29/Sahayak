from rag.rag_pipeline import answer_question
from actions.action_handler import handle_action

def handle_user_input(user_input: str, session_id: str) -> str:
    if is_action(user_input):
        return handle_action(user_input, session_id)  # ✅ session_id passed
    else:
        return answer_question(user_input, session_id)

def is_action(text: str) -> bool:
    action_keywords = ["schedule", "create", "book", "raise", "ticket"]
    return any(word in text.lower() for word in action_keywords)