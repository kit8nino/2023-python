
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


def a_star(maze,start,end):
    openList = [start]
    closedList = []
    cameFrom = {}
    gScore = {start: 0}
    fScore = {start: heuristic(start, end)} # Текущая оценка расстояния от стартовой точки до целевой
    while openList:
        current = min(openList, key=lambda x: fScore[x])
        if end[0]-3 <= current[0] <= end[0]+3 and end[1]-3 <= current[1] <= end[1]+3:
            path = [end]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            return path[::-1]
        openList.remove(current)
        closedList.append(current)

        for neighbor in available_paths(current, maze):
            if neighbor in closedList:
                continue
            tentative_gScore = gScore[current] + 1
            if neighbor not in openList:
                openList.append(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, end)
    return None

def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]

start = (0, 1)
end = (599, 799)
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == '*':
            key = (i, j)
            break

pathToKey = a_star(maze, start, key)
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