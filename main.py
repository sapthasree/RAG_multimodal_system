from ingestion.load_text import load_text
from ingestion.load_pdf import load_pdf
from preprocessing.clean_text import clean_text
from chunking.document_chunker import chunk_document
from embeddings.embedder import embed_chunks
from vector_store.faiss_index import create_faiss_index
from retrieval.retriever import retrieve
from sentence_transformers import SentenceTransformer

# Load documents
docs = []
docs.extend(load_text("data/documents/sample.txt"))
docs.extend(load_pdf("data/documents/sample.pdf"))

# Clean documents
for d in docs:
    d["text"] = clean_text(d["text"])

# Chunk documents
chunks = []
for doc in docs:
    chunks.extend(chunk_document(doc))

# Embed
embeddings = embed_chunks(chunks)

# Vector store
index = create_faiss_index(embeddings)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Query
query = input("Ask a question: ")
results = retrieve(query, model, index, chunks)

print("\nRetrieved Context:\n")
for r in results:
    print(f"[{r['metadata']['source']} | Page {r['metadata']['page']}]")
    print(r["text"])
    print("-" * 50)
