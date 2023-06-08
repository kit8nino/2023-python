from queue import PriorityQueue
from math import sqrt
import random

# функция для чтения лабиринта из файла
def read_maze(filename):
    with open(filename) as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze

# функция для получения списка соседей
def get_neighbors(maze, cell):
    row, col = cell
    neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    valid_neighbors = []
    for neighbor in neighbors:
        row, col = neighbor
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
            valid_neighbors.append(neighbor)
    return valid_neighbors

# функция для расчета эвристической функции
def get_heuristic(cell, end):
    return sqrt((cell[0]-end[0])**2 + (cell[1]-end[1])**2)

# жадный алгоритм поиска пути до ключа
def find_path_to_key(maze, key):
    start = (0, 1)
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
                stack.append((neighbor, path+[neighbor]))

# A* алгоритм поиска пути до выхода
def find_path_to_exit(maze, start, end):
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    visited = set()

    while not queue.empty():
        p, current, path = queue.get()
        if current == end:
            return path
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                priority = len(new_path) + get_heuristic(neighbor, end)
                queue.put((priority, neighbor, new_path))

# чтение лабиринта из файла
maze = read_maze("maze-for-u.txt")

# выбор произвольного места для ключа
height = len(maze)
width = len(maze[0])
passages = []
for i in range(height):
    for j in range(width):
        if maze[i][j] == " ":
            passages.append((i, j))
key = random.choice(passages)
maze[key[0]][key[1]] = "*"

# поиск пути до ключа и отметка его ячеек
path_to_key = find_path_to_key(maze, key)
for place in path_to_key:
    maze[place[0]][place[1]] = "."

# поиск пути до выхода и отметка его ячеек
start = path_to_key[-1]
end = (height-1, width-2)
path_to_exit = find_path_to_exit(maze, start, end)
for place in path_to_exit:
    maze[place[0]][place[1]] = ","

# запись результата в файл "maze-for-me-done.txt"
with open("maze-for-me-done.txt", "w") as file:
    for line in maze:
        file.write("".join(line)+"\n")