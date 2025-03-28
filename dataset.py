import pandas as pd
import os

def load_mind_data(data_dir, dataset_type="train"):
    """
    Load MIND dataset
    :param data_dir: Directory containing MIND dataset
    :param dataset_type: "train" or "dev"
    :return: DataFrames for behaviors and news
    """
    behaviors_path = os.path.join(data_dir, f"MINDlarge_{dataset_type}/behaviors.tsv")
    news_path = os.path.join(data_dir, f"MINDlarge_{dataset_type}/news.tsv")
    
    # Load behaviors (User interactions: user ID, clicked history, impressions)
    behaviors = pd.read_csv(behaviors_path, sep='\t', header=None, 
                            names=['ImpressionID', 'UserID', 'Time', 'History', 'Impressions'])
    
    # Load news articles (News ID, category, subcategory, title, abstract)
    news = pd.read_csv(news_path, sep='\t', header=None, 
                       names=['NewsID', 'Category', 'SubCategory', 'Title', 'Abstract', 'URL', 'TitleEntities', 'AbstractEntities'])
    
    return behaviors, news

# Modify bandits.py to use MIND dataset
def process_news_recommendation():
    """Example function to process news recommendations using MIND dataset."""
    data_dir = "dataset/"
    behaviors, news = load_mind_data(data_dir)
    
    # Example: Print first 5 user interactions
    print("User Interactions:")
    print(behaviors.head())
    
    # Example: Print first 5 news articles
    print("News Articles:")
    print(news.head())

if __name__ == "__main__":
    process_news_recommendation()
