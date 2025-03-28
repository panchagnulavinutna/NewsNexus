import json
import numpy as np
import pandas as pd

# Load bandit results
with open("bandit_results.json", "r") as f:
    bandit_data = json.load(f)

# Define column names based on the data structure
column_names = ["NewsID", "Category", "SubCategory", "Title", "Description", "URL", "Entities", "Keywords"]

# Load the CSV file with specified column names
news = pd.read_csv("dataset/MINDlarge_train/news.csv", sep="\t", names=column_names, header=None)

# Create a mapping of NewsID to index
news_id_to_index = {news_id: idx for idx, news_id in enumerate(news["NewsID"])}

print(news_id_to_index)  # Verify mapping


def recommend_news(impressions, strategy="epsilon_greedy"):
    """Recommend news based on bandit model values."""
    valid_news = [imp.split('-')[0] for imp in impressions.split()]
    valid_news = [n for n in valid_news if n in news_id_to_index]

    if not valid_news:
        return []  # If no valid news articles are found

    scores = []
    for news_id in valid_news:
        index = news_id_to_index[news_id]
        score = bandit_data["values"][index]
        scores.append((news_id, score))

    # Sort by estimated reward (descending order)
    sorted_news = sorted(scores, key=lambda x: x[1], reverse=True)

    return [news_id for news_id, _ in sorted_news[:5]]  # Return top 5 recommendations

# Example usage
impressions = "N78206-0 N26368-0 N7578-0 N58592-0 N19858-0 N51569-0"
top_news = recommend_news(impressions)
print("Top recommended news:", top_news)
