from dotenv import load_dotenv
import numpy as np
import tempfile
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_openai import OpenAIEmbeddings
from langchain_classic.embeddings import CacheBackedEmbeddings
from langchain_classic.storage import LocalFileStore

load_dotenv()

# Google Generative AI Embeddings (Gemini)
embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# Uncomment below if you want to use OpenAI Embeddings instead:
# embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")


def basic_embeddings():
    print("=== 1. Basic Embeddings ===")
    # single text
    text = "What is Machine Learning?"
    single_embedding = embeddings_model.embed_query(text)
    print(f"Text: '{text}'")
    print(f"Vector dimensions: {len(single_embedding)}")
    print(f"First 5 values: {single_embedding[:5]}")
    print(f"Vector norm: {np.linalg.norm(single_embedding):.4f}\n")


def batch_embeddings():
    print("=== 2. Batch Embeddings ===")
    texts = [
        "What is Machine Learning?",
        "Explain the concept of overfitting in ML.",
        "How does a neural network work?",
    ]

    batch_embedding = embeddings_model.embed_documents(texts)
    for i, (txt, emb) in enumerate(zip(texts, batch_embedding)):
        print(f"Text {i+1}: '{txt}'")
        print(f"  Vector dimensions: {len(emb)}")
        print(f"  First 5 values: {emb[:5]}")
        print(f"  Vector norm: {np.linalg.norm(emb):.4f}")
    print()


def similarity_search():
    print("=== 3. Similarity Search ===")
    # Documents
    docs = [
        "Python is a programming language",
        "JavaScript is used for web development",
        "Machine learning enables AI applications",
        "Deep learning uses neural networks",
        "Cats are popular pets",
    ]

    query = "What programming languages exist?"

    # embed documents and query
    doc_vectors = embeddings_model.embed_documents(docs)
    query_vector = embeddings_model.embed_query(query)

    # compute cosine similarities
    def cosine_similarity(vec1, vec2):
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    similarities = [cosine_similarity(query_vector, doc_vec) for doc_vec in doc_vectors]

    # rank documents by similarity
    ranked_docs = sorted(zip(docs, similarities), key=lambda x: x[1], reverse=True)

    print(f"Query: {query}\n")
    print("Ranked by similarity:")
    for doc, score in ranked_docs:
        print(f"  {score:.4f}: {doc}")
    print()


# Caching ---
def embedding_caching():
    print("=== 4. Embedding Caching ===")
    with tempfile.TemporaryDirectory() as tempdir:
        store = LocalFileStore(root_path=tempdir)

        cached_embeddings = CacheBackedEmbeddings.from_bytes_store(
            underlying_embeddings=embeddings_model,
            document_embedding_cache=store,
            namespace="exercise",
        )

        text = "What is Reinforcement Learning?"

        # First call - hits API
        print("First call (API):")
        vectors1 = cached_embeddings.embed_documents([text])
        print(f"  Embedded {len(vectors1)} documents")

        # Second call - from cache
        print("\nSecond call (Cache):")
        vectors2 = cached_embeddings.embed_documents([text])
        print(f"  Embedded {len(vectors2)} documents")

        # Verify same results
        print(f"\nSame vectors: {np.allclose(vectors1[0], vectors2[0])}\n")


if __name__ == "__main__":
    basic_embeddings()
    batch_embeddings()
    similarity_search()
    embedding_caching()
