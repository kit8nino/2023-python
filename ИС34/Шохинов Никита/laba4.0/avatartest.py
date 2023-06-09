import turtle
from queue import PriorityQueue
import math

class Avatar(turtle.Turtle):
    name = 'Noname'
    max_x, max_y = 101, 101
    _step_count = 0

    def __init__(self, name='Noname', x=0, y=0, target=(80, 40), speed=5):
        super().__init__()
        self.x, self.y = x, y
        self.name = name
        self.target = target
        self.speed = speed

    def set_coord(self, x, y):
        if x < self.max_x:
            self.x = x
        if y < self.max_y:
            self.y = y

    def step(self, direction='up'):
        if direction == 'up':
            self.y += self.speed
        if direction == 'down':
            self.y -= self.speed
        if direction == 'left':
            self.x -= self.speed
        if direction == 'right':
            self.x += self.speed
        self.move()
        return (self.x, self.y)

    def move(self):
        self._step_count += 1
        self.goto(self.x, self.y)

    def A_star(self):

        start = (self.x, self.y)
        end = self.target
        next_step = None

        def heuristic(a, b):
            return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

        def in_bounds(point):
            x, y = point
            return 0 <= x < self.max_x and 0 <= y < self.max_y

        def neighbors(point):
            x, y = point
            results = [(x+5, y), (x, y-5), (x-5, y), (x, y+5)]
            results = filter(in_bounds, results)
            return results

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                path = []
                while current != start:
                    path.append(current)
                    current = came_from[current]
                    if path:
                        next_step = path[-1]
                if next_step is not None:
                    if next_step[0] > start[0]:
                        return "right"
                    elif next_step[0] < start[0]:
                        return "left"
                    elif next_step[1] < start[1]:
                        return "down"
                    elif next_step[1] > start[1]:
                        return "up"
                    else:
                        return None
                else:
                    return None

            for next in neighbors(current):
                new_cost = cost_so_far[current] + 5
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(end, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        return None
