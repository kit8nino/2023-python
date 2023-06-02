import queue as q
import math as m

#Читаем лабиринт
def read_maze(file):
    with open(file) as f:
        maze = [[c for c in line.strip()] for line in f]
    return maze

def get_neighbors(maze, cell):
    r, c = cell
    neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    valid_neighbors = []
    for n in neighbors:
        r, c = n
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != "#":
            valid_neighbors.append(n)
    return valid_neighbors

#Поиск в ширину
def BFS(maze):
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

#Эвристическое расстояние
def heuristic(cell, end):
    return m.sqrt((cell[0] - end[0]) ** 2 + (cell[1] - end[1]) ** 2)

#A
def A_star(maze):
    start = (0, 1)
    end = (len(maze) - 1, len(maze[0]) - 2)
    queue = q.PriorityQueue()
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
                priority = len(new_path) + heuristic(neighbor, end)
                queue.put((priority, neighbor, new_path))
    return None

file = "maze-for-u.txt"
maze = read_maze(file)
path1 = BFS(maze)
path2 = A_star(maze)
path2 = path2[1]

for place in path1:
    maze[place[0]][place[1]] = "."
result1 = ""

for line in maze:
    result1 += "".join(line) + "\n"

for place in path2:
    maze[place[0]][place[1]] = ","
result2 = ""

for line in maze:
    result2 += "".join(line) + "\n"

with open("maze-for-me-done.txt", "w") as f:
    f.write(result2)