import numpy as np

from agents.agent import *
from configs.config import *
from maze.maze import *
from utils.metrics import *
from utils.visualizer import *
from agents.q_learner import *

def main():
    maze = Maze(CONFIG) #Create instance of maze class, feed it the config (to define the grid)
    agent = Agent(maze, CONFIG) #Create instance of agent class, feed it the maze and config (for training parameters)
    q_learning = QLearning(agent, maze) #Create a combined Q_learning class with the agent and maze objects
    q_learning.train(CONFIG) #Perform the q_learning training
    q_learning.test(CONFIG) #Test if the training resulted in a successful algorithm

if __name__ == '__main__':
    main()
