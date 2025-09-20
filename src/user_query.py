# src/query_gemini.py

import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv
from query_gemini import LLMClient
from google.genai import types

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def load_index():
    return faiss.read_index('embeddings/faiss_index.idx')

def load_chunks():
    with open('embeddings/chunks.txt', 'r') as f:
        content = f.read()
    return content.split("\n---\n")

#def query_user(user_input):
def query_user(user_input):
	print("Loading embeddings index...")
	index = load_index()
	print("Loading chunks...")
	chunks = load_chunks()

	print("Loading embedding model...")
	model = SentenceTransformer('all-mpnet-base-v2')

	print("Encoding query...")
	query_embedding = model.encode(
            [user_input],
    		show_progress_bar=False,
    		device='cpu',
    		normalize_embeddings=True,  # keeps vectors comparable
    		batch_size=1
            )

	print("Searching for relevant chunk...")
	distances, indices = index.search(np.array(query_embedding), k=3)
	best_chunks = [chunks[i] for i in indices[0]]
	best_chunks_text = "\n---\n".join(best_chunks)
	#print("printing best chunk",best_chunks_text)

	print("Found best matching chunk. Querying Gemini API...")

	client = LLMClient()

	contents = [
        types.Content(
            role="user",
            parts=[
                types.Part(
                    text=(
                        f"You are a data expert helping with dbt models.."
                        f"Here is some model information:\n{best_chunks_text}\nQuestion: {user_input}"
                    )
                )
            ]
        )
    ]

	response = client.generate_content(
        model="gemini-2.5-flash",
        contents=contents
    )

	print(response.text)

#   response = model_gemini.generate_content(messages=messages)
#   print("Response:")
#   print(response.text)

if __name__ == "__main__":
	user_input = input("Enter your question: ")
	query_user(user_input)
