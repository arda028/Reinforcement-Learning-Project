import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

#This is code to render the final run of the maze by the test function. It is fed a maze state and the input that was performed
def show_maze(maze, input):

    numerical_maze = convert_maze(maze)

    cmap = mcolors.ListedColormap(['white', 'black', 'green', 'blue', 'red'])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    
    plt.clf()
    plt.imshow(numerical_maze, cmap=cmap, norm=norm, interpolation='nearest')

    plt.xticks([])
    plt.yticks([])

    plt.title('Input: ' + input)

    plt.pause(0.2)
    if maze.is_done():
        plt.pause(4)

#Convert maze from the string/grid representation into something that can be rendered (numerical representation only)
def convert_maze(maze):
    numerical_maze = np.zeros((len(maze.grid), len(maze.grid[0])), dtype=int)
    for y, row in enumerate(maze.grid):
        for x, cell in enumerate(row):
            if cell == 1:
                numerical_maze[y, x] = 1
            elif cell == 0:
                numerical_maze[y, x] = 0
            elif cell == 'S':
                numerical_maze[y, x] = 2
            elif cell == 'G':
                numerical_maze[y, x] = 3
            elif cell == 'E':
                numerical_maze[y, x] = 4
    x, y = maze.current_position
    numerical_maze[y, x] = 2
    return numerical_maze

def convert_input(action):
    if action == 0:
        return 'w'
    if action == 1:
        return 'a'
    if action == 2:
        return 's'
    if action == 3:
        return 'd'

def initialize_q_table_display(grid_size=10):
    # Create a figure and set up two subplots for the Q-value tables
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Initialize empty grids for display, with color normalization based on expected Q-values
    dummy_data = np.zeros((10, 10))
    vmin, vmax = -2, 2  # Adjust these to expected Q-value ranges

    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
    img1 = ax1.imshow(dummy_data, cmap='viridis', norm=norm)
    ax1.set_title('Average Q-values (Subgoal Not Reached)')
    plt.colorbar(img1, ax=ax1, orientation='vertical')

    img2 = ax2.imshow(dummy_data, cmap='viridis', norm=norm)
    ax2.set_title('Average Q-values (Subgoal Reached)')
    plt.colorbar(img2, ax=ax2, orientation='vertical')

    plt.tight_layout()
    plt.ion()  # Turn on interactive mode

    return fig, img1, img2

def update_q_table_display(fig, img1, img2, Q_table, grid_size=10):
    # Calculate the average Q-values for both subgoal states
    Q_no_subgoal = Q_table[:100]
    Q_with_subgoal = Q_table[100:]
    
    avg_Q_no_subgoal = Q_no_subgoal.mean(axis=1).reshape((grid_size, grid_size))
    avg_Q_with_subgoal = Q_with_subgoal.mean(axis=1).reshape((grid_size, grid_size))

    # Update image data without redrawing figure
    img1.set_data(avg_Q_no_subgoal)
    img2.set_data(avg_Q_with_subgoal)

    fig.canvas.draw()  # Update the figure canvas
    fig.canvas.flush_events()  # Process GUI events quickly to reflect changes
