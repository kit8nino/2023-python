import heapq
from collections import deque

# Функция для импорта и преобразования исходного файла
def read_maze(filename):
    with open(filename) as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze
maze = read_maze("maze-for-u.txt")

# Функция определения начальной точки
def start_points(maze):
    for Y in range(len(maze[0])):
        if maze[0][Y] == " ":
            start = (0, Y)
            break
    return start
start = start_points(maze)

# Функция нахождения точки выхода
def end_points(maze):
    for Y in range(len(maze[0])):
        if maze[len(maze) - 1][Y] == " ":
            end = (len(maze) - 1, Y)
            break
    return end
end = end_points(maze)

# Функция определения ключевой точки
def key_points(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "*":
                key = (i, j)
                break
    return key
key = key_points(maze)

def bfs(maze, start, end):
    # инициализация очереди и множества посещенных вершин
    queue = deque([(start, [])])
    visited = set([start])

    # продолжаем искать, пока очередь не опустеет
    while queue:
        # извлечь вершину из очереди
        node, path = queue.popleft()

        # если мы достигли цели, вернуть найденный путь
        if node == end:
            return path

        # добавить все непосещенные соседние вершины в очередь
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = node[0]+dx, node[1]+dy
            if 0 <= x <len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#' and (x, y) not in visited:
                visited.add((x, y))
                queue.append(((x, y), path + [(x, y)]))

    # если мы не нашли путь до цели, возвращаем None
    return None
Up_to_the_key = bfs(maze, start, key)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):

    path = []
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == end:
            break

        for next in get_neighbors(maze, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(end, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    if current != end:
        return None

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    return path

def get_neighbors(maze, current):

    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x = current[0] + dx
        y = current[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "#":
            neighbors.append((x, y))
    return neighbors
Before_the_exit = astar(maze,key, end)

def Signs(maze, path, symbol):
    for cord in path:
        x, y = cord
        maze[x][y] = symbol
        x, y = key
        maze[x][y] = "*"
    return maze
maze_to_the_key = Signs(maze, Up_to_the_key, ".")
maze_to_exit = Signs(maze, Before_the_exit, ",")

def final_file(maze, filename):
    with open(filename, "w") as file:
        for row in maze:
            for elem in row:
                file.write(str(elem))
            file.write("\n")

final_file(maze, "maze-for-me-done.txt")