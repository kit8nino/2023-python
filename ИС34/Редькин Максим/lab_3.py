import heapq
from typing import List, Tuple

def read_maze(file_name):
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    maze = [list(line) for line in lines]
    return maze

def start_end_points(maze):
    start = None
    end = None
    for i in range(len(maze[0])):
        if maze[0][i] == " ":
            start = (0, i)
        if maze[len(maze)-1][i] == " ":
            end = ((len(maze)-1), i)
    return start, end

def key_points(maze):
    key = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "*":
                key = (i, j)
    return key

def Dijkstra(start: Tuple[int, int], end: Tuple[int, int], maze: List[List[int]]) -> List[Tuple[int, int]]:
    m, n = len(maze), len(maze[0])
    visited = {(i, j): False for i in range(m) for j in range(n)}
    distance = {(i, j): float("inf") for i in range(m) for j in range(n)}
    previous = {(i, j): None for i in range(m) for j in range(n)}
    distance[start] = 0
    queue = {start}
    while len(queue) > 0:
        u = min(queue, key=lambda x: distance[x])
        queue.remove(u)
        visited[u] = True
        if u == end:
            path = []
            while previous[u]:
                path.append(u)
                u = previous[u]
            path.append(start)
            path.reverse()
            return path
        for v in [(u[0]-1, u[1]), (u[0]+1, u[1]), (u[0], u[1]-1), (u[0], u[1]+1)]:
            if (0 <= v[0] < m) and (0 <= v[1] < n) and not visited[v] and maze[v[0]][v[1]] != "#":
                alt = distance[u] + 1
                if alt < distance[v]:
                    distance[v] = alt
                    previous[v] = u
                    queue.add(v)
    return []

def Astar(start: Tuple[int, int], end: Tuple[int, int], maze: List[List[str]]) -> List[Tuple[int, int]]:

    def Heurit(a: Tuple[int, int], b: Tuple[int, int]) -> float:
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    open_set = [(0, start)]
    closed_set = set()

    expenses = {start: 0}
    came_from = {}

    while open_set:
        Now = heapq.heappop(open_set)[1]
        if Now == end:
            path = []
            while Now in came_from:
                path.append(Now)
                Now = came_from[Now]
            path.append(start)
            path.reverse()
            return path
        closed_set.add(Now)
        for row, col in [(Now[0] - 1, Now[1]), (Now[0] + 1, Now[1]), (Now[0], Now[1] - 1), (Now[0], Now[1] + 1)]:
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
                estimated_costs = expenses[Now] + 1
                if (row, col) in closed_set and estimated_costs >= expenses.get((row, col), float("inf")):
                    continue
                if estimated_costs < expenses.get((row, col), float("inf")):
                    expenses[(row, col)] = estimated_costs
                    came_from[(row, col)] = Now
                    heapq.heappush(open_set, (estimated_costs + Heurit((row, col), end), (row, col)))
    return []

def new_maze(maze, path, mark):
    for cord in path:
        x, y = cord
        maze[x][y] = mark
    return maze

def new_file(maze, file_name):
    with open(file_name, "w") as file:
        for row in maze:
            for elem in row:
                file.write(str(elem))
            file.write("\n")

maze = read_maze("maze-for-u.txt")
start, end = start_end_points(maze)
key = key_points(maze)

path1 = Dijkstra(start, key, maze)
path2 = Astar(key, end, maze)

maze = new_maze(maze, path1, ".")
maze = new_maze(maze, path2, ",")
x, y = key
maze[x][y] = "*"

new_file(maze, "maze-for-me-done.txt")