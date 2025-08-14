# 📄 ContextSmith – A Context-Aware AI Assistant

## 🚀 Overview
**ContextSmith** is an intelligent, context-aware AI assistant that understands user questions in relation to provided or retrieved context.  
Unlike basic chatbots that respond blindly, ContextSmith **evaluates whether it has enough information before answering** — and takes autonomous steps to get what it needs.

---

## 🧠 How It Works
At its core, ContextSmith uses **LangChain** with a custom **tool-based reasoning system** and a local **Llama 3 model** via **Ollama**.  
The assistant’s decision-making flow:

1. **Judge context presence** – Checks if the user provided enough background.
2. **Retrieve missing context** – Uses a search tool if information is insufficient.
3. **Validate relevance** – Ensures the retrieved context matches the query.
4. **Separate context & question** – Prepares a clean, structured prompt for the AI.
5. **Answer with confidence** – Combines all relevant details into a clear response.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- [LangChain](https://www.langchain.com/) – Agent orchestration
- [Ollama](https://ollama.com/) – Local Llama 3 model
- [Streamlit](https://streamlit.io/) – Web-based UI
- Document parsing: `python-docx`, `PyPDF2`, `chardet`
- Optional: Web search integration (Tavily API or similar)

---

## 📂 Project Structure
```
ContextSmith/
│
├── tools/                 # Custom LangChain tools
│   ├── context_presence_judge.py
│   ├── web_search_tool.py
│   ├── context_relevance_checker.py
│   └── context_splitter.py
│
├── prompts/               # Prompt templates for tools
│   ├── context_judge_prompt.txt
│   ├── relevance_prompt.txt
│   └── splitter_prompt.txt
│
├── ui/                    # Streamlit interface
│   └── streamlit_ui.py
│
├── agent/                 # Agent configuration
│   └── agent_runner.py
│
├── main.py                # Entry point for local CLI mode
├── requirements.txt       # Python dependencies
└── README.md
```

---

## ⚙️ Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/YoussefYasserAbdelkader/ContextSmith.git
cd ContextSmith
```

2️⃣ **Create and activate a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

3️⃣ **Install dependencies**
```
pip install -r requirements.txt
```

4️⃣ **Install Ollama and pull Llama 3**
```
ollama pull llama3
```

---

## ▶️ Running the Project

### **Streamlit Web App**
```
streamlit run ui/streamlit_ui.py
```
Open your browser at `http://localhost:....`.

### **CLI Mode**
```
python main.py
```

---

## 📑 Features
- **Document upload** – Supports `.pdf`, `.docx`, `.txt` files
- **Automatic context analysis** – Determines whether more info is needed
- **Web search fallback** – Retrieves missing context dynamically
- **Context validation** – Ensures the information is relevant
- **Local AI processing** – No cloud API required (privacy-friendly)
- **Interactive UI** – Streamlit-based interface for seamless use


---

## 📌 Roadmap
- [ ] Add memory for multi-turn context
- [ ] Support more file formats (Markdown, HTML)
- [ ] Integrate vector database for long-term knowledge storage
- [ ] Add speech-to-text for voice queries

---

## 🤝 Contributing
Pull requests are welcome! Please fork the repo and create a new branch for your feature or bugfix.


This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
