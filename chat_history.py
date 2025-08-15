chat_history_store = {}

def get_chat_history(session_id):
    return chat_history_store.get(session_id, [])

def add_message(session_id, role, text):
    if session_id not in chat_history_store:
        chat_history_store[session_id] = []
    chat_history_store[session_id].append({"role": role, "text": text})

def build_contents(session_id):
    history = get_chat_history(session_id)
    return [{"role": msg["role"], "parts": [{"text": msg["text"]}]} for msg in history]
