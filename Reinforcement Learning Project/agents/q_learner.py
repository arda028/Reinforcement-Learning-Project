#Here are most of the details specific to q_learning. This way, the maze and agent can be adapted to a different algorithm if needed.

import numpy as np
from utils.visualizer import *

def get_state_index(self, position):
    return ((position[0] - 1) * len(self.maze.grid[0]) + position[1]) * (1 + self.maze.subgoal_reached)

class QLearning:
    def __init__(self, agent, maze):
        self.agent = agent
        self.maze = maze
        self.q_table = np.zeros((self.agent.state_space, len(self.agent.action_space)))

    #This is the training loop. Here we ask the maze to reset, reset the values we keep track of,
    #and then loop through a training iteration. The q-table is not reset, most other things are.
    def train(self, config):
        episodes = config['episodes']

        self.first_finished_run = 0
        self.first_perfect_run = 0
        self.average_reward = 0
        self.number_of_perfect_runs = 0
        self.average_score_first_fifth = 0
        self.average_score_last_fifth = 0
        self.final_run_inputs = []
        #variables for visualizer initialize_q_table_display(self.q_table)


        for episode in range(episodes):
            self.maze.reset()
            state = get_state_index(self, self.maze.current_position)
            endreached = False
            total_reward = 0

            while not self.maze.is_done():
                action = self.agent.choose_action(state, self.q_table)
                next_state = self.maze.move(action)
                next_state = get_state_index(self, next_state)
                reward = self.maze.get_reward()
                total_reward += reward
                self.q_table[state][action] += self.agent.alpha * (reward + self.agent.gamma * np.max(self.q_table[next_state]) - self.q_table[state][action])
                state = next_state

            if config['print_training_episode']:
                print("Episode: ", episode, " Reward: ", total_reward, " Epsilon: ", self.agent.epsilon)

            if config['print_data_summary']:
                if total_reward == 17:
                    self.number_of_perfect_runs += 1
                    if self.first_perfect_run == 0:
                        self.first_perfect_run = episode
                if total_reward > (config['max_steps'] - 10) * -1 and self.first_finished_run == 0:
                    self.first_finished_run = episode
                self.average_reward += total_reward
                if episode < episodes / 5:
                    self.average_score_first_fifth += total_reward
                if episode > episodes - episodes / 5:
                    self.average_score_last_fifth += total_reward


            self.agent.decay_epsilon()
 
        #Print details specific to the training. Useful for checking whether a certain epsilon, gamma, etc. is good.
        if config['print_data_summary']:
            print("Average Reward: ", self.average_reward / episodes)
            print("Number of Perfect Runs: ", self.number_of_perfect_runs)
            print("Average Score First Fifth: ", self.average_score_first_fifth / (episodes / 5))
            print("Average Score Last Fifth: ", self.average_score_last_fifth / (episodes / 5))
            print("First Finished Run: ", self.first_finished_run)
            print("First Perfect Run: ", self.first_perfect_run)

    #Here we set the exploration rate to zero and then let the trained algorithm attempt to solve the maze.
    #If the algorithm has not been sufficiently trained, the agent WILL get stuck in a loop here, because it can no longer break out
    #of infinite loops by random chance exploration. This means that, even if the algorithm has finished once, the test might still fail.
    def test(self, config):
        self.maze.reset()
        state = get_state_index(self, self.maze.current_position)
        endreached = False
        total_reward = 0
        show_n = 0
        if config['display_test_run']:
            action_sequence = ""
        while not self.maze.is_done():
            action = np.argmax(self.q_table[state])
            if show_n < 30 and config['display_test_run']:
                action_sequence += convert_input(action)
                action_sequence += " "
                show_maze(self.maze, action_sequence)
                show_n += 1
            next_state = self.maze.move(action)
            next_state = get_state_index(self, next_state)
            reward = self.maze.get_reward()
            total_reward += reward
            state = next_state
        if config['display_test_run']:
            show_maze(self.maze, action_sequence)
        if config['print_data_summary']:
            if total_reward <= (config['max_steps'] - 10) * -1:
                print("Failed to reach goal")
            else:
                print("Final run Reward: ", total_reward)
