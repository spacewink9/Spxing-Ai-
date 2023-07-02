# spxing/machine_learning/reinforcement_learning.py

import numpy as np

class QLearningAgent:
    def __init__(self, num_actions, num_states, learning_rate=0.1, discount_factor=0.9, exploration_prob=0.2):
        self.num_actions = num_actions
        self.num_states = num_states
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob

        # Initialize Q-table with zeros
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.exploration_prob:
            # Random action to explore
            return np.random.choice(self.num_actions)
        else:
            # Choose best action based on Q-values
            return np.argmax(self.q_table[state, :])

    def update_q_table(self, state, action, next_state, reward, done):
        # Q-learning update rule
        q_value = self.q_table[state, action]
        next_q_value = np.max(self.q_table[next_state, :]) if not done else 0
        td_error = reward + self.discount_factor * next_q_value - q_value
        self.q_table[state, action] += self.learning_rate * td_error

    def get_q_table(self):
        return self.q_table# spxing/machine_learning/reinforcement_learning.py


# spxing/machine_learning/reinforcement_learning.py

