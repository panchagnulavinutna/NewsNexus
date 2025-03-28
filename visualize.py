import json
import matplotlib.pyplot as plt
import numpy as np

# Load bandit results
with open("bandit_results.json", "r") as f:
    results = json.load(f)

values = np.array(results["values"])
counts = np.array(results["counts"])

# Plot estimated values
plt.figure(figsize=(10, 5))
plt.hist(values, bins=50, alpha=0.7, color="blue", label="Estimated values")
plt.xlabel("Estimated Reward")
plt.ylabel("Frequency")
plt.title("Distribution of Estimated Reward Values")
plt.legend()
plt.show()

# Plot arm selection frequency
plt.figure(figsize=(10, 5))
plt.hist(counts, bins=50, alpha=0.7, color="green", label="Arm Selection Count")
plt.xlabel("Number of Times Arm was Selected")
plt.ylabel("Frequency")
plt.title("Distribution of Arm Selections")
plt.legend()
plt.show()
