import turtle

class Mob(turtle.Turtle):
    def __init__(self, target_turtle: turtle.Turtle, speed: int = 15):
        super().__init__()
        self.target_turtle = target_turtle
        self._ = speed
        self.speed(self._speed)
        self.current_step = 0
        self.path = None

    def greedy(self):
        if self.position() == self.target_turtle.position():
            return

        position = tuple(map(int, self.position()))
        avatar_position = tuple(map(int, self.target_turtle.position()))

        queue = [(position, [])]
        visited = set()

        while queue:
            current, path = queue.pop(0)
            if current == avatar_position:
                self.path = path[::self._speed]
                break

            if current in visited:
                continue

            visited.add(current)

            x, y = current
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for neighbor in neighbors:
                queue.append((neighbor, path + [neighbor]))

        if not self.path:
            return

        if self.current_step >= len(self.path):
            return

        self.goto(self.path[self.current_step])
        self.current_step += 1

        return self.heading()