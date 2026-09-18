# Project Rules & Model Guidelines

## ⚠️ Model Provider Constraint (CRITICAL)
- **User Environment**: Only has access to **Google Gemini (Google Generative AI)** via `GEMINI_API_KEY` (or `GOOGLE_API_KEY`).
- **NO OpenAI or Anthropic Accounts**: Do **NOT** use `langchain-openai` (`ChatOpenAI`, `OpenAIEmbeddings`) or `langchain-anthropic` (`ChatAnthropic`) in active executable code.

## 🔄 Model Conversion & Replacement Standards

### 1. LLM Chat Models (`ChatGoogleGenerativeAI`)
Replace `ChatOpenAI(...)` / `ChatAnthropic(...)` with `ChatGoogleGenerativeAI`:
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Fast / Lightweight / Cost-effective model:
llm_fast = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# Standard / General Purpose model:
llm_standard = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# Advanced / High-Reasoning / Complex Tasks:
llm_advanced = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

# Recommended LCEL pipe with StrOutputParser for consistent string output:
chain = llm_standard | StrOutputParser()
```

### 2. Embedding Models (`GoogleGenerativeAIEmbeddings`)
Replace `OpenAIEmbeddings(...)` with `GoogleGenerativeAIEmbeddings`:
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Standard Embedding Model (3072 dimensions):
embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
```

### 3. Output Handling
When invoking `ChatGoogleGenerativeAI`, always handle content cleanly:
- Either pipe with `StrOutputParser()`: `chain = llm | StrOutputParser()`
- Or extract text: `text = res.content[0]['text'] if isinstance(res.content, list) else res.content`

### 4. Vector Stores & Cache
- For Chroma: Use `GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")`.
- For CacheBackedEmbeddings: `from langchain_classic.embeddings import CacheBackedEmbeddings` and `from langchain_classic.storage import LocalFileStore`.
