import os
import tkinter as tk
from tkinter import filedialog
import docx
import PyPDF2

from agent.agent_runner import run_agent

# -------------------
# Document Loader
# -------------------
def load_document():
    root = tk.Tk()
    root.withdraw()

    print("📂 Please choose a document...")
    file_path = filedialog.askopenfilename(
        title="Select Document",
        filetypes=[
            ("All Supported", "*.txt;*.pdf;*.docx"),
            ("Text Files", "*.txt"),
            ("PDF Files", "*.pdf"),
            ("Word Documents", "*.docx"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        print("❌ No file selected.")
        return None

    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

        elif ext == ".docx":
            doc = docx.Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])

        elif ext == ".pdf":
            text = ""
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            return text.strip()

        else:
            print("⚠ Unsupported file type.")
            return None

    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


# -------------------
# Main Loop
# -------------------
def main():
    print("🔹 ContextSmith AI Agent (Llama 3 + LangGraph)")
    print("Type 'exit' to quit\n")

    document_text = load_document()
    if not document_text:
        return

    print("\n✅ Document loaded successfully!")
    print(f"📄 First 200 characters:\n{document_text[:200]}...\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = run_agent(user_input, document_text)
        print("🤖 AI:", result)


if __name__ == "__main__":
    main()
