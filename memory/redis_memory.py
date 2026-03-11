import redis
import json
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
MAX_HISTORY = 5

client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def save_message(session_id: str, role: str, content: str):
    key = f"session:{session_id}:history"
    message = json.dumps({"role": role, "content": content})
    client.rpush(key, message)
    client.ltrim(key, -MAX_HISTORY * 2, -1)
    client.expire(key, 3600)

def get_history(session_id: str) -> list:
    key = f"session:{session_id}:history"
    messages = client.lrange(key, 0, -1)
    return [json.loads(m) for m in messages]

def clear_history(session_id: str):
    key = f"session:{session_id}:history"
    client.delete(key)

def format_history_for_prompt(session_id: str) -> str:
    history = get_history(session_id)
    if not history:
        return ""
    formatted = "Previous Conversation:\n"
    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        formatted += f"{role}: {msg['content']}\n"
    return formatted + "\n"