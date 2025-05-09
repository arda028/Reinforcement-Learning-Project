import numpy as np

#Agent class. Can choose an action based on the current epsilon, and decay said epsilon. Q-learning details are handled in q_learner
class Agent:
    def __init__(self, maze, config):
        self.maze = maze
        self.epsilon = config['epsilon']
        self.alpha = config['alpha']
        self.gamma = config['gamma']
        self.action_space = [0, 1, 2, 3]
        self.state_space = len(self.maze.grid) * len(self.maze.grid[0]) * 2
        self.epsilon_decay = config['epsilon_decay']

    def choose_action(self, state, q_table):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.choice(self.action_space)
        else:
            return np.argmax(q_table[state])

    def decay_epsilon(self):
        self.epsilon = self.epsilon * self.epsilon_decay
