import requests
import csv
import streamlit as st
import pandas as pd
from datetime import datetime
from recommend_news import get_recommendations_by_interest, get_recommendations_by_history

def log_user_click(title, url, user_id="guest"):
    history = {
        "user_id": user_id,
        "timestamp": datetime.now().isoformat(),
        "title": title,
        "url": url
    }
    df = pd.DataFrame([history])
    df.to_csv("user_history.csv", mode='a', header=not pd.io.common.file_exists("user_history.csv"), index=False)

def save_feedback(user_id, title, url, feedback):
    row = {
        "user_id": user_id,
        "timestamp": datetime.now().isoformat(),
        "title": title,
        "url": url,
        "feedback": feedback
    }
    df = pd.DataFrame([row])
    df.to_csv("feedback.csv", mode='a', header=not pd.io.common.file_exists("feedback.csv"), index=False)

def fetch_live_news(interest, api_key="34c62eb4d3fc4c0286bf51cc05f923f9"):
    url = f"https://newsapi.org/v2/everything?q={interest}&language=en&pageSize=10&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [
            {
                "title": a["title"],
                "description": a["description"],
                "url": a["url"]
            } for a in articles if a["title"] and a["description"]
        ]
    else:
        return []

# Streamlit UI
st.title("📰 NewsNexus: Connecting You to What Matters Most")

tab1, tab2 = st.tabs(["🔍 Explore by Interest", "🎯 Recommended for You"])

# Custom background image for the entire app
st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1635868355594-a297d37b3494?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .big-button {
            font-size: 24px;
            padding: 8px 20px;
            margin-right: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔍 Explore by Interest Tab
with tab1:
    user_id_interest = st.text_input("Enter your Username to explore interests", key="user_id_interest")
    if user_id_interest:
        interest = st.text_input("Enter a topic of interest (e.g., music, sports, finance)", key="topic_input")
        if interest:
            st.subheader(f"Top Articles for: {interest}")
            articles = fetch_live_news(interest)
            if not articles:
                st.warning("No live articles found. Try a different interest.")
            for i, article in enumerate(articles):
                with st.container():
                    st.markdown(f"### {article['title']}")
                    st.markdown(article['description'])
                    st.markdown(f"[Click here to read more]({article['url']})", unsafe_allow_html=True)

                    # Like/Dislike buttons (enlarged using HTML)
                    like_key = f"like-{i}"
                    dislike_key = f"dislike-{i}"
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button("👍 Like", key=like_key):
                            log_user_click(article['title'], article['url'], user_id_interest)
                            save_feedback(user_id_interest, article['title'], article['url'], "like")
                    with col2:
                        if st.button("👎 Dislike", key=dislike_key):
                            log_user_click(article['title'], article['url'], user_id_interest)
                            save_feedback(user_id_interest, article['title'], article['url'], "dislike")

                st.markdown("---")

# 🎯 Recommended for You Tab
with tab2:
    user_id = st.text_input("Enter your Username to get personalized recommendations", key="recommend_user_id")
    if user_id:
        st.subheader(f"Articles recommended for you, {user_id}")
        articles = get_recommendations_by_history(user_id)
        if not articles:
            st.info("No recommendations found. Start exploring articles in the first tab!")
        for i, article in enumerate(articles):
            with st.container():
                st.markdown(f"### {article['title']}")  # case preserved
                st.markdown(article['description'])     # case preserved
                st.markdown(f"[Click here to read more]({article['url']})", unsafe_allow_html=True)
            st.markdown("---")
