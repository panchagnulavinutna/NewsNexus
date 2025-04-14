# app.py
import streamlit as st
from recommend_news import recommend_news

st.title("📰 NewsNexus - Personalized News Recommendation")

# Get user interest
user_input = st.text_input("Enter your interest (e.g., 'AI technology', 'finance', 'sports')")

# When the button is clicked, show recommendations
if st.button("Get Recommendations"):
    if user_input:
        articles = recommend_news(user_input)
        st.subheader("🔍 Top Recommended Articles")

        for article in articles:
            st.markdown(f"### 📰 {article['title']}")
            st.markdown(f"{article['description']}")
            st.markdown(f"[Read more]({article['url']})", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.warning("Please enter your interest to get recommendations.")
