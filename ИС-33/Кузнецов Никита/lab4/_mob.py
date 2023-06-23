import turtle
from collections import deque

class Mob(turtle.Turtle):

    def __init__(self, target_turtle: turtle.Turtle, speed: int = 15):
        super().__init__()
        self.target_turtle = target_turtle
        self._speed = speed
        self.speed(self._speed)
        self.current_step = 0
        self.path = None
        self.parents = {}

    def search(self, start_coordinates, target_coordinates):
        search_deque = deque()
        search_deque.append(start_coordinates)
        searched = set()
        while search_deque:
            coordinates = search_deque.popleft()
            if coordinates == target_coordinates:
                return
            if coordinates in searched:
                continue
            searched.add(coordinates)
            neighbors = self.get_neighbors(coordinates)
            for n in neighbors:
                if n not in searched:
                    self.parents[n] = coordinates  # запись родителя
                    search_deque.append(n)
        return None

    def get_neighbors(self, coordinates):
        x, y = coordinates
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return neighbors

    def get_path_1(self, node, start, path):
        while node != start:
            if node == (0, 0):
                path.append((0, 0))
            else:
                path.append(self.parents[node])
                node = self.parents[node]

    def move(self):
        if self.position() == self.target_turtle.position():
            yield
        position = tuple(map(int, self.position()))
        avatar_position = tuple(map(int, self.target_turtle.position()))
        self.search(position, avatar_position)
        path2 = []
        self.get_path_1(avatar_position, position, path2)
        self.path = path2[::-self._speed]
        if self.current_step >= len(self.path):
            yield
        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1
        yield self.heading()
