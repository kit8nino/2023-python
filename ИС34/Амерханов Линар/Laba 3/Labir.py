import tkinter as tk
def mark_path(maze, path):
    for coords in path:
        x, y = coords
        maze[x][y] = "X"
    return maze
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
        if current == end:
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

with open('Maze.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]

start = (0, 1)
end = (19, 18)


path = a_star(maze, start, end)

with open('maze-for-me-done.txt', 'w') as f:
    for row in maze:
        f.write("".join(row) + "\n")

if path is not None:
    maze = mark_path(maze, path)
    with open('maze-for-me-done.txt', 'w') as f:
        for row in maze:
            f.write("".join(row) + "\n")
else:
    print("Пути для выхода нет.")
