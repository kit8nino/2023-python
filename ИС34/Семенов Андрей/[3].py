import heapq
from typing import List, Tuple

def read_maze(file):
    with open(file, 'r') as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze

# Функция нахождения точки входа
def start_pos(maze):
    for Y in range(len(maze[0])):
        if maze[0][Y] == " ":
            start = (0, Y)
            break
    return start

# Функция нахождения точки выхода
def end_pos(maze):
    for Y in range(len(maze[0])):
        if maze[len(maze) - 1][Y] == " ":
            end = (len(maze) - 1, Y)
            break
    return end

# Функция нахождения ключа
def key_pos(maze):
    key = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "*":
                key = (i, j)
    return key

#Алгоритм Дейкстры
def dijkstra(start: Tuple[int, int], end: Tuple[int, int], maze: List[List[int]]) -> List[Tuple[int, int]]:
    m, n = len(maze), len(maze[0])
    visited = {(i, j): False for i in range(m) for j in range(n)}
    distance = {(i, j): float("inf") for i in range(m) for j in range(n)}
    prev = {(i, j): None for i in range(m) for j in range(n)}
    distance[start] = 0
    queue = {start}
    while len(queue) > 0:
        u = min(queue, key=lambda x: distance[x])
        queue.remove(u)
        visited[u] = True
        if u == end:
            path = []
            while prev[u]:
                path.append(u)
                u = prev[u]
            path.append(start)
            path.reverse()
            return path
        for v in [(u[0]-1, u[1]), (u[0]+1, u[1]), (u[0], u[1]-1), (u[0], u[1]+1)]:
            if (0 <= v[0] < m) and (0 <= v[1] < n) and not visited[v] and maze[v[0]][v[1]] != "#":
                alt = distance[u] + 1
                if alt < distance[v]:
                    distance[v] = alt
                    prev[v] = u
                    queue.add(v)
    return []

#A*
def astar(start: Tuple[int, int], end: Tuple[int, int], maze: List[List[str]]) -> List[Tuple[int, int]]:
    open_set = [(0, start)]
    closed_set = set()
    cost = {start: 0}
    came_from = {}
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        closed_set.add(current)
        for row, col in [(current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0], current[1] - 1), (current[0], current[1] + 1)]:
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
                tentative_cost = cost[current] + 1
                if (row, col) in closed_set and tentative_cost >= cost.get((row, col), float("inf")):
                    continue
                if tentative_cost < cost.get((row, col), float("inf")):
                    cost[(row, col)] = tentative_cost
                    came_from[(row, col)] = current
                    heapq.heappush(open_set, (tentative_cost + heuristic((row, col), end), (row, col)))
    return []

#Эвристическая стоимость
def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> float:
        return abs(b[0] - a[0]) + abs(b[1] - a[1])
    
def updated_maze(maze, path, mark):
    for pos in path:
        x, y = pos
        maze[x][y] = mark
    return maze

def new_file(maze, filename):
    with open(filename, "w") as file:
        for row in maze:
            for elem in row:
                file.write(str(elem))
            file.write("\n")

def main():
    maze = read_maze("maze-for-u.txt")
    start = start_pos(maze)
    end = end_pos(maze)
    key = key_pos(maze)
    go_to_key = dijkstra(start, key, maze)
    go_to_exit = astar(key, end, maze)
    maze = updated_maze(maze, go_to_key, ".")
    maze = updated_maze(maze, go_to_exit, ",")
    x, y = key
    maze[x][y] = "*"
    new_file(maze, "maze-for-me-done.txt")
    print("Лабиринт пройден. Результат можно посмотреть в файле 'maze-for-me-done.txt'.")
main()