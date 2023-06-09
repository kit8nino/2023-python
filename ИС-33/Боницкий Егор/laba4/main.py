# -*- coding: utf-8 -*-

from Avatar import Avatar
from Mob import Mob

import turtle

H_MERGE = 495
W_MERGE = 800
WALL_SIZE = 2


def read_maze(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

        h = len(lines)
        w = len(lines[0]) - 1
        maze = []

        for line in lines:
            tmp_line = [0 if sym == "#" else 1 for sym in line[:-1]]
            maze.append(tmp_line[:])

    return h, w, maze


def main():
    input_file_name = "maze-for-u.txt"

    h, w, maze = read_maze(input_file_name)

    print("Координаты аватара:")
    avatar_x, avatar_y = int(input(f"0 <= x <= {w - 1}: ")), int(input(f"0 <= y <= {h - 1}: "))
    avatar_pos = (avatar_x, avatar_y)

    print("Координаты моба:")
    mob_x, mob_y = int(input(f"0 <= x < {w - 1}: ")), int(input(f"0 <= y < {h - 1}: "))
    mob_pos = (mob_x, mob_y)

    print("Координаты выхода:")
    exit_x, exit_y = int(input(f"0 <= y < {w - 1}: ")), int(input(f"0 <= y < {h - 1}: "))
    exit_pos = (exit_x, exit_y)

    turtle.setup(width=1700, height=1000)

    wall = turtle.Turtle()
    wall.shape('square')
    wall.color('black')
    wall.shapesize(WALL_SIZE / 20)
    wall.penup()
    wall.speed(5)

    for y in range(h):
        for x in range(w):
            if maze[y][x] == 0:
                wall.goto(x * WALL_SIZE - W_MERGE, -y * WALL_SIZE + H_MERGE)
                wall.stamp()

    avatar = Avatar(avatar_pos, 5, 'blue', maze, exit_pos)
    mob = Mob(mob_pos, 5, 'red')

    while avatar.getPos() != exit_pos and avatar.getPos() != mob.getPos():
        if avatar.getPos() != exit_pos and avatar.getPos() != mob.getPos():
            avatar.move()
        if avatar.getPos() != exit_pos and avatar.getPos() != mob.getPos():
            mob.move(maze, avatar.getPos())


if __name__ == "__main__":
    main()

"""
Входные данные
0
1
456
444
599
798
"""
