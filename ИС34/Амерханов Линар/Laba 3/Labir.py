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

with open('Maze.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]
for i in range(len(maze)):
    print(*maze[i])