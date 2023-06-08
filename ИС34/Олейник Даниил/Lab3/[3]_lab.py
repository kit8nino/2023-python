from collections import deque
import heapq

POSSIBLE_WAYS = ('N', 'S', 'W', 'E')

def heuristic(coord, target):
    x1, y1 = map(int, coord)
    x2, y2 = map(int, target)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def is_coord_in_maze(maze, coord):
    len_x, len_y = len(maze), len(maze[0])
    if coord[0] < 0 or coord[0] >= len_x:
        return False
    if coord[1] < 0 or coord[1] >= len_y:
        return False
    return True

def is_path_clean(maze, coord):
    coord_tuple = tuple(coord)
    if maze[coord_tuple[0]][coord_tuple[1]] != '#':
        return True
    return False

def step(coord, direction):
    if direction == 'N':
        return [coord[0], coord[1] - 1].copy()
    elif direction == 'S':
        return [coord[0], coord[1] + 1].copy()
    elif direction == 'E':
        return [coord[0] + 1, coord[1]].copy()
    elif direction == 'W':
        return [coord[0] - 1, coord[1]].copy()

def bfs(maze, start, target):
    queue = deque()
    visited = set()
    parent = {}
    start = tuple(start)
    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()

        if current == target:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        for direction in POSSIBLE_WAYS:
            next_coord = tuple(step(list(current), direction))
            if not is_coord_in_maze(maze, next_coord) or not is_path_clean(maze, next_coord):
                continue

            if next_coord not in visited:
                parent[next_coord] = current
                queue.append(next_coord)
                visited.add(next_coord)

    return None


def a_star(maze, start, target):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, target)}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == target:
            return reconstruct_path(came_from, current)

        for direction in POSSIBLE_WAYS:
            next_coord = step(current, direction)

            if not is_coord_in_maze(maze, next_coord) or not is_path_clean(maze, next_coord):
                continue

            tentative_g_score = g_score[current] + 1

            next_coord = tuple(next_coord)

            if next_coord in g_score and tentative_g_score >= g_score[next_coord]:
                continue

            came_from[next_coord] = current
            g_score[next_coord] = tentative_g_score
            f_score[next_coord] = tentative_g_score + heuristic(next_coord, target)
            heapq.heappush(open_list, (f_score[next_coord], next_coord))

    return None


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]


start = [0, 1]  # Starting coordinate

for e in range(len(maze[0]) - 1, -1, -1):
    if maze[len(maze) - 1][e] == ' ':
        end_point = (len(maze) - 1, e)
        break



start_point = [0, 1]
while True:
    x = int(input("Координата сокровища по X: "))
    y = int(input("Координата сокровища по Y: "))
    if maze[x][y] != "#":
        treja_is_here = (x, y)
        break
    print("Стена! Выбери другие координаты")

for e in range(len(maze[0]) - 1, -1, -1):
    if maze[len(maze) - 1][e] == ' ':
        end_point = (len(maze) - 1, e)
        break
print("Путь найден!")


# BFS
path_start_to_treja = bfs(maze, start, treja_is_here)
#print(path_start_to_treja)

# A*
path_treja_to_end = a_star(maze, treja_is_here, end_point)
#print(path_treja_to_end)
if path_start_to_treja is not None:
    for coord in path_start_to_treja:
        maze[coord[0]][coord[1]] = '.'

if path_treja_to_end is not None:
    for coord in path_treja_to_end:
        maze[coord[0]][coord[1]] = ','

maze[treja_is_here[0]][treja_is_here[1]] = "*"

# Запись пути в файл
with open("maze-for-me-done.txt", "w") as txt_file:
    for line in maze:
        txt_file.write(''.join(line) + '\n')
