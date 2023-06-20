import turtle
import math
from collections import deque


class Avatar(turtle.Turtle):
    name = 'Noname'
    max_x, max_y = 100, 100
    _step_count = 0

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
        queue = deque([(start, [])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == target:
                return path

            if current in visited:
                continue

            visited.add(current)

            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                queue.append((neighbor, path + [neighbor]))

            # Сортировка очереди по эвристической стоимости
            queue = deque(sorted(queue, key=lambda x: self.heuristic(x[0])))

        return None

    def get_neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return neighbors

    def init_path(self):
        self.path = self.a_star((int(self.xcor()), int(self.ycor())), self.target)

    def make_step(self):
        if self.current_step == len(self.path):
            self.is_finish = True
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += self._speed

        return self.heading()
