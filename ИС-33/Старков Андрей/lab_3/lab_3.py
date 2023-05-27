from queue import Queue

# Функция для импорта и преобразования исходного файла
def read_maze(fileMaze="maze-for-u.txt"):
    maze = [list(line.replace("#", "1").replace(" ", "0")) for line in open(fileMaze).read().split("\n")[:-1]]
    return maze


# Создание лабиринта, нахождение габаритов
try:
    maze = read_maze()
    size_x = len(maze)
    size_y = len(maze[0])
except Exception:
    print("Исходный файл не найден!")

# Функция отображения окресности точки
def near(x, y, maze):
    near = []
    if y == 0:
        if x == 0:
            near = [["#", maze[x][y + 1]],
                    [maze[x + 1][y], maze[x + 1][y + 1]]]
        elif x == (size_x - 1):
            near = [[maze[x - 1][y], maze[x - 1][y + 1]],
                    ["#", maze[x][y + 1]]]
        else:
            near = [[maze[x - 1][y], maze[x - 1][y + 1]],
                    ["#", maze[x][y + 1]],
                    [maze[x + 1][y], maze[x + 1][y + 1]]]
    elif y == (size_y - 1):
        if x == 0:
            near = [[maze[x][y - 1], "#"],
                    [maze[x + 1][y - 1], maze[x + 1][y]]]
        elif x == (size_x - 1):
            near = [[maze[x - 1][y - 1], maze[x - 1][y]],
                    [maze[x][y - 1], "#"]]
        else:
            near = [[maze[x - 1][y - 1], maze[x - 1][y]],
                    [maze[x][y - 1], "#"],
                    [maze[x + 1][y - 1], maze[x + 1][y]]]
    elif x == 0:
        near = [[maze[x][y - 1], "#", maze[x][y + 1]],
                [maze[x + 1][y - 1], maze[x + 1][y], maze[x + 1][y + 1]]]
    elif x == (size_x - 1):
        near = [[maze[x - 1][y - 1], maze[x - 1][y], maze[x - 1][y + 1]],
                [maze[x][y - 1], "#", maze[x][y + 1]]]
    else:
        near = [[maze[x - 1][y - 1], maze[x - 1][y], maze[x - 1][y + 1]],
                [maze[x][y - 1], "#", maze[x][y + 1]],
                [maze[x + 1][y - 1], maze[x + 1][y], maze[x + 1][y + 1]]]
    return near

# Функция определения точки аватара (начальной точки)
def sel_ava(maze):
    while 1:
        try:
            x = int(input(f"Введите координату X аватара(не больше {size_x - 1}):"))
            if x >= 0 and x < size_x:
                y = int(input(f"Введите координату Y аватара(не больше {size_y - 1}):"))
                if y >= 0 and y < size_y:
                    if str(maze[x][y]) == "1":
                        print(
                            "По введённым координатам находится стена! Попробуйте ещё раз! Окрестности выбранной точки:\n")
                        for line in near(x, y, maze):
                            print(line, "\n")
                    else:
                        return (x, y)
                else:
                    print("Введённое значение выходит за допустимый диапазон! Попробуйте ещё раз.")
                    continue
            else:
                print("Введённое значение выходит за допустимый диапазон! Попробуйте ещё раз.")
                continue
        except Exception:
            print("Вы ввели неверное значение! Попробуйте ещё раз.")

# Функция определения ключевой точки
def sel_key(maze):
    while 1:
        try:
            x = int(input(f"Введите координату X ключа(не больше {size_x - 1}):"))
            if x >= 0 and x < size_x:
                y = int(input(f"Введите координату Y ключа(не больше {size_y - 1}):"))
                if y >= 0 and y < size_y:
                    if str(maze[x][y]) == "1":
                        print(
                            "По введённым координатам находится стена! Попробуйте ещё раз! Окрестности выбранной точки:\n")
                        for line in near(x, y, maze):
                            print(line, "\n")
                    else:
                        return (x, y)
                else:
                    print("Введённое значение выходит за допустимый диапазон! Попробуйте ещё раз.")
                    continue
            else:
                print("Введённое значение выходит за допустимый диапазон! Попробуйте ещё раз.")
                continue
        except Exception:
            print("Вы ввели неверное значение! Попробуйте ещё раз.")

# Функция нахождения точки выхода
def sel_exit(maze):
    for y in range(size_y):
        if int(maze[size_x-1][y]) == 0:
            return (size_x - 1,y)

# Объявление и инициализация точек
start = sel_ava(maze)
key = sel_key(maze)
end = sel_exit(maze)

