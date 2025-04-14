import pandas as pd
import re

def clean_text(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special chars
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra whitespace
    return text

def preprocess():
    df = pd.read_csv("combined_news.csv")
    df['title'] = df['title'].apply(clean_text)
    df['description'] = df['description'].apply(clean_text)
    df.to_csv("preprocessed_news.csv", index=False)
    print("✅ Preprocessing complete. Saved to preprocessed_news.csv")

if __name__ == "__main__":
    preprocess()
