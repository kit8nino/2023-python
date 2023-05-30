from math import sqrt
from queue import PriorityQueue

def read_maze(filename):
    with open(filename) as file:
        maze = [[char for char in line.strip()] for line in file]
    return maze

def get_neighbors(maze, cell: tuple[int, int]):
    row, col = cell
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    valid_neighbors = []
    for neighbor in neighbors:
        row, col = neighbor
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
            valid_neighbors.append(neighbor)
    return valid_neighbors

def bfs(maze):
    start = (0, 1)
    end = (len(maze) - 1, len(maze[0]) - 2)
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

def get_heuristic(cell, end):
    return sqrt((cell[0] - end[0]) ** 2 + (cell[1] - end[1]) ** 2)

def a_star(maze):
    start = (0, 1)
    end = (len(maze) - 1, len(maze[0]) - 2)
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    visited = set()
    while not queue.empty():
        p, current, path = queue.get()
        if current == end:
            return p, path
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                priority = len(new_path) + get_heuristic(neighbor, end)
                queue.put((priority, neighbor, new_path))
    return None

def solve_maze():
    filename = "maze-for-u.txt"
    maze = read_maze(filename)

    path1 = bfs(maze)
    for place in path1:
        maze[place[0]][place[1]] = "."
    result_1 = ""
    for line in maze:
        result_1 += "".join(line) + "\n"
    with open("maze-for-me-done1.txt", "w") as f:
        f.write(result_1)

    path_2 = a_star(maze)
    path_2 = path_2[1]

    for place in path_2:
        maze[place[0]][place[1]] = ","
        
    result_2 = ""
    for line in maze:
        result_2 += "".join(line) + "\n"

    with open("maze-for-me-done2.txt", "w") as f:
        f.write(result_2)

solve_maze()
