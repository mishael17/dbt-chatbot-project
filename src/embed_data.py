import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from parse_dbt import load_manifest, extract_models
from format_metadata import create_chunks

def embed_chunks():
    print("Loading manifest...")
    manifest = load_manifest('data/target/manifest.json')
    models = extract_models(manifest)
    print(f"Extracted {len(models)} models.")

    print("Formatting chunks...")
    chunks = create_chunks(models)
    #print(chunks)

    print("Loading embedding model...")
    model = SentenceTransformer('all-mpnet-base-v2')

    print("Generating embeddings...")
    embeddings = model.encode(chunks, show_progress_bar=True, device='cpu')

    print("Creating FAISS index...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    print("Saving index...")
    faiss.write_index(index, 'embeddings/faiss_index.idx')

    print("Saving chunks...")
    with open('embeddings/chunks.txt', 'w') as f:
        for chunk in chunks:
            f.write(chunk + "\n---\n")

    print("Embedding process completed.")

if __name__ == "__main__":
    embed_chunks()
