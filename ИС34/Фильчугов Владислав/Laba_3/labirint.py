import heapq

# функция для чтения txt файла
def readmaze(file_name):
    with open(file_name) as f:
        maze = [list(line.strip()) for line in f]
    return maze

# вход и выход
def door(maze):
    for X in range(len(maze[0])):
        if maze[0][X] == " ":
            start = (0, X)
            break
    for X in range(len(maze[0])):
        if maze[len(maze) - 1][X] == " ":
            end = (len(maze) - 1, X)
            break
    return start, end

# поиск ключа
def find_key_position(maze):
    for i, g in enumerate(maze):
        if "*" in g:
            return(i, g.index("*"))

# Поиск пути от входа до ключа с помощью алгоритма Дейкстры
def Dijkstra_algorithm(maze, start, end):
    distances = {start: 0}
    queue = [(0, start, [start])]
    while queue:
        (cost, current, path) = heapq.heappop(queue)
        if current == end:
            return path
        if current not in distances or cost > distances[current]:
            continue
        for neighbor in available_paths(current, maze):
            if neighbor not in distances or cost + 1 < distances[neighbor]:
                distances[neighbor] = cost + 1
                heapq.heappush(queue, (cost + 1, neighbor, path + [neighbor]))
    return None
# функция для поиска доступных путей из текущей точки
def available_paths(current, maze):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    paths = []
    for neighbor in neighbors:
        x = current[0] + neighbor[0]
        y = current[1] + neighbor[1]
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "#":
            paths.append((x, y))
    return paths

# нахождения пути от ключа до выхода с помощью алгоритма А*
def A_star(maze, start, end):
    heap = [(0, start)]
    heapq.heapify(heap)
    visited = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while heap:
        current = heapq.heappop(heap)[1]
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)

            return path[::-1]

        visited.add(current)

        for neighbor in available_paths(current, maze):
            if neighbor == start or neighbor == key:
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor in visited and tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                if neighbor not in visited:
                    heapq.heappush(heap, (f_score[neighbor], neighbor))
    return []

# функция для определения эвристической оценки расстояния между двумя точками
def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

# создание нового лабиринта с отмеченными путями
def new_maze(maze, path, marker):
    for i, j in path:
        if maze[i][j] == " ":
            if marker == "." and (i, j) in path2:
                maze[i][j] = ";"
            else:
                maze[i][j] = marker
    return maze

# функция для записи обновленного лабиринта в txt файл
def new_file(maze, file_name):
    with open(file_name, "w") as f:
        for g in maze:
            f.write("".join(g)+"\n")

maze = readmaze("maze-for-u.txt")
start, end = door(maze)
key = find_key_position(maze)

path1 = Dijkstra_algorithm(maze, start, key)
path2 = A_star(maze, key, end)
maze = new_maze(maze, path1, ".")
maze = new_maze(maze, path2, ",")
new_file(maze, "maze-for-me-done.txt")