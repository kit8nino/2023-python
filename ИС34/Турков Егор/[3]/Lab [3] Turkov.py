from collections import deque
#1. проверка доступности пути и шаги
def possible_ways(coordsXY, maze):
    LenMazeY = len(maze[0])
    LenMazeX = len(maze)
    coordsX = coordsXY[0]
    coordsY = coordsXY[1]
    free_way = []

    if (coordsX - 1) >= 0 and maze[coordsX - 1][coordsY] == " ":
        coord_for_append = (coordsX - 1, coordsY)
        free_way.append(coord_for_append)

    if (coordsX + 1) < LenMazeX and maze[coordsX + 1][coordsY] == " ":
        coord_for_append = (coordsX + 1, coordsY)
        free_way.append(coord_for_append)

    if (coordsY - 1) >= 0 and maze[coordsX][coordsY - 1] == " ":
        coord_for_append = (coordsX, coordsY - 1)
        free_way.append(coord_for_append)

    if (coordsY + 1) < LenMazeY and maze[coordsX][coordsY + 1] == " ":
        coord_for_append = (coordsX, coordsY + 1)
        free_way.append(coord_for_append)

    return free_way
#2. A*
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

        for neighbor in possible_ways(current, maze):
            if neighbor in closed_list:
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)
    return open_list
#3. deep search
def get_neighbors(maze, cell: tuple[int, int]):
    row, col = cell
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    valid_neighbors = []
    for neighbor in neighbors:
        row, col = neighbor
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
            valid_neighbors.append(neighbor)
    return valid_neighbors

def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if current == end:
            return path
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

#4. определение входа, выхода, ключа
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

#5. решение лабиринта
pathToKey = dfs(maze, start, key)
pathToExit = a_star(maze, key, end)

for coords in pathToKey:
    x, y = coords
    maze[x][y] = "."

for coords in pathToExit:
    x, y = coords
    if maze[x][y] == ".":
        maze[x][y] = ";"
    else:
        maze[x][y] = ","

with open('maze-for-me-done.txt', 'w') as f:
    for line in maze:
        f.write("".join(line) + "\n")
