from queue import PriorityQueue
from math import sqrt
import random

# создание списка на основе "maze-for-u.txt" файла с лабиринтом
def read_maze(filename):
    with open(filename) as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze

# создание ключа  в рандомном месте
maze = read_maze("maze-for-u.txt")
height = len(maze)
width = len(maze[0])
passages = []
for i in range(height):
    for j in range(width):
        if maze[i][j] == " ":
            passages.append((i, j))
random_key = random.choice(passages)

# функция, возвращающая список валидных соседей
def get_neighbors(maze, cell):
    row, col = cell
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    valid_neighbors = []
    for neighbor in neighbors:
        row, col = neighbor
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
            valid_neighbors.append(neighbor)
    return valid_neighbors

# эвристическое расстояние от ячейки до ключа или конечной точки
def get_heuristic(cell, end):
    return sqrt((cell[0] - end[0]) ** 2 + (cell[1] - end[1]) ** 2)

# Жадный алгоритм
def find_path_greedy(maze):
    start = (0, 1)
    key = random_key

    stack = [(start, [start])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if current == key:
            return path
        visited.add(current)
        neighbors = get_neighbors(maze, current)
        neighbors.sort(key=lambda neighbor: get_heuristic(neighbor, key))
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

# алгоритм А*
def find_path_a_star(maze):
    key = random_key
    end = (len(maze) - 1, len(maze[0]) - 2)
    queue = PriorityQueue()
    queue.put((0, key, [key]))
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

# создание файла "resuult.txt" 
def main():
    filename = "maze-for-u.txt"
    maze = read_maze(filename)

    path1 = find_path_greedy(maze)
    path2 = find_path_a_star(maze)
    path2 = path2[1]

    for place in path1:
        maze[place[0]][place[1]] = "."

    res1 = ""
    for line in maze:
        res1 += "".join(line) + "\n"

    for place in path2:
        maze[place[0]][place[1]] = ","

    res2 = ""
    for line in maze:
        res2 += "".join(line) + "\n"

    with open("resuult.txt", "w") as f:
        f.write(res2)

main()
