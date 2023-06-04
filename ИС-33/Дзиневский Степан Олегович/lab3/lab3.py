import heapq

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


def bfs(maze, start, end):
    queue = [start]
    visited = set()
    came_from = {}
    while queue:
        current = queue.pop(0)
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path
        visited.add(current)
        for neighbor in available_paths(current, maze):
            if neighbor not in visited:
                came_from[neighbor] = current
                queue.append(neighbor)
                visited.add(neighbor)
    return None


def a_star(maze, start, end):
    heap = [(0, start)]
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
            path.reverse()
            return path

        visited.add(current)

        for neighbor in available_paths(current, maze):
            tentative_g_score = g_score[current] + 1
            if neighbor in visited and tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                if neighbor not in visited:
                    heapq.heappush(heap, (f_score[neighbor], neighbor))

    # Если A* не находит путь, функция возвращает None
    return None


def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]


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


pathToKey = bfs(maze, start, key)
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
