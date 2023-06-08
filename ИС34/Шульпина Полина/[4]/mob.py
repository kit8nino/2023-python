import turtle
turtle.register_shape("calcifer.gif")
class Mob(turtle.Turtle):
    def __init__(self, target_turtle, speed =10 ):
        super().__init__()
        self.shape("calcifer.gif")
        self.target_turtle = target_turtle
        self._speed = speed
        self.current_step = self._speed
        self.path = None
        screen = turtle.Screen()
        screen.bgcolor('black')
        screen.title('realization')


    def greedy(self):
        avatar_position = tuple(map(int, self.target_turtle.position()))
        queue = [(tuple(map(int, self.position())), [])]
        visited = set()
        dxs = [0, 0, 1, -1]
        dys = [1, -1, 0, 0]
        found_path = False


        while queue and not found_path:
            current, path = queue.pop(0)
            if current == avatar_position:
                self.path = path[::self._speed]
                found_path = True

            if current not in visited:
                visited.add(current)
                x, y = current
                neighbors = [(x + dx, y + dy) for dx, dy in zip(dxs, dys)]
                for neighbor in neighbors:
                    queue.append((neighbor, path + [neighbor]))

        if not found_path:
            return

        if self.current_step >= len(self.path):
            return

        self.goto(self.path[self.current_step])
        self.current_step += 1

        return self.heading()