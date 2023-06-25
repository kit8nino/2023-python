import turtle

class Mob(turtle.Turtle):
    def __init__(self, target: turtle.Turtle, speed=15):
        super().__init__()
        self.target = target
        self.speed = speed
        self.current_step = 2
        self.way = None

    def Greedy(self):
        if self.position() == self.target.position():
            return
        location = tuple(map(int, self.position()))
        location_avatar = tuple(map(int, self.target.position()))
        queue = [(location, [])]
        visited = set()
        while queue:
            current, way = queue.pop(0)
            if current == location_avatar:
                self.way = way[::self._speed]
                break
            if current in visited:
                continue
            visited.add(current)
            x, y = current
            cells = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for cell in cells:
                queue.append((cell, way + [cell]))
        if not self.way:
            return
        if self.current_step >= len(self.way):
            return
        self.goto(self.way[self.current_step])
        self.current_step += 1
        return self.heading()