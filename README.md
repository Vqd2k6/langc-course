# LangChain Course & Practice

Repository học tập và thực hành các khái niệm cốt lõi trong hệ sinh thái **LangChain**, bao gồm Document Loaders, Text Splitters, Embeddings, Vector Stores, RAG Pipelines, Cost Optimization Patterns, LangSmith Observability, Semantic Chunking và Advanced RAG Patterns.

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

Các bài học và mã nguồn được đánh số thứ tự tuần tự từ cơ bản đến nâng cao:

| TT | Tệp | Mô tả |
| :---: | :--- | :--- |
| 01 | [`01_main.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/01_main.py) | Khởi động & kiểm tra kết nối với các model Gemini (`gemini-3.6-flash`, `gemini-3.5-flash`). |
| 02 | [`02_document_loaders.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/02_document_loaders.py) | Tải dữ liệu từ tệp văn bản (`TextLoader`) và tệp PDF (`PyPDFLoader`). |
| 03 | [`03_text_splitters.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/03_text_splitters.py) | Các chiến lược chia nhỏ văn bản (Recursive, Character, Token, Markdown Header Splitter). |
| 04 | [`04_embeddings_deep.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/04_embeddings_deep.py) | Tạo vector embedding đơn/batch, tính Cosine Similarity và lưu bộ nhớ đệm (`CacheBackedEmbeddings`). |
| 05 | [`05_vector_stores.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/05_vector_stores.py) | Lưu trữ và truy vấn vector database với ChromaDB sử dụng Google Embeddings. |
| 06 | [`06_rag_pipeline.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/06_rag_pipeline.py) | Xây dựng pipeline RAG (Retrieval-Augmented Generation) hoàn chỉnh kết hợp Chroma và Gemini. |
| 07 | [`07_cost_optimization.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/07_cost_optimization.py) | Tối ưu chi phí LLM: Model Routing (Flash-Lite / Pro), Response Caching, và Token Budgeting. |
| 08 | [`08_langsmith_setup.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/08_langsmith_setup.py) | Giám sát & Quan trắc với LangSmith: Basic Tracing, Tagged Runs, và Metadata Filtering. |
| 09 | [`09_prod_senmatic.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/09_prod_senmatic.py) | Cắt văn bản ngữ nghĩa nâng cao (`SemanticChunker`) kết hợp cơ chế Recursive Fallback. |
| 10 | [`10_advanced_rag.py`](file:///Users/vqd2k6/Desktop/SGOD/Self/langc-course/src/langc_course/10_advanced_rag.py) | Các kỹ thuật RAG nâng cao: Multi-Query Retriever, Contextual Compression, Ensemble/Hybrid Search, Parent Document Retriever. |

---

## 🏃 Hướng Dẫn Chạy Thử

Chạy từng bài học thông qua `uv`:

```bash
# Bài 01: Setup & Gọi thử Gemini
uv run python src/langc_course/01_main.py

# Bài 02: Document Loaders (Text, PDF)
uv run python src/langc_course/02_document_loaders.py

# Bài 03: Text Splitters & Chunking
uv run python src/langc_course/03_text_splitters.py

# Bài 04: Embeddings & Caching
uv run python src/langc_course/04_embeddings_deep.py

# Bài 05: Vector Stores (ChromaDB)
uv run python src/langc_course/05_vector_stores.py

# Bài 06: RAG Pipeline
uv run python src/langc_course/06_rag_pipeline.py

# Bài 07: Tối ưu Chi phí (Model Routing, Caching, Token Budgeting)
uv run python src/langc_course/07_cost_optimization.py

# Bài 08: LangSmith Observability & Tracing
uv run python src/langc_course/08_langsmith_setup.py

# Bài 09: Semantic Chunking trong Production
uv run python src/langc_course/09_prod_senmatic.py

# Bài 10: Advanced RAG Patterns
uv run python src/langc_course/10_advanced_rag.py
```
