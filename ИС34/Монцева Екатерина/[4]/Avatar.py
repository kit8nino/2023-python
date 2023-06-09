from queue import PriorityQueue
import turtle
import math

turtle.register_shape("muh.gif")
class Avatar(turtle.Turtle):
    def __init__(self, target: tuple, speed):
        super().__init__()
        self.shape("muh.gif")
        self._speed = speed
        self.speed(speed)
        self.finish = False
        self.target = target
        self.path = []
        self.now_step = 0

    def heuristic(self, coord):
        end_x, end_y = self.target
        x, y = coord
        distances = math.sqrt((end_x - x) ** 2 + (end_y - y) ** 2)
        return distances

    def astar(self, start, target):
        list = PriorityQueue()
        path = []
        visited = set()
        list.put((0, start, path))

        while not list.empty():
            f_cost, current_pos, path = list.get()

            if current_pos == target:
                return path

            if current_pos in visited:
                continue

            visited.add(current_pos)

            for neighbor in self.neighbors(current_pos):
                if neighbor in visited:
                    continue

                g_cost = self.get_pay(current_pos, neighbor)
                new_path = path + [neighbor]
                h_cost = self.heuristic(neighbor)
                f_cost = g_cost + h_cost
                list.put((f_cost, neighbor, new_path))

        return None

    def init_path(self):
        self.path = self.astar((0, 0), self.target)[::self._speed]

    def neighbors(self, GPS):
        (x, y) = GPS
        res_point = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)]
        return res_point

    def get_pay (self, stream, neighbor):
        return 1

    def do_step(self):
        if self.now_step == len(self.path):
            self.finish = True
            return
        self.goto(self.path[self.now_step][0], self.path[self.now_step][1])
        self.now_step += 1

        return self.heading()