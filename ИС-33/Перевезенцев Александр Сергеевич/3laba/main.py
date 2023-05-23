def available_paths(coordsXY, maze):
    LenMazeY = len(maze[0])
    LenMazeX = len(maze)
    coordsX = coordsXY[0]
    coordsY = coordsXY[1]
    possibleWays = []

    if (coordsX - 1) >= 0 and maze[coordsX - 1][coordsY] == " ": #Север
        coord_for_append = (coordsX - 1, coordsY)
        possibleWays.append(coord_for_append)

    if (coordsY + 1) < LenMazeY and maze[coordsX][coordsY + 1] == " ":  #Восток
        coord_for_append = (coordsX, coordsY + 1)
        possibleWays.append(coord_for_append)

    if (coordsX + 1) < LenMazeX and maze[coordsX + 1][coordsY] == " ": #Юг
        coord_for_append = (coordsX + 1, coordsY)
        possibleWays.append(coord_for_append)

    if (coordsY - 1) >= 0 and maze[coordsX][coordsY - 1] == " ": #Запад
        coord_for_append = (coordsX, coordsY - 1)
        possibleWays.append(coord_for_append)
    return possibleWays


def greedy_search(maze, start, end):
    # Инициализируем список открытых и закрытых вершин
    open_list = [start]
    closed_list = []

    # Инициализируем словарь, в котором будем хранить "родителей" вершин
    came_from = {}

    # Ищем путь от начала до конца
    while open_list:
        # Выбираем из списка открытых вершин вершину с наименьшей эвристической оценкой
        current = min(open_list, key=lambda x: heuristic(x, end))

        # Если мы нашли конечную точку, составляем путь и возвращаем его
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        # Перемещаем текущую вершину из списка открытых в список закрытых вершин
        open_list.remove(current)
        closed_list.append(current)

        # Ищем все соседние вершины текущей вершины
        for neighbor in available_paths(current, maze):
            # Если соседняя вершина уже в списке закрытых, пропускаем ее
            if neighbor in closed_list:
                continue

            # Если соседняя вершина еще не в списке открытых, добавляем ее туда
            if neighbor not in open_list:
                open_list.append(neighbor)

            # Добавляем текущую вершину как "родителя" для соседней вершины
            came_from[neighbor] = current

    # Если жадный алгоритм не находит путь, функция возвращает None
    return None


def a_star(maze, start, end):
    open_list = [start]
    closed_list = []
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_list:
        current = min(open_list, key=lambda x: f_score[x])
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in available_paths(current, maze):
            if neighbor in closed_list:
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)

    # Если A* не находит путь, функция возвращает None
    return None


def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

# Читаем лабиринт из файла
with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]

# Ищем начальную, конечную точки и точку с ключом в лабиринте
for Y in range(len(maze[0])):
    if maze[0][Y] == " ":
        start = (0, Y)
        break

for Y in range(len(maze[0])):
    if maze[len(maze) - 1][Y] == " ":
        end = (len(maze) - 1, Y)
        break

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "*":
            key = (i, j)
            maze[i][j] = " "
            break

# Ищем путь от начала до точки с ключом с помощью жадного алгоритма
pathToKey = greedy_search(maze, start, key)

# Ищем путь от точки с ключом до конца с помощью алгоритма A*
pathToExit = a_star(maze, key, end)

#от точки-ключа до выхода  "."
for coords in pathToKey:
    x, y = coords
    maze[x][y] = "."

#от точки-ключа до выхода  ","
for coords in pathToExit:
    x, y = coords
    maze[x][y] = ","

# Записываем измененный лабиринт в файл
with open('maze-for-me-done.txt', 'w') as f:
    for line in maze:
        f.write("".join(line) + "\n")

