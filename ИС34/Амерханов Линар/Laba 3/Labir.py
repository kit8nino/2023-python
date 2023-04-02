# import turtle
#
# screen = turtle.Screen()
# screen.setup(600, 600)
# t = turtle.Turtle()
#
# # Размер клетки и чернота
# cell_size = 25
# t.hideturtle()
# screen.bgcolor("black")
#
# # Открытие файла с лабиринтом
# with open("MazeTest.txt", "r") as maze_file:
#     # Чтение строк из файла
#     maze_rows = maze_file.readlines()
#
#
#     # Проход по строкам
#     for i, row in enumerate(maze_rows):
#         # Проход по символам
#         for j, char in enumerate(row.strip()):
#             # Вычисление координат
#             x = -screen.window_width() / 2 + cell_size * j
#             y = screen.window_height() / 2 - cell_size * i
#
#             # Черепаха живи
#             t.penup()
#             t.goto(x, y)
#             t.pendown()
#
#             # Проходы в лаб
#             if char == "#":
#                 t.color("white")
#                 t.begin_fill()
#                 for razv in range(4):
#                     t.forward(cell_size)
#                     t.right(90)
#                 t.end_fill()
# turtle.done()
from math import sqrt

def manhattan(start, end):
    return sum(abs(val1 - val2) for val1, val2 in zip(start, end))


def available_paths(coordsXY, maze):
    LenMazeY = len(maze[0])
    LenMazeX = len(maze)
    coordsX = coordsXY[0]
    coordsY = coordsXY[1]
    av_path_list = []

    if maze[coordsX - 1][coordsY] == "#" and coordsX - 1 >= 0: #Север
        coord_for_append = [coordsX - 1, coordsY,]
        av_path_list.append(coord_for_append)

    if maze[coordsX][coordsY + 1] == "#" and coordsY + 1 <= LenMazeY:  #Восток
        coord_for_append = [coordsX, coordsY + 1]
        av_path_list.append(coord_for_append)

    if maze[coordsX + 1][coordsY] == "#" and coordsX + 1 <= LenMazeX: #Юг
        coord_for_append = [coordsX + 1, coordsY]
        av_path_list.append(coord_for_append)

    if maze[coordsX][coordsY - 1] == "#" and coordsY - 1 >= 0: #Запад
        coord_for_append = [coordsX, coordsY - 1]
        av_path_list.append(coord_for_append)

    return av_path_list

# a*
def a_star(maze, start, end):
    OpenList = [start]




with open('Maze.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]

for i in range(len(maze)):
     print(*maze[i])





start = [0, 0]
end = [18, 0]
print(available_paths(start, maze))
print(manhattan(start,end))


