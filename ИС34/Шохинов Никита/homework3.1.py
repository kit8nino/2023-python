import heapq
from typing import List, Tuple

def read_maze(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    maze = [list(line) for line in lines]
    return maze

def find_points(maze):
    start = None
    end = None
    for i in range(len(maze[0])):
        if maze[0][i] == " ":
            start = (0, i)
        if maze[len(maze)-1][i] == " ":
            end = ((len(maze)-1), i)
    return start, end

def find_key(maze):
    key = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "*":
                key = (i, j)
    return key

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

def astar(start: Tuple[int, int], end: Tuple[int, int], maze: List[List[str]]) -> List[Tuple[int, int]]:

    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> float:
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

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

def new_maze(maze, path, mark):
    for cord in path:
        x, y = cord
        maze[x][y] = mark
    return maze

def new_file(maze, filename):
    with open(filename, "w") as file:
        for row in maze:
            for elem in row:
                file.write(str(elem))
            file.write("\n")

maze = read_maze("maze-for-u.txt")
start, end = find_points(maze)
key = find_key(maze)

path1 = dijkstra(start, key, maze)
path2 = astar(key, end, maze)

maze = new_maze(maze, path1, ".")
maze = new_maze(maze, path2, ",")
x, y = key
maze[x][y] = "*"

new_file(maze, "maze-for-me-done.txt")
