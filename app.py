import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import uuid
from agent.agent_controller import handle_user_input
from memory.redis_memory import clear_history

# Page title
st.title("Sahayak - Enterprise Assistant")

# Initialize session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear memory button
if st.button("🗑️ Clear Memory"):
    clear_history(st.session_state.session_id)
    st.session_state.messages = []  # also clear UI chat history
    st.success("Memory cleared!")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input (only one!)
user_input = st.chat_input("Ask a question:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking..."):
        response = handle_user_input(
            user_input,
            st.session_state.session_id
        )

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)