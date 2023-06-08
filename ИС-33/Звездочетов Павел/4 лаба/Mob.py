# -*- coding: utf-8 -*-

from turtle import Turtle


class Mob(Turtle):
    def __init__(self, coords, speed, color):
        super().__init__()
        self.penup()
        self.__pos = coords
        self.goto(coords[1] * 2 - 480, -coords[0] * 2 + 480)
        self.speed(speed)
        self.color(color)
        self.shape('square')
        self.color(color)
        self.shapesize(2 / 20)

    def getPos(self):
        return self.__pos

    def make_move(self, maze, target):
        move_y, move_x = self.greedy_first_search(maze, self.__pos, target)[1]
        self.goto(move_x * 2 - 480, -move_y * 2 + 480)
        self.__pos = move_y, move_x

    def greedy_first_search(self, maze, start, goal):
        frontier = [start]
        visited = []
        currentList = [start]
        while len(frontier) != 0:
            current = min(frontier, key=lambda n: self.heuristic(n, goal))
            currentList.append(current)
            if current == goal:
                return self.get_path(currentList)
            frontier.remove(current)
            visited.append(current)
            neighbors = self.get_neighbors(maze, current)
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in frontier:
                    frontier.append(neighbor)

    def heuristic(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    def get_neighbors(self, maze, pos):
        row, col = pos
        candidates = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]
        result = []
        for r, c in candidates:
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == "0":
                result.append((r, c))

        return result

    def get_path(self, current):
        path = [current[-1]]
        current = list(reversed(current))
        i = len(current)
        for j in range(i - 1):
            if ((current[0][0] - path[-1][0]) ** 2 + (current[0][1] - path[-1][1]) ** 2) ** (1 / 2) == 1:
                path.append(current[0])
                del current[0]
            else:
                del current[0]
        return list(reversed(path))
