import turtle
from collections import deque


class Achilles(turtle.Turtle):
    _algorithm = 'breadth_first_search'

    def __init__(self, target_turtle: turtle.Turtle, speed: int = 15):
        super().__init__()
        self.target_turtle = target_turtle
        self._speed = speed
        self.speed(self._speed)
        self.current_step = 0
        self.path = None

    def bfs(self, start, target):
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

        return None

    def get_neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return neighbors

    def make_step(self):
        if self.position() == self.target_turtle.position():
            return

        position = tuple(map(int, self.position()))
        avatar_position = tuple(map(int, self.target_turtle.position()))

        self.path = self.bfs(position, avatar_position)[::self._speed]

        if self.current_step > len(self.path):
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1

        return self.heading()
