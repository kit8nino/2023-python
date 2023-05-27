from queue import PriorityQueue
from math import sqrt

def read_maze(filename):
    with open(filename) as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze

def neighbors(maze, cell: tuple[int, int]):
    row, col = cell
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    valid_neighbors = []
    for neighbor in neighbors:
        row, col = neighbor
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
            valid_neighbors.append(neighbor)
    return valid_neighbors

# Поиск в ширину
def find_path(maze):
    start = (0, 1)
    end = (len(maze) - 1, len(maze[0]) - 2)
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        visited.add(current)
        for neighbor in neighbors(maze, current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

# А*
def heuristic(cell, end):
    return sqrt((cell[0] - end[0]) ** 2 + (cell[1] - end[1]) ** 2)

def find_path_a_star(maze):
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
        for neighbor in neighbors(maze, current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                priority = len(new_path) + heuristic(neighbor, end)
                queue.put((priority, neighbor, new_path))
    return None

def main():
    filename = "maze-for-u.txt"
    maze = read_maze(filename)
    way1 = find_path(maze)
    way2 = find_path_a_star(maze)
    way22 = way2[1]
    for place in way1:
        maze[place[0]][place[1]] = "."
    result1 = ""
    for line in maze:
        result1 += "".join(line) + "\n"
    for place in way22:
        maze[place[0]][place[1]] = ","
    result2 = ""
    for line in maze:
        result2 += "".join(line) + "\n"
    with open("maze-for-me-done.txt", "w") as f:
        f.write(result2)
        print("Сработало!")
main()