import turtle
import heapq
import math
from Avatar import Avatar

class Mob(turtle.Turtle):
    def __init__(self, target: Avatar, speed: int = 15):
        super().__init__()
        self.speed(speed)
        self.target = target
        self.current_step = 0
        self.path = None

    def calculate_heuristic(self, coord):
        target_x, target_y = self.target.position()
        x, y = coord
        distance = math.sqrt((target_x - x) ** 2 + (target_y - y) ** 2)
        return distance

    def a_star(self, start, target):
        pq = [(0, start, [])]
        visited = set()

        while pq:
            f_cost, current, path = heapq.heappop(pq)

            if current == target:
                return path

            if current in visited:
                continue

            visited.add(current)

            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                g_cost = len(path) + 1
                h_cost = self.calculate_heuristic(neighbor)
                f_cost = g_cost + h_cost

                heapq.heappush(pq, (f_cost, neighbor, path + [neighbor]))

        return None

    def get_neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return neighbors

    def initialize_path(self):
        position = tuple(map(int, self.position()))
        avatar_position = tuple(map(int, self.target.position()))
        self.path = self.a_star(position, avatar_position)

    def take_step(self):
        if self.position() == self.target.position():
            return

        position = tuple(map(int, self.position()))
        avatar_position = tuple(map(int, self.target.position()))
        self.path = self.a_star(position, avatar_position)

        if self.path is None:
            return

        if self.current_step >= len(self.path):
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1
