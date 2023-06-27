import turtle
import heapq

class Avatar(turtle.Turtle):

    def __init__(self, target: tuple, speed=10):
        super().__init__()
        self.speed(speed)
        self.finish = False
        self.target = target
        self.way = None
        self.current_step = 1

    def a_star(self, start, target):
        queue = [(0, start, [])]
        previous = set()
        while queue:
            F_cost, current, way = heapq.heappop(queue)
            if current == target:
                return way
            if current in previous:
                continue
            previous.add(current)
            x,y = current
            cells = [(x - 2, y), (x + 3, y), (x, y - 2), (x, y + 3)]
            for cell in cells:
                G_cost = len(way) + 1
                H_cost = self.heuristic(cell)
                F_cost = (H_cost**2 + G_cost**2)
                heapq.heappush(queue, (F_cost, cell, way + [cell]))
        return None

    def heuristic(self, coord):
        target_x, target_y = self.target
        x,y = coord
        distance = ((target_x - x) ** 2 + (target_y - y) ** 2) ** 0.5
        return distance

    def init_way(self):
        self.way = self.a_star((0, 0), self.target)[::self._speed]

    def make_step(self):
        if self.current_step == len(self.way):
            self.finish = True
            return
        self.goto(self.way[self.current_step][0], self.way[self.current_step][1])
        self.current_step += 1
        return self.heading()