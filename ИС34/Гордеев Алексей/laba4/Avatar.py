import turtle
import math
import heapq

class Avatar(turtle.Turtle):
    def __init__(self, target: tuple, speed: int = 10):
        super().__init__()
        self._speed = speed
        self.speed(speed)
        self.is_finish = False
        self.target = target
        self.path = None
        self.current_step = 0

    def heuristic(self, coord):
        target_x, target_y = self.target
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
                h_cost = self.heuristic(neighbor)
                f_cost = g_cost + h_cost

                heapq.heappush(pq, (f_cost, neighbor, path + [neighbor]))

        return None

    def get_neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return neighbors

    def init_path(self):
        self.path = self.a_star((0, 0), self.target)[::self._speed]

    def make_step(self):
        if self.current_step == len(self.path):
            self.is_finish = True
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1

        return self.heading()
