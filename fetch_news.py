import requests
import pandas as pd

API_KEY = "34c62eb4d3fc4c0286bf51cc05f923f9"  # Replace this with your actual key
query = "India"  # You can change this to any keyword
URL = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=50&apiKey={API_KEY}"

def fetch_and_save():
    response = requests.get(URL)
    data = response.json()

    if data["status"] == "ok":
        articles = data.get("articles", [])
        print(f"🔍 Number of articles fetched: {len(articles)}")

        if len(articles) > 0:
            df = pd.DataFrame(articles)
            df.to_csv("live_news.csv", index=False)
            print("✅ Articles saved to live_news.csv")
        else:
            print("⚠️ No articles found in the response.")
    else:
        print("❌ Failed to fetch news:", data)

if __name__ == "__main__":
    fetch_and_save()
