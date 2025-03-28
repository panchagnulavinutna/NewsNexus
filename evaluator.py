import pandas as pd
import numpy as np

import json
from dataset import load_mind_data
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

class BanditAlgorithm:
    def __init__(self, num_arms):
        self.num_arms = num_arms
        self.counts = np.zeros(num_arms)  # Number of times each arm was pulled
        self.values = np.zeros(num_arms)  # Estimated reward values

    def select_arm(self):
        """Override this method in a subclass."""
        raise NotImplementedError

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value

class EpsilonGreedy(BanditAlgorithm):
    def __init__(self, num_arms, epsilon):
        super().__init__(num_arms)
        self.epsilon = epsilon

    def select_arm(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.num_arms)
        return np.argmax(self.values)

def evaluate_bandit(data_dir):
    """Evaluate bandit algorithm using MIND dataset."""
    behaviors, news = load_mind_data(data_dir)
    num_arms = len(news)
    bandit = EpsilonGreedy(num_arms, epsilon=0.1)

    news_id_to_index = {news_id: idx for idx, news_id in enumerate(news['NewsID'])}

    y_true = []
    y_pred = []

    for index, row in behaviors.iterrows():
        impressions = row['Impressions'].split()
        chosen_news = np.random.choice(impressions)
        chosen_news_base = chosen_news.split('-')[0]  # Remove '-X' suffix

        if chosen_news_base not in news_id_to_index:
            continue  # Skip if no match

        chosen_arm = news_id_to_index[chosen_news_base]  # Fast lookup
        reward = np.random.choice([0, 1], p=[0.8, 0.2])  # Simulated reward

        # Collect predictions and ground truths
        y_true.append(1 if '-1' in chosen_news else 0)  # Actual click (1) or not (0)
        y_pred.append(reward)  # Model prediction (rewarded click or not)

        bandit.update(chosen_arm, reward)

    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average='weighted')
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')

    print("Accuracy:", accuracy)
    print("F1 Score:", f1)
    print("Precision:", precision)
    print("Recall:", recall)

    # Save results
    results = {
        "counts": bandit.counts.tolist(),
        "values": bandit.values.tolist(),
        "metrics": {
            "accuracy": accuracy,
            "f1_score": f1,
            "precision": precision,
            "recall": recall
        }
    }
    with open("bandit_results.json", "w") as f:
        json.dump(results, f)

    print("Results saved to bandit_results.json")

if __name__ == "__main__":
    evaluate_bandit("dataset/")
