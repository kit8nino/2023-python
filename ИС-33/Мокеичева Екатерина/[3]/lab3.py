from collections import deque
# Импорт с заменой символов и последующим превращением в двумерный массив исходного файла
def readMaze(file="maze-for-u.txt"):
    maze = [list(line.replace("#", "1").replace(" ", "0")) for line in open(file).read().split("\n")[:-1]]
    return maze

# Определение ключевой точки
def key(maze):
    while 1:
        try:
            x = int(input(f"Введите координату X ключевой точки в пределах от 0 до {len(maze)-1}):"))
            if x >= 0 and x < len(maze):
                y = int(input(f"Введите координату Y ключевой точки в пределах от 0 до {len(maze[0]) - 1}):"))
                if y >= 0 and y < len(maze[0]):
                    if str(maze[x][y]) == "1":
                        print("По этим координатам находится стена! Попробуйте ещё раз!")
                    else:
                        return (x, y)
                else:
                    print("Введённое значение вне диапазона! Попробуйте ещё раз!")
                    continue
            else:
                print("Введённое значение вне диапазона! Попробуйте ещё раз!")
                continue
        except Exception:
            print("Вы ввели неверное значение! Попробуйте ещё раз.")

# Функция определения координат выхода
def end(maze):
    for y in range(len(maze[0])):
        if maze[len(maze)-1][y] == '0':
            return (len(maze)- 1,y)

# Функция определения координат старта
def start(maze):
    for y in range(len(maze[0])):
        if maze[0][y] == '0':
            return (0,y)

# Алгоритм поиска в ширину
def bfs(maze, start, end):
    queue = deque([start])
    visited = set([start])
    path = {start: [start]}
    while queue:
        vertex = queue.popleft()
        if vertex == end:
            return path[vertex] # путь найден
        for neighbor in get_neighbors(maze, vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path[neighbor] = path[vertex] + [neighbor]
    return None # путь не найден

# Функция для нахождения свободных ячеек поблизости
def get_neighbors(maze, vertex):
    rows, cols = len(maze), len(maze[0])
    r, c = vertex
    candidates = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
    result = []
    for row, col in candidates:
        if 0 <= row < rows and 0 <= col < cols and maze[row][col] == "0":
            result.append((row, col))
    return result

# Эвристическая оценка расстояния от вершины до вершины
def heuristic(start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

# Алгоритм А*
def A_star(maze, start, end):
        open_set = [start]
        closed_set = []
        came_from = {}
        g_score = {start:0}
        f_score = {start:heuristic(start, end)}
        while len(open_set) > 0:
            current = min(open_set, key=lambda x:f_score[x])
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return list(reversed(path)) 
            open_set.remove(current)
            closed_set.append(current)
            for neighbor in get_neighbors(maze, current):
                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + 1 
                if neighbor not in open_set:
                    open_set.append(neighbor)
                elif tentative_g_score >= g_score[neighbor]:
                    continue
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
        return None

def main():
    # Создаём лабиринт
    maze = readMaze()
    # Объявляем ключевую точку
    keyPoint = key(maze)
    # Находим путь от старта до ключевой точки алгоритмом поиска в ширину
    pathBfs = bfs(maze,start(maze),keyPoint)
    # Находим путь от ключевой точки до выхода алгоритмом А*
    pathAstar = A_star(maze, keyPoint, end(maze))
    # Заносим путь от старта до ключа в лабиринт
    for point in pathBfs:
        maze[point[0]][point[1]] = "."

    # Заносим путь от ключа до выхода в лабиринт
    for point in pathAstar:
        maze[point[0]][point[1]] = ","

    # Заносим ключевую точку в лабиринт
    maze[keyPoint[0]][keyPoint[1]] = "*"

    # Генерируем файл с пройдённым лабиринтом
    with open("maze-for-me-done.txt", "w") as f:
        f.write('\n'.join([''.join(map(str, line)) for line in maze]))
        print("Лабиринт пройден!\nПуть находится в файле 'maze-for-me-done.txt'!")

# Запуск работы программы
main()


