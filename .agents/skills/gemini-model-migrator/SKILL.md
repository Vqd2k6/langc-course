---
name: gemini-model-migrator
description: Automatically migrate and adapt LangChain Python code to use Google Gemini models instead of OpenAI or Claude.
---

# Gemini Model Migrator

Use this workflow to convert any script or module that references OpenAI (`ChatOpenAI`, `OpenAIEmbeddings`) or Claude (`ChatAnthropic`) to run reliably with Google Gemini.

## Migration Steps

1. **Update Imports**:
   - Replace `from langchain_openai import ChatOpenAI, OpenAIEmbeddings` with:
     ```python
     from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
     from langchain_core.output_parsers import StrOutputParser
     ```

2. **Replace LLM Instances**:
   - For fast/cheap/routing/classifier tasks:
     ```python
     llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
     ```
   - For general tasks:
     ```python
     llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
     ```
   - For complex reasoning / advanced generation:
     ```python
     llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
     ```

3. **Replace Embeddings**:
   - Use:
     ```python
     embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
     ```

4. **Ensure Clean String Parsing**:
   - Pipe LLMs with `StrOutputParser()`:
     ```python
     chain = prompt | llm | StrOutputParser()
     ```

5. **Verify Execution**:
   - Run the script with `uv run python <file_path>` to ensure exit code 0.
