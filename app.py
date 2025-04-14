import streamlit as st
import pandas as pd
from datetime import datetime
from recommend_news import get_recommendations

# Function to save clicked article
def log_user_click(title, url, user_id="guest"):
    history = {
        "user_id": user_id,
        "timestamp": datetime.now().isoformat(),
        "title": title,
        "url": url
    }

    df = pd.DataFrame([history])
    df.to_csv("user_history.csv", mode='a', header=not pd.io.common.file_exists("user_history.csv"), index=False)

# Streamlit App
st.title("📰 NewsNexus: Personalized News Recommender")

user_input = st.text_input("Enter your interest (e.g., AI, finance, sports)")

if user_input:
    st.subheader("Top Recommended Articles:")
    articles = get_recommendations(user_input)

    for article in articles:
        st.markdown(f"### {article['title']}")
        st.markdown(f"{article['description']}")
        if st.button(f"Read More about: {article['title']}"):
            log_user_click(article['title'], article['url'])
            st.markdown(f"[Click here to read more]({article['url']})")

