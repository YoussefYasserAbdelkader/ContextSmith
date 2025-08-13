import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tempfile
from pathlib import Path
import fitz  
import docx
from agent.agent_runner import run_agent  

# =================
# Helpers to read files
# =================
def read_txt(file_path):
    return Path(file_path).read_text(encoding="utf-8")

def read_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def read_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def process_file(uploaded_file):
    suffix = uploaded_file.name.lower()
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    if suffix.endswith(".txt"):
        return read_txt(tmp_path)
    elif suffix.endswith(".docx"):
        return read_docx(tmp_path)
    elif suffix.endswith(".pdf"):
        return read_pdf(tmp_path)
    else:
        st.error("❌ Unsupported file type")
        return ""

# =================
# Streamlit UI Config
# =================
st.set_page_config(page_title="ContextSmith Chat", layout="wide")
st.title("💬 ContextSmith AI Agent")

# =================
# Session State Setup
# =================
if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "messages" not in st.session_state:
    st.session_state.messages = []  # [{"role": "user", "content": "..."}, {"role": "ai", "content": "..."}]

# =================
# Upload Document
# =================
uploaded_file = st.file_uploader("📂 Upload document", type=["txt", "pdf", "docx"])
if uploaded_file:
    st.session_state.document_text = process_file(uploaded_file)
    st.success("✅ Document loaded successfully!")

# =================
# Display Chat Messages
# =================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# =================
# Chat Input
# =================
if st.session_state.document_text:  # Only allow chat if doc uploaded
    user_input = st.chat_input("Ask something about the document or general...")
    if user_input:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Call the exact same agent logic from terminal
        with st.chat_message("assistant"):
            with st.spinner("🤖 Thinking..."):
                ai_response = run_agent(user_input, st.session_state.document_text)
            st.markdown(ai_response)

        # Store assistant reply in history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
else:
    st.info("Please upload a document to start chatting.")
