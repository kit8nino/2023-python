import turtle
import heapq
turtle.register_shape("frog.gif")
class Mob(turtle.Turtle):

    def __init__(self, target_turtle: turtle.Turtle, speed):
        super().__init__()
        self.shape("frog.gif")
        self.target_turtle = target_turtle
        self._ = speed
        self.speed(self._speed)
        self.now_step = 0
        self.path = []

    def stingy(self):
        if self.position() == self.target_turtle.position():
            return

        place = tuple(map(int, self.position()))
        avatar_place = tuple(map(int, self.target_turtle.position()))

        queue = [(place, [])]
        Visit = set()

        while queue:
            coord, path = queue.pop(0)
            if coord == avatar_place:
                self.path = path[::self._speed]
                break

            if coord in Visit:
                continue

            Visit.add(coord)

            x, y = coord
            dx, dy = [-5, 3, 0, 0], [0, 0, -1, 1]
            neighbors = [(x + dx[i], y + dy[i]) for i in range(len(dx))]
            for neighbor in neighbors:
                queue.append((neighbor, path + [neighbor]))

        if not self.path:
            return

        if self.now_step >= len(self.path):
            return

        self.goto(self.path[self.now_step])
        self.now_step += 1

        return self.heading()







