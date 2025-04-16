import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

# Helper to convert text to sentence case
def to_sentence_case(text):
    if not isinstance(text, str) or not text:
        return ""
    text = text.strip()
    return text[0].upper() + text[1:].lower()

def load_embeddings():
    with open("news_embeddings.pkl", "rb") as f:
        df, embeddings = pickle.load(f)
    return df, embeddings

def get_recommendations_by_interest(interest, top_k=5):
    df, embeddings = load_embeddings()
    query_embedding = model.encode([interest])
    similarity_scores = cosine_similarity(query_embedding, embeddings)[0]
    top_k_indices = similarity_scores.argsort()[-top_k:][::-1]
    
    results = df.iloc[top_k_indices][['title', 'description', 'url']].copy()
    results['title'] = results['title'].apply(to_sentence_case)
    results['description'] = results['description'].apply(to_sentence_case)
    
    return results.to_dict(orient='records')

def get_recommendations_by_history(user_id="guest", top_k=5):
    try:
        history = pd.read_csv("user_history.csv")
        user_history = history[history['user_id'] == user_id]
        if user_history.empty:
            return []

        recent_titles = user_history['title'].tail(3).tolist()
        combined_query = " ".join(recent_titles)

        df, embeddings = load_embeddings()
        query_embedding = model.encode([combined_query])
        similarity_scores = cosine_similarity(query_embedding, embeddings)[0]
        top_k_indices = similarity_scores.argsort()[-top_k:][::-1]

        results = df.iloc[top_k_indices][['title', 'description', 'url']].copy()
        results['title'] = results['title'].apply(to_sentence_case)
        results['description'] = results['description'].apply(to_sentence_case)
        
        return results.to_dict(orient='records')
    except FileNotFoundError:
        return []
