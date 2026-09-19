import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


def _recursive_fallback(text: str, chunk_size: int) -> list[str]:
    """Cắt văn bản theo phương pháp đệ quy dự phòng."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=50,
    )
    return splitter.split_text(text)


def smart_chunker(
    text: str,
    use_semantic: bool = True,
    fallback_chunk_size: int = 500,
) -> list[str]:
    """Production chunking with semantic as primary, recursive as fallback using Google Gemini embeddings."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    if use_semantic:
        try:
            chunker = SemanticChunker(
                embeddings,
                breakpoint_threshold_type="percentile",
                breakpoint_threshold_amount=90,
            )
            chunks = chunker.split_text(text)

            # Validate chunks aren't too large
            max_chunk_size = 200
            if any(len(c) > max_chunk_size for c in chunks):
                # Fallback to recursive for oversized chunks
                return _recursive_fallback(text, fallback_chunk_size)

            return chunks

        except Exception as e:
            print(f"Semantic chunking failed: {e}, using fallback")
            return _recursive_fallback(text, fallback_chunk_size)

    return _recursive_fallback(text, fallback_chunk_size)


# === Ví dụ kiểm thử thực tế ===
if __name__ == "__main__":
    sample_document = """
    Tập đoàn VinFast được thành lập vào năm 2017 tại Việt Nam. Doanh nghiệp này vừa công bố kế hoạch xuất khẩu xe điện sang thị trường Bắc Mỹ.
    
    Quy trình xác thực người dùng yêu cầu hệ thống phải kiểm tra OAuth token kỹ lưỡng. Mọi API call cần tuân thủ cơ chế Rate Limiting nghiêm ngặt để tránh nghẽn mạng.
    """

    chunks = smart_chunker(sample_document, use_semantic=True)
    print(f"Created {len(chunks)} semantic chunks:")
    for i, c in enumerate(chunks, 1):
        print(f"\n--- Chunk {i} ---")
        print(c.strip())