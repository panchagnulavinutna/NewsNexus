# recommend_news.py
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_recommendations(user_input, top_k=5):
    # Load the saved data
    with open("news_embeddings.pkl", "rb") as f:
        df, embeddings = pickle.load(f)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([user_input])
    similarity_scores = cosine_similarity(query_embedding, embeddings)[0]
    top_k_indices = similarity_scores.argsort()[-top_k:][::-1]

    results = []
    for idx in top_k_indices:
        results.append({
            "title": df.iloc[idx]["title"],
            "description": df.iloc[idx]["description"],
            "url": df.iloc[idx]["url"]
        })
    return results
