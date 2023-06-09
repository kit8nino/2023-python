import heapq
# импорт и преобразование исходного файла
filename = "maze-for-u.txt"
maze = []

with open(filename, 'r') as f:
    for line in f:
        maze.append(list(line.strip()))

# Функция определения начальной точки
def find_start_point(lst):
    first_line = lst[0]
    for i in range(len(first_line)):
        if first_line[i] == ' ':
            start=(0,i)
            return start
    return -1
start = find_start_point(maze)

# Функция нахождения точки выхода
def end_point(lst):
    first_line = maze[len(maze)-1]
    for i in range(len(first_line)):
        if first_line[i] == ' ':
            start=(len(maze)-1,i)
            return start
    return -1
end = end_point(maze)



# определение ключевой точки

for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == "*":
            key = (x, y)
            break

# Определяем функцию для поиска выхода из лабиринта.
def greedy_algorithm(maze, start, goal):
    # Создаем приоритетную очередь
    queue = []
    heapq.heappush(queue, (heuristic(start, goal), start)) #начинаем с координат старта
    # Создаем список посещенных координат
    visited = set()
    # Создаем словарь для хранения предыдущих шагов
    came_from = {}

    while queue:
        # Получаем текущую координату
        current = heapq.heappop(queue)[1]

        # Если текущая координата соответствует цели, мы нашли выход из лабиринта
        if current == goal:
            return construct_path(came_from, start, goal)

        # Добавляем текущую координату в список посещенных
        visited.add(current)

        # Получаем список доступных координат из текущего местоположения
        possible_moves = get_possible_moves(maze, current)

        # Добавляем координаты в очередь в соответствии со значением эвристической функции
        for move in possible_moves:
            if move not in visited:
                heapq.heappush(queue, (heuristic(move, goal), move))
                came_from[move] = current

    # Если выход из лабиринта не найден
    return None

def get_possible_moves(maze, current):
    # Получаем размеры лабиринта
    rows, cols = len(maze), len(maze[0])
    moves = []

    # Проверяем возможные шаги в каждом направлении
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        row, col = current[0] + dx, current[1] + dy
        # Проверяем, что координата находится в лабиринте и доступна
        if 0 <= row < rows and 0 <= col < cols and maze[row][col] != "#":
            moves.append((row, col))

    return moves

def heuristic(current, goal):
    # Вычисляем Евклидово расстояние от текущей координаты до целевой координаты
    return ((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2) ** 0.5

def construct_path(came_from, start, goal):
    current = goal
    path = [current]

    while current != start:
        current = came_from[current]
        path.append(current)

    # Переворачиваем путь, так как мы добавляли координаты в обратном порядке
    path.reverse()

    return path


def heuristic(a, b):
    """
    Реализация эвристической функции для A*
    """
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def astar(array, start, goal):
    """
    Реализация алгоритма A*
    """
    # Инициализируем очередь, очередь приоритетов и список посещенных узлов
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    # Помещаем начальную вершину в очередь
    heapq.heappush(oheap, (fscore[start], start))

    # Цикл пока очередь не опустеет
    while oheap:

        # Берем первый элемент очереди
        current = heapq.heappop(oheap)[1]

        # Если мы достигли цели, то возвращаем путь
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        # Кладем текущую вершину в список посещенных
        close_set.add(current)

        # Просматриваем все соседние вершины
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j

            # Выбрасываем вершины, которые выходят за границы лабиринта
            if neighbor[0] < 0 or neighbor[0] >= len(array):
                continue
            if neighbor[1] < 0 or neighbor[1] >= len(array[0]):
                continue

            # Выбрасываем блокированные вершины
            if array[neighbor[0]][neighbor[1]] == "#":
                continue

            # Вычисляем стоимость пути через текущую вершину
            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            # Добавляем новый узел в очередь приоритетов
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            # Обновляем лучший путь до вершины
            came_from[neighbor] = current
            gscore[neighbor] = tentative_g_score
            fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
            heapq.heappush(oheap, (fscore[neighbor], neighbor))

    # Если путь не был найден, возвращаем None
    return None
Before_the_exit = astar(maze,key, end)

def Signs(maze, path, symbol):
    for cord in path:
        x, y = cord
        maze[x][y] = symbol
        x, y = key
        maze[x][y] = "*"
    return maze

res = greedy_algorithm(maze, start, key)


maze_to_the_key = Signs(maze, res, ".")
maze_to_exit = Signs(maze, Before_the_exit, ",")



def final_file(maze, filename):
    with open(filename, "w") as file:
        for row in maze:
            for elem in row:
                file.write(str(elem))
            file.write("\n")

final_file(maze, "maze-for-me.txt")