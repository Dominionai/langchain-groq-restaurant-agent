<div align="center">

# 🍽️ LangChain Groq Restaurant Agent

### AI that names your restaurant, builds your menu, and thinks for itself

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://console.groq.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

</div>

---

## 🧠 What Is This?

This project combines two things - a **working AI web app** and a **deep dive into LangChain agents**.

Pick a cuisine. The AI names your restaurant, then builds a full menu for it powered by **LLaMA 3.3 70B running on Groq**, chained together using **LangChain LCEL pipelines**.

Beyond the app, `langchain_groq.ipynb` goes further building an autonomous agent that can search the web, look up Wikipedia, solve maths, and hold a conversation with memory.

---

## 🚀 The App — Restaurant Name Generator

> **Select a cuisine → get a restaurant name → get a full menu. Instantly.**

| Cuisine | Generated Name (example) | Menu Style |
|---------|--------------------------|------------|
| 🇳🇬 Nigerian | Naija Royale | Jollof, Egusi, Suya Platter |
| 🇮🇹 Italian | La Bella Cucina | Pasta, Risotto, Tiramisu |
| 🇲🇽 Mexican | Casa del Sol | Tacos, Guac, Churros |
| 🇸🇦 Arabic | Al Majlis | Shawarma, Hummus, Baklava |
| 🇺🇸 American | The Liberty Grill | Burgers, Ribs, Cheesecake |

**How it works under the hood:**

```
User picks cuisine
      ↓
Chain 1 → "Suggest a fancy restaurant name for {cuisine} food"
      ↓
Chain 2 → "Suggest menu items for {restaurant_name}"
      ↓
Streamlit displays results
```

Two prompts. Two chains. One clean output. That's **LCEL sequential chaining**.

---

## 🤖 The Agent — `langchain_groq.ipynb`

A standalone LangChain agent built from scratch that can:

- 🔍 **Search the web** via Google (Serper API)
- 📖 **Look up Wikipedia** for factual answers
- 🧮 **Solve calculations** with a built-in calculator tool
- 🧠 **Remember conversations** using buffer and window memory

The agent doesn't just answer, it **thinks**:

```
Question → Thought → Action → Observation → Final Answer
```

This is the **ReAct reasoning pattern** that powers modern AI assistants.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🦜 [LangChain](https://langchain.com) | Chains, agents, memory, prompt templates |
| ⚡ [Groq](https://console.groq.com) | Blazing fast LLM inference |
| 🤖 LLaMA 3.3 70B | The brain behind every response |
| 🖥️ [Streamlit](https://streamlit.io) | Web interface |
| 🐍 Python 3.10 | Core language |

---

## 📁 Project Structure

```
langchain-groq-restaurant-agent/
│
├── 📂 RestaurantNameGenerator/
│   ├── main.py               # Streamlit UI
│   ├── langchain_helper.py   # LCEL chain logic
│   └── secret_key.py         # Your API keys go here
│
├── 📓 langchain_groq.ipynb   # Agent + memory implementation
├── 📄 requirement.txt
├── 📄 secret_key.py          # Root-level keys for the notebook
└── 📄 README.md
```

## What was removed in this project because of streamlit hosting

### 1. In main.py
- Removed - import langchain.py

### 2. In langchain.py
- Removed - from langchain_groq import ChatGroq
- Converted CORRECT_PASSWORD = "your password"  # Hardcoded in code to
  CORRECT_PASSWORD = st.secrets["APP_PASSWORD"]  # Instead of hardcoded 
---

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/Dominionai/langchain-groq-restaurant-agent.git
cd langchain-groq-restaurant-agent
```

### 2. Create a virtual environment
```bash
python -m venv ai_env

# Windows
ai_env\Scripts\activate

# Mac / Linux
source ai_env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirement.txt
```

### 4. Add your API keys & password
Fill in `secret_key.py`:
```python
groq_api_key = ""       # → console.groq.com (free)
serper_api_key = ""     # → serper.dev (free tier)
APP_PASSWORD = ""       # → add your password
```

### 5. Run the app
```bash
cd RestaurantNameGenerator
streamlit run main.py
```

---

## 💡 Core Concepts Implemented

| Concept | Where |
|---------|-------|
| `PromptTemplate` + `LCEL` pipe `\|` operator | `langchain_helper.py` |
| Sequential chaining (output → next input) | `langchain_helper.py` |
| `StrOutputParser` | `langchain_helper.py` |
| Tool-calling agent (Search, Wikipedia, Calculator) | `langchain_groq.ipynb` |
| ReAct reasoning loop | `langchain_groq.ipynb` |
| `ConversationBufferMemory` | `langchain_groq.ipynb` |
| `ConversationBufferWindowMemory` | `langchain_groq.ipynb` |

---

## 🔮 Coming Next

- [ ] Deploy to Streamlit Cloud (live demo link)
- [ ] Add custom cuisine input by the user
- [ ] RAG project - chat with your own documents
- [ ] Multi-agent system with LangGraph

---

<div align="center">

## 👤 Author

**Egwuatu Chibuike Dominion**
*AI Engineer | Nnamdi Azikiwe University*

[![Email](https://img.shields.io/badge/Email-chibuikedominion7@gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:chibuikedominion7@gmail.com)

---

*⭐ If this was useful or interesting, a star means a lot — thank you!*

</div>
