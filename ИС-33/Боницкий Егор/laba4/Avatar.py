# -*- coding: utf-8 -*-

from turtle import Turtle

H_MERGE = 495
W_MERGE = 800
WALL_SIZE = 2


class Avatar(Turtle):
    def __init__(self, coords, speed, color, maze, target):
        super().__init__()
        self.penup()

        self.__pos = coords
        self.goto(coords[1] * WALL_SIZE - W_MERGE, -coords[0] * WALL_SIZE + H_MERGE)

        self.speed(speed)
        self.shape('square')
        self.color(color)
        self.shapesize(WALL_SIZE / 20)

        self.path = self.astar(maze, self.__pos, target)
        self.step = 1

    def getPos(self):
        return self.__pos

    def move(self):
        self.goto(self.path[self.step][1] * WALL_SIZE - W_MERGE, -self.path[self.step][0] * WALL_SIZE + H_MERGE)
        self.__pos = self.path[self.step]
        self.step += 1

    def astar(self, maze, start, end):
        open_list = [start]
        closed_list = []
        g_scores = {start: 0}
        f_scores = {start: self.manhattan_distance(start, end)}
        came_from = {}

        while open_list:
            current = min(open_list, key=lambda x: f_scores[x])

            if current == end:
                return self.path(came_from, end)

            open_list.remove(current)
            closed_list.append(current)

            for neighbor in self.get_neighbors(current, maze):
                if neighbor in closed_list or maze[neighbor[0]][neighbor[1]] == 0:
                    continue

                tentative_g_score = g_scores[current] + 1

                if neighbor not in open_list:
                    open_list.append(neighbor)
                elif tentative_g_score >= g_scores[neighbor]:
                    continue

                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = g_scores[neighbor] + self.manhattan_distance(neighbor, end)

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
