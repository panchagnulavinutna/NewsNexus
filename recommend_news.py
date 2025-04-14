import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_news(user_input, top_k=5):
    # Load the saved data
    with open("news_embeddings.pkl", "rb") as f:
        df, embeddings = pickle.load(f)

    # Load the same model used for generating embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Encode the user input
    query_embedding = model.encode([user_input])

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(query_embedding, embeddings)[0]

    # Get top K indices
    top_k_indices = similarity_scores.argsort()[-top_k:][::-1]

    # Show top K recommended articles
    print(f"\n🔍 Top {top_k} Recommended News Articles for: \"{user_input}\"")
    for idx in top_k_indices:
        print(f"\n📰 Title: {df.iloc[idx]['title']}")
        print(f"📄 Description: {df.iloc[idx]['description']}")
        print(f"🔗 URL: {df.iloc[idx]['url']}")

if __name__ == "__main__":
    query = input("🔎 Enter your interest (e.g., 'AI technology', 'finance', 'sports'): ")
    recommend_news(query)