# Функция для определения возможных путей из текущей позиции
def get_moves(pos):
    moves = []
    if pos[0] > 0 and not int(maze[pos[0] - 1][pos[1]]):
        moves.append((pos[0] - 1, pos[1]))
    if pos[0] < size_x - 1 and not int(maze[pos[0] + 1][pos[1]]):
        moves.append((pos[0] + 1, pos[1]))
    if pos[1] > 0 and not int(maze[pos[0]][pos[1] - 1]):
        moves.append((pos[0], pos[1] - 1))
    if pos[1] < size_y - 1 and not int(maze[pos[0]][pos[1] + 1]):
        moves.append((pos[0], pos[1] + 1))
    return moves


# Функция для поиска пути с помощью поиска в ширину
def bfs(start, end):
    queue = Queue()
    queue.put((start, [start]))
    while not queue.empty():
        pos, path = queue.get()
        if pos == end:
            return path
        for move in get_moves(pos):
            if move not in path:
                queue.put((move, path + [move]))
    return None


# Запускаем поиск в ширину от аватара до ключа
path_bfs = bfs(start, key)

# Функция поиска пути в лабиринте с помощью алгоритма A*
def astar(maze, start, end):
    # Определяем размеры лабиринта
    rows = len(maze)
    cols = len(maze[0])

    # Определяем набор возможных направлений движения (вправо, вниз, влево, вверх)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Определяем эвристическую функцию
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Создаем два списка для открытых и закрытых вершин
    # Каждая вершина представляется в виде кортежа (y,x)
    open = [start]
    close = []

    # Создаем словарь, где для каждой точки будет храниться значение f = g + h, где g - стоимость пути от начальной точки до данной,
    # а h - эвристическое расстояние от данной точки до конечной
    g = {start: 0}
    f = {start: heuristic(start, end)}

    # Пока есть открытые вершины
    while open:
        # Находим вершину с минимальным значением F
        current = min(open, key=lambda x: f[x])

        # Если найдена конечная точка
        if current == end:
            # Создаем путь
            def get_key(val,my_dict):
                for key, value in my_dict.items():
                    if val == value:
                        return key

            path = []
            i=g[current]
            path.append(current)
            while i > 0:
                maybe = get_key(i - 1,g)
                if ((current[0]-maybe[0])**2 + (current[1]-maybe[1])**2)**(1/2) == 1:
                    current = maybe
                    path.append(maybe)
                    i-=1
                else:
                    del g[maybe]
            path.reverse()
            return path

        # Переносим текущую вершину из открытых в закрытые
        open.remove(current)
        close.append(current)

        # Проходимся по всем возможным направлениям движения
        for dir in dirs:
            # Вычисляем новую точку
            new_point = (current[0] + dir[0], current[1] + dir[1])

            # Проверяем, что новая точка находится в пределах лабиринта и не является стеной
            if new_point[0] >= 0 and new_point[0] < rows and new_point[1] >= 0 and new_point[1] < cols and int(maze[new_point[0]][new_point[1]]) == 0:
                # Вычисляем стоимость пути от начальной точки до новой точки
                temp_g = g[current] + 1

                # Если новая точка уже была рассмотрена, проверяем, что текущий путь до нее лучше, чем предыдущий
                if new_point in g:
                    if temp_g < g[new_point]:
                        g[new_point] = temp_g
                    else:
                        continue
                # Если новая точка еще не была рассмотрена, добавляем ее в открытые вершины
                else:
                    g[new_point] = temp_g
                    h = heuristic(new_point, end)
                    f[new_point] = g[new_point] + h
                    open.append(new_point)

    # Если путь не найден
    return None

# Запускаем поиск алгоритмом A* от ключа до выхода
path_astar = astar(maze, key, end)

# Заносим изменения в исходный лабиринт
try:
    # Заносим путь от аватара до ключа
    for point in path_bfs:
        maze[point[0]][point[1]] = "."

    # Заносим путь от ключа до выхода
    for point in path_astar:
        maze[point[0]][point[1]] = ","

    # Заносим ключевую точку
    maze[key[0]][key[1]] = "*"

    # Генерируем файл с пройдённым лабиринтом
    with open("maze-for-me-done.txt", "w") as f:
        f.write('\n'.join([''.join(map(str, line)) for line in maze]))
        print("Лабиринт успешно пройден!\n Получившийся путь находится в файле 'maze-for-me-done.txt' в папке со скриптом!")
except Exception:
    print("При поиске пути произошла ошибка!")


