"""
LangSmith Setup and Observability
Production monitoring for LangChain/LangGraph with Google Gemini
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable
from dotenv import load_dotenv

load_dotenv()

# Enable tracing if LANGSMITH_API_KEY is available
if os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGSMITH_TRACING"] = "true"


@traceable(name="basic_chaining")
def demo_basic_tracing():
    """Basic LangSmith tracing."""

    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

    prompt = ChatPromptTemplate.from_template("Explain {topic} in one sentence.")

    chain = prompt | llm | StrOutputParser()

    print("=== 1. Basic Tracing Demo ===\n")
    print("Running chain with LangSmith tracing enabled...")

    result = chain.invoke({"topic": "machine learning"})

    print(f"Result: {result}")
    print("\nCheck LangSmith dashboard for trace details.\n")


@traceable(name="named_runs_demo", tags=["production", "summarization"])
def demo_named_runs():
    """Name your runs for easier identification."""

    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

    prompt = ChatPromptTemplate.from_template("Summarize: {text}")

    chain = prompt | llm | StrOutputParser()

    print("=== 2. Named Runs Demo ===\n")

    result = chain.invoke(
        {"text": "LangSmith provides observability for LLM applications."}
    )

    print(f"Result: {result}")
    print("Run tagged with 'production', 'summarization'\n")


@traceable(name="trace_with_metadata_demo", tags=["metadata", "filtering"])
def demo_trace_with_metadata(user_id: str, request_type: str):
    """Add metadata to traces for filtering."""

    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
    chain = llm | StrOutputParser()

    print("=== 3. Trace with Metadata Demo ===\n")
    result = chain.invoke(f"Hello from user {user_id}")

    print(f"User ID: {user_id}, Request Type: {request_type}")
    print(f"Result: {result}\n")
    return result


if __name__ == "__main__":
    demo_basic_tracing()
    demo_named_runs()
    demo_trace_with_metadata(user_id="user_123", request_type="greeting")
