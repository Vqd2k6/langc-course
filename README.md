# LangChain Course & Practice

Repository học tập và thực hành các khái niệm cốt lõi trong hệ sinh thái **LangChain**, bao gồm Document Loaders, Text Splitters, Semantic Chunking, Embeddings, Vector Stores, RAG Pipelines, Cost Optimization Patterns và LangSmith Observability.

---

> [!NOTE]
> **Lưu ý quan trọng về hệ sinh thái Model**:
> Hầu như toàn bộ các module và mã nguồn trong dự án này đều được chuẩn hóa và cấu hình để sử dụng **hệ sinh thái của Google (Google Generative AI / Gemini)**:
> - **LLM Chat Models**: `ChatGoogleGenerativeAI` (`gemini-3.6-flash`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`)
> - **Embedding Models**: `GoogleGenerativeAIEmbeddings` (`models/gemini-embedding-001`)
>
> Vui lòng đảm bảo bạn đã cấu hình `GEMINI_API_KEY` (hoặc `GOOGLE_API_KEY`) trong file `.env`.

---

## 🚀 Cài Đặt & Môi Trường

Dự án sử dụng trình quản lý gói `uv` với Python >= 3.10.

### 1. Cài đặt Dependencies
```bash
uv sync
```

### 2. Cấu hình biến môi trường (`.env`)
Tạo file `.env` ở thư mục gốc của project:
```env
GEMINI_API_KEY="your-gemini-api-key-here"
# GOOGLE_API_KEY="your-google-api-key-here"

# (Tùy chọn) Cấu hình LangSmith Tracing
LANGSMITH_API_KEY="your-langsmith-api-key"
LANGSMITH_PROJECT="langc-course"
```

---

## 📂 Cấu Trúc Mã Nguồn (`src/langc_course/`)

| Tệp | Mô tả |
| :--- | :--- |
| [`main.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/main.py) | Kiểm tra cài đặt và gọi thử các model Gemini (`gemini-3.6-flash`, `gemini-3.5-flash`). |
| [`document_loaders.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/document_loaders.py) | Demo tải dữ liệu từ tệp văn bản (`TextLoader`) và tệp PDF (`PyPDFLoader`). |
| [`text_splitters.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/text_splitters.py) | Các chiến lược chia nhỏ văn bản (Recursive, Character, Token, Markdown Header Splitter). |
| [`prod_senmatic.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/prod_senmatic.py) | Chiến lược cắt văn bản ngữ nghĩa (`SemanticChunker`) kết hợp cơ chế Recursive Fallback dùng Google Embeddings. |
| [`embeddings_deep.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/embeddings_deep.py) | Tạo embedding đơn lẻ, batch embedding, tính Cosine Similarity và lưu cache embedding (`CacheBackedEmbeddings`). |
| [`vector_stores.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/vector_stores.py) | Lưu trữ và truy vấn vector database với ChromaDB sử dụng Google Embeddings. |
| [`rag_pipeline.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/rag_pipeline.py) | Triển khai hoàn chỉnh luồng RAG (Retrieval-Augmented Generation) kết hợp Chroma và Gemini. |
| [`cost_optimization.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/cost_optimization.py) | Các kỹ thuật tối ưu chi phí LLM: Model Routing, Response Caching, và Token Budgeting với Gemini. |
| [`langsmith_setup.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/langsmith_setup.py) | Cấu hình giám sát LangSmith: Basic Tracing, Tagged Runs, và Metadata Filtering với Gemini. |

---

## 🏃 Hướng Dẫn Chạy Thử

Chạy từng module thông qua `uv`:

```bash
# Kiểm tra kết nối Gemini
uv run python src/langc_course/main.py

# Demo Semantic Chunking trong Production
uv run python src/langc_course/prod_senmatic.py

# Demo Embeddings & Caching
uv run python src/langc_course/embeddings_deep.py

# Demo Document Loaders
uv run python src/langc_course/document_loaders.py

# Demo Text Splitters
uv run python src/langc_course/text_splitters.py

# Demo Vector Stores (Chroma)
uv run python src/langc_course/vector_stores.py

# Demo RAG Pipeline
uv run python src/langc_course/rag_pipeline.py

# Demo Tối ưu Chi phí (Model Routing, Caching, Token Budgeting)
uv run python src/langc_course/cost_optimization.py

# Demo LangSmith Observability & Tracing
uv run python src/langc_course/langsmith_setup.py
```
