import heapq


def read_maze_file(file_path):
    maze = []
    with open(file_path, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

# Функция для поиска начальной координаты в лабиринте.
def find_start(maze):
    for y in range(len(maze[0])):
        if maze[0][y] == ' ':
            return (0, y)


def find_exit(maze):
    for y in range(len(maze[0])):
        if maze[len(maze) - 1][y] == ' ':
            return (len(maze) - 1, y)


def find_key(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '*':
                return (i, j)

# Функция для получения соседних координат от заданной координаты в лабиринте.
def get_neighbors(maze, x, y):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Верх, низ, лево, право
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#':
            neighbors.append((new_x, new_y))
    return neighbors

# Функция для выполнения поиска в глубину от начальной координаты до ключа в лабиринте.
def depth_first_search(maze, start_coord, key_coord):
    stack = [start_coord]
    visited = set()
    paths = {start_coord: []}

    while stack:
        x, y = stack.pop()
        if (x, y) == key_coord:
            return paths[(x, y)] + [(x, y)]
        if (x, y) in visited:
            continue
        visited.add((x, y))
        neighbors = get_neighbors(maze, x, y)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                paths[neighbor] = paths[(x, y)] + [(x, y)]



def heuristic(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(maze, key_coord, exit_coord):
    heap = [(0, key_coord)]
    path_costs = {key_coord: 0}
    paths = {key_coord: []}

    while heap:
        cost, coord = heapq.heappop(heap)
        if coord == exit_coord:  # Если достигнута координата выхода, возвращаем путь
            return paths[coord] + [coord]
        neighbors = get_neighbors(maze, *coord)
        for neighbor in neighbors:
            new_cost = path_costs[coord] + 1
            if neighbor not in path_costs or new_cost < path_costs[neighbor]:
                path_costs[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, exit_coord)  # Приоритет = стоимость пути + эвристическое значение
                heapq.heappush(heap, (priority, neighbor))
                paths[neighbor] = paths[coord] + [coord]



def update_maze_with_path(maze, path, symbol):
    for coord in path:
        x, y = coord
        maze[x][y] = symbol

# функция для записи в файл
def save_maze_to_file(maze, file_path):
    with open(file_path, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

# Основная часть программы
maze = read_maze_file('maze-for-u.txt')
start_coord = find_start(maze)
key_coord = find_key(maze)
exit_cord = find_exit(maze)

# поиск пути от начальной координаты до ключа с использованием поиска в глубину
dfs_path = depth_first_search(maze, start_coord, key_coord)

if dfs_path:
    update_maze_with_path(maze, dfs_path, '.')
    a_star_path = a_star_search(maze, key_coord, exit_cord)

    if a_star_path:
        # Обновляем лабиринт с путем от ключа до выхода, путь запятыми
        update_maze_with_path(maze, a_star_path, ',')

        x, y = key_coord
        maze[x][y] = '*'

        # Сохраняем лабиринт в файл
        save_maze_to_file(maze, 'maze-for-me-done.txt')
        print("Маршрут найден")
    else:
        print("Невозможно найти путь от ключа до выхода.")
else:
    print("Невозможно найти путь от начальной координаты до ключа.")