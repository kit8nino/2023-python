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
        heap = []
        heapq.heappush(heap, (0, start, []))
        visited = set()

        while heap:
            _, current, path = heapq.heappop(heap)

            if current == target:
                return path

            if current in visited:
                continue

            visited.add(current)

            neighbors = self.get_neighbors(current)

            for neighbor in neighbors:
                if neighbor in visited:
                    continue

                cost = self.get_cost(current, neighbor)
                new_path = path + [neighbor]
                heuristic_cost = self.heuristic(neighbor)
                total_cost = cost + heuristic_cost

                heapq.heappush(heap, (total_cost, neighbor, new_path))

        return None

    def get_neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return neighbors

    def get_cost(self, current, neighbor):
        return 1

    def init_path(self):
        self.path = self.a_star((0, 0), self.target)[::self._speed]

    def make(self):
        if self.current_step == len(self.path):
            self.is_finish = True
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1
        return self.heading()