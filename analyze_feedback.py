import pandas as pd
from collections import Counter

def analyze_feedback(user_id="guest"):
    try:
        df = pd.read_csv("feedback.csv")
        df_user = df[df['user_id'] == user_id]
        liked_articles = df_user[df_user['feedback'] == 'like']

        if liked_articles.empty:
            print("No liked articles to analyze.")
            return

        print(f"\n🧠 Feedback Summary for {user_id}:")

        titles = liked_articles['title'].tolist()
        print("✅ Titles liked:")
        for title in titles:
            print(f" - {title}")

    except FileNotFoundError:
        print("⚠️ No feedback found.")

if __name__ == "__main__":
    analyze_feedback()
