---
name: model_provider_rules
description: Enforce Google Gemini usage and prohibit OpenAI/Claude models across the repository.
always_on: true
---

# Google Gemini Model Provider Rules

- **Provider**: Exclusively use `langchain-google-genai` with `GEMINI_API_KEY`.
- **Prohibited**: Do not initialize active `ChatOpenAI`, `OpenAIEmbeddings`, `ChatAnthropic` as the user has no OpenAI/Claude accounts.

## Mapping Table:
| Legacy / OpenAI Model | Google Gemini Replacement | Use Case |
| :--- | :--- | :--- |
| `gpt-4o-mini`, `gpt-3.5-turbo` | `gemini-3.5-flash-lite` hoặc `gemini-3.5-flash` | Fast, high-throughput, classification, simple tasks |
| `gpt-4o`, `claude-3-5-sonnet` | `gemini-3.6-flash` | Reasoning, multi-step analysis, complex RAG |
| `text-embedding-3-small/large` | `GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")` | Semantic search, vector stores, caching |

## Best Practices:
- Always use `StrOutputParser()` to ensure standard string responses.
- Load environment variables with `dotenv.load_dotenv()`.
