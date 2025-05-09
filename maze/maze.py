def find_position(self, symbol):
    for y, row in enumerate(self.grid):
        for x, cell in enumerate(row):
            if cell == symbol:
                return (x, y)
    return None

# Maze class. handles movement, rewards, and resetting itself for a new loop.
class Maze:
    def __init__(self, config):
        self.grid = config['grid']
        self.start = find_position(self, 'S')
        self.goal = find_position(self, 'E')
        self.subgoal = find_position(self, 'G')
        self.current_position = self.start
        self.position_index = (self.start[0] - 1) * len(config['grid'][0]) + self.start[1]
        self.subgoal_reached = False
        self.reward = -1
        self.max_steps = config['max_steps']
        self.total_steps = 0


    def reset(self):
        self.current_position = self.start
        self.subgoal_reached = False
        self.total_steps = 0
        return self.start

    def move(self, action):
        self.total_steps += 1
        x, y = self.current_position
        #1234 are w a s d in order
        if action == 0:
            y -= 1
        elif action == 1:
            x -= 1
        elif action == 2:
            y += 1
        elif action == 3:
            x += 1
        if self.grid[y][x] == 1:
            self.reward -= 1
            return self.current_position
        else:
            self.current_position = (x, y)
            return self.current_position

    def get_reward(self):
        if self.current_position == self.goal and self.subgoal_reached:
            return 20
        elif self.current_position == self.subgoal and not self.subgoal_reached:
            self.subgoal_reached = True
            return 10
        else:
            return_value = self.reward
            self.reward = -1
            return return_value

    def is_done(self):
        return self.current_position == self.goal and self.subgoal_reached or self.total_steps > self.max_steps
