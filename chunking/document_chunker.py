def chunk_document(doc, chunk_size=300, overlap=50):
    text = doc["text"]
    metadata = doc["metadata"]

    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end]

        chunks.append({
            "text": chunk_text,
            "metadata": {
                **metadata,
                "chunk_id": chunk_id
            }
        })

        chunk_id += 1
        start = end - overlap

    return chunks
