import turtle
import heapq


class Avatar(turtle.Turtle):

    def __init__(self, target: tuple, speed = 10):
        super().__init__()
        self.speed(speed)
        self.is_finish = False
        self.target = target
        self.path = None
        self.current_step = 0

    def heuristic(self, coord):
        target_x, target_y = self.target
        x, y = coord
        distance = ((target_x - x) ** 2 + (target_y - y) ** 2) ** 0.5
        return distance

    def a_star(self, start, target):
        queue = [(0, start, [])]
        used = set()

        while queue:
            f_cost, current, path = heapq.heappop(queue)
            if current == target:
                return path
            if current in used:
                continue
            used.add(current)
            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                g_cost = len(path) + 1
                h_cost = self.heuristic(neighbor)
                f_cost = (g_cost**2 + h_cost**2)
                heapq.heappush(queue, (f_cost, neighbor, path + [neighbor]))
        return None

    def get_neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 2, y), (x + 3, y), (x, y - 2), (x, y + 3)]
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