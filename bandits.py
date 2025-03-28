import numpy as np

class BanditAlgorithm:
    def __init__(self, num_arms):
        self.num_arms = num_arms
        self.counts = np.zeros(num_arms)  # Count of times each arm was pulled
        self.values = np.zeros(num_arms)  # Estimated reward for each arm

    def select_arm(self):
        """Override this method in a subclass."""
        raise NotImplementedError

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        
        # Update value estimate using incremental mean formula
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
