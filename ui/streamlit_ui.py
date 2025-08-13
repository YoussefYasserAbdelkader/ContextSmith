import os
import sys
import streamlit as st

# Make sure we can import from the main project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.agent_runner import run_agent  # EXACT same as main.py
import docx
import fitz  # PyMuPDF

def read_file(file):
    """Reads txt, pdf, docx and returns plain text."""
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file.name.endswith(".pdf"):
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join(page.get_text() for page in pdf)

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    else:
        return ""

# UI Title
st.title("📄 ContextSmith AI Agent (Streamlit UI)")

# File uploader
uploaded_file = st.file_uploader("Upload your document", type=["txt", "pdf", "docx"])

# Store document text in session
if uploaded_file:
    st.session_state.document_text = read_file(uploaded_file)
    st.success("✅ Document loaded successfully!")

# Chat input
user_input = st.chat_input("Ask me something about the document or the world...")

# Conversation display
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# If the user sends a message
if user_input and "document_text" in st.session_state:
    # Pass EXACTLY as main.py does
    result = run_agent(user_input, st.session_state.document_text)

    # Save to chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", result))

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")
