from queue import PriorityQueue
from queue import Queue

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

def valid_moves(maze, current_position):
    moves = []
    x, y = current_position
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d in directions:
        dx, dy = d
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
            moves.append((nx, ny))
    return moves

def bfs(maze, start, end):
    # Создаём очередь
    queue = Queue()
    queue.put(start)
    visited = {start: None}
    # Определяем возможные направления движения
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Запускаем цикл поиска пути
    while not queue.empty():
        current = queue.get()
        # Если точка является конечной, то создаём путь до неё
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]
        # Перебираем возможные направления движения
        for direction in directions:
            # Вычисляем следующую точку
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            # Проверяем, находится ли следующая точка в лабиринте и не была ли она уже посещена
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and neighbor not in visited and maze[neighbor[0]][neighbor[1]] != '#':
                # Добавляем следующую точку в очередь
                queue.put(neighbor)
                visited[neighbor] = current
    return None
Up_to_the_key = bfs(maze, start, key)

def astar(maze, start, end):
    explored = set()
    pq = PriorityQueue()
    pq.put((0, start))
    path = {}
    # Начинаем алгоритм A*
    while not pq.empty():
        # Извлекаем клетку из очереди с минимальным приоритетом
        current_cost, current_node = pq.get()

        # Добавляем клетку в список посещенных
        explored.add(current_node)

        # Если мы нашли конечную клетку, то строим путь
        if current_node == end:
            return build_path(start, end, path)

        # Перебираем соседние клетки
        for child_node in get_neighbors(maze, current_node):
            if child_node in explored:
                continue
            new_cost = current_cost + 1
            if child_node not in [item[1] for item in pq.queue]:
                # Вычисляем эвристическую функцию
                h = heuristic(child_node, end)

                # Добавляем соседнюю клетку в очередь с приоритетами
                pq.put((new_cost + h, child_node))
                path[child_node] = current_node

            # Если соседняя клетка уже была добавлена в очередь, но новый путь до нее лучше, то обновляем путь
            elif new_cost < current_cost(child_node):
                pq.put((new_cost + h, child_node))
                path[child_node] = current_node
    return None

def get_neighbors(maze, node):
    i, j = node

    # Перебираем соседние клетки
    neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    valid_neighbors = []

    for neighbor in neighbors:
        x, y = neighbor

        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
            valid_neighbors.append(neighbor)

    return valid_neighbors

def heuristic(node, end):
    # Манхэттенское расстояние
    return abs(node[0] - end[0]) + abs(node[1] - end[1])

def build_path(start, end, path):
    # Строим путь от конечной клетки до начальной
    node = end
    path_list = [end]

    while node != start:
        node = path[node]
        path_list.append(node)
    return path_list[::-1]
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