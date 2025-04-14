import streamlit as st
import pandas as pd
from recommend_news import recommend_news  # Make sure this function is importable

st.set_page_config(page_title="NewsNexus", layout="centered")

st.title("🗞️ NewsNexus - Personalized News Recommender")

# Input for user ID or preferences
user_id = st.text_input("Enter your user ID:")

if st.button("Get Recommendations"):
    if user_id:
        recommended = recommend_news(user_id)
        if recommended:
            st.success("Here are your recommended articles:")
            for i, article in enumerate(recommended, 1):
                st.markdown(f"**{i}. {article}**")
        else:
            st.warning("No recommendations found for this user.")
    else:
        st.warning("Please enter a user ID.")
