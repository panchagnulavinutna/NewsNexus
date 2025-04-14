import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

def generate_embeddings():
    # Load preprocessed news
    df = pd.read_csv("preprocessed_news.csv")
    
    # Use title + description as input text
    texts = (df['title'].fillna('') + ". " + df['description'].fillna('')).tolist()
    
    # Load sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')  # You can use other models too

    print("🔍 Generating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)

    # Save embeddings to a file
    with open("news_embeddings.pkl", "wb") as f:
        pickle.dump((df, embeddings), f)
    
    print("✅ Embeddings generated and saved to news_embeddings.pkl")

if __name__ == "__main__":
    generate_embeddings()
