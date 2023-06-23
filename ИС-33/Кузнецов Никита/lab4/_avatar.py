import turtle
from math import sqrt
from queue import PriorityQueue

class Avatar(turtle.Turtle):

    def __init__(self, target: tuple, speed: int = 10):
        super().__init__()
        self._speed = speed
        self.speed(speed)
        self.is_finish = False
        self.target = target
        self.path = None
        self.current_step = 0
        self.parents = {}

    def get_heuristic(self, current_coordinates):
        target_x, target_y = self.target
        x = current_coordinates[0]
        y = current_coordinates[1]
        return sqrt((target_x - x) ** 2 + (target_y - y) ** 2)

    def get_valid_neighbors(self, coordinates):
        neighbors = [(coordinates[0] + 1, coordinates[1]), (coordinates[0], coordinates[1] - 1),
                     (coordinates[0], coordinates[1] + 1),
                     (coordinates[0] - 1, coordinates[1])]
        return neighbors

    def get_path_1(self, node, start, path):
        while node != start:
            path.append(self.parents[node])
            node = self.parents[node]

    def search_in_A(self, start, end):
        queue = PriorityQueue()
        queue.put((0, start))
        searched = set()
        while not queue.empty():
            priority, coordinates = queue.get()
            if coordinates == end:
                return
            if coordinates in searched:
                continue
            searched.add(coordinates)
            neighbors = self.get_valid_neighbors(coordinates)
            for n in neighbors:
                if n not in searched:
                    self.parents[n] = coordinates
                    priority = self.get_heuristic(n)
                    queue.put((priority, n))
        return None

    def init_path(self):
        self.search_in_A((0, 0), self.target)
        path2 = []
        self.get_path_1(self.target, (0, 0), path2)
        self.path = path2[::-self._speed]

    def move(self):
        if self.current_step == len(self.path):
            self.is_finish = True
            yield
        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1
        yield self.heading()
