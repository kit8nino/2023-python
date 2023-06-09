# -*- coding: utf-8 -*-

from turtle import Turtle

H_MERGE = 495
W_MERGE = 800
WALL_SIZE = 2


class Mob(Turtle):
    def __init__(self, coords, speed, color):
        super().__init__()
        self.penup()

        self.__pos = coords
        self.goto(coords[1] * WALL_SIZE - W_MERGE, -coords[0] * WALL_SIZE + H_MERGE)

        self.speed(speed)
        self.shape('square')
        self.color(color)
        self.shapesize(WALL_SIZE / 20)

    def getPos(self):
        return self.__pos

    def move(self, maze, target):
        move_y, move_x = self.greedy(maze, self.__pos, target)[1]
        self.goto(move_x * WALL_SIZE - W_MERGE, -move_y * WALL_SIZE + H_MERGE)
        self.__pos = move_y, move_x

    def greedy(self, maze, start, end):
        open_list = [(start, 0)]
        closed_list = set()
        came_from = {}

        while len(open_list) > 0:
            current, _ = open_list.pop(0)
            if current == end:
                return self.path(came_from, end)

            closed_list.add(current)
            for neighbor in self.get_neighbors(current, maze):
                if neighbor in closed_list or maze[neighbor[0]][neighbor[1]] == 0:
                    continue
                if neighbor not in [x[0] for x in open_list]:
                    came_from[neighbor] = current
                    priority = self.manhattan_distance(neighbor, end)
                    open_list.append((neighbor, priority))

            open_list.sort(key=lambda x: x[1])

        return None

    def get_neighbors(self, point, maze):
        x, y = point
        neighbors_list = []

        if x > 0:
            neighbors_list.append((x - 1, y))
        if y > 0:
            neighbors_list.append((x, y - 1))
        if x < len(maze) - 1:
            neighbors_list.append((x + 1, y))
        if y < len(maze[0]) - 1:
            neighbors_list.append((x, y + 1))

        return neighbors_list

    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.insert(0, current)
        return total_path
