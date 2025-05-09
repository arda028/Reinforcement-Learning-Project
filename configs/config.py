CONFIG = {
    'grid': [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 'S', 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 'G', 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 'E', 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ], # you can change the grid here to test the algorithm with different mazes
       # if you change the maze, make sure there is still an s, g, and e in the grid, and that all are reachable.
       # there should also be a wall around the maze, otherwise the algorithm might break.

       #17 is a perfect score for the standard maze, and it is what "perfect runs" are scored on in the data summary.
       # this means that if you change the maze, the "perfect run count" will likely display 0, because the max reward changed.
    
    'episodes': 2000,
    'max_steps': 50,
    'alpha': 1, # learning rate
    'gamma': 0.9, # discount factor
    'epsilon': 1, # exploration
    'epsilon_decay': 0.9, # decay rate of epsilon

    'display_test_run': False, # display the final run after training with the visualizer
    'print_training_episode': False, #print the training episode number and total reward for the episode
    'print_data_summary': True
}
