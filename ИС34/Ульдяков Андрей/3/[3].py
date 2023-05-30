import heapq
import numpy as np



def read_maze(file_path='maze-for-u.txt'):
    with open(file_path, 'r') as f:
        maze = [[char for char in line.strip()] for line in f]
    return np.array(maze)

maze = read_maze()
size_x = len(maze)
size_y = len(maze[0])
def write_maze(maze, file_path):
    with open(file_path, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')


def get_neighbors(maze, row, col):
    neighbors = []
    if row > 0 and maze[row - 1][col] != '#':
        neighbors.append((row - 1, col))
    if row < maze.shape[0] - 1 and maze[row + 1][col] != '#':
        neighbors.append((row + 1, col))
    if col > 0 and maze[row][col - 1] != '#':
        neighbors.append((row, col - 1))
    if col < maze.shape[1] - 1 and maze[row][col + 1] != '#':
        neighbors.append((row, col + 1))
    return neighbors


def greedy_best_first_search(maze, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next_cell in get_neighbors(maze, *current):
            new_cost = cost_so_far[current] + 1
            if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                cost_so_far[next_cell] = new_cost
                priority = new_cost + np.linalg.norm(np.array(goal) - np.array(next_cell))
                heapq.heappush(frontier, (priority, next_cell))
                came_from[next_cell] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    for cell in path:
        if maze[cell] != 'S' and maze[cell] != 'T' and maze[cell] != 'E':
            maze[cell] = '.'

    return maze


def a_star_search(maze, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next_cell in get_neighbors(maze, *current):
            new_cost = cost_so_far[current] + 1
            if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                cost_so_far[next_cell] = new_cost
                priority = new_cost + np.linalg.norm(np.array(goal) - np.array(next_cell))
                heapq.heappush(frontier, (priority, next_cell))
                came_from[next_cell] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    for cell in path:
        if maze[cell] != 'S' and maze[cell] != '*' and maze[cell] != 'E' and maze[cell] != '.':
            maze[cell] = ','

    return maze


def remove_walls(maze):
    wall_count = {}
    for row in range(maze.shape[0]):
        for col in range(maze.shape[1]):
            if maze[row][col] == '#':
                wall_count[(row, col)] = 0

    for row in range(maze.shape[0]):
        for col in range(maze.shape[1]):
            if maze[row][col] == '.' or maze[row][col] == ',':
                for next_cell in get_neighbors(maze, row, col):
                    if maze[next_cell] == '#':
                        wall_count[next_cell] += 1

    for wall, count in wall_count.items():
        if count > 3:
            maze[wall] = ' '

    return maze


def solve_maze(file_path):
    global x, y
    maze = read_maze(file_path)
    start = tuple(np.argwhere(maze == 'S')[0])
    x = int(input(f"Введите координату X сокровища(не больше {size_x - 1}):"))
    y = int(input(f"Введите координату Y сокровища(не больше {size_y - 1}):"))
    if maze[x][y] == '#':
        while maze[x][y] == '#':
            print('Это поле занято стеной, так что подвинься\n')
            x = int(input('Попробуй еще раз ввести X: '))
            y = int(input('А теперь Y: '))
    maze[x][y] = '*'
    treasure = (x, y)
    exit = tuple(np.argwhere(maze == 'E')[0])
    maze = greedy_best_first_search(maze, start, treasure)
    maze = a_star_search(maze, treasure, exit)
    maze = remove_walls(maze)

    return maze

# Example usage
maze = solve_maze('maze-for-u.txt')
maze[x][y] = '*'
write_maze(maze, 'maze-for-u-done.txt')