import numpy as np

def retrieve(query, model, index, chunks, k=3):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), k)

    results = []
    for i in indices[0]:
        results.append(chunks[i])

    return results
