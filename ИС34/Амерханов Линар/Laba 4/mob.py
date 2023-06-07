import turtle

turtle.register_shape("MrCrabs.gif")


class Mob(turtle.Turtle):
    def __init__(self, name, maze, avatar, x=-450, y=360):
        super().__init__()
        self.hideturtle()
        self.shape("MrCrabs.gif")
        self.setheading(270)
        self.shapesize(3, 3)
        self._start_point_turt_y = y
        self._start_point_turt_x = x
        self._x_log = 1
        self._y_log = 1
        self.name = name
        self.speed(2)
        self.penup()
        self.goto(x, y)
        self.setheading(270)
        self.maze = maze
        self.path = None
        self.avatar = None

    def set_avatar(self, avatar):
        self.avatar = avatar

    def move(self):
        if self.path:
            next_cell = self.path.pop(0)
            self._y_log = next_cell[1]
            self._x_log = next_cell[0]
            # Гениальный мув
            self.goto(self._start_point_turt_x + self._y_log * 60 - 60, self._start_point_turt_y - self._x_log * 60 + 60)

    def get_avatar_coord(self):
        return self.avatar.get_coord_log()

    def get_self_cood(self):
        return (self._x_log, self._y_log)

    def calculate_path(self):
        start = self.get_self_cood()
        end = self.get_avatar_coord()

        open_list = [start]
        closed_list = []
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}

        while open_list:
            current = min(open_list, key=lambda x: f_score[x])

            if current == end:
                path = [end]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                self.path = path[1:]
                return

            open_list.remove(current)
            closed_list.append(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in closed_list:
                    continue

                tentative_g_score = g_score[current] + 1

                if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, end)
                    if neighbor not in open_list:
                        open_list.append(neighbor)

    def heuristic(self, current, end):
        return abs(current[0] - end[0]) + abs(current[1] - end[1])

    def get_neighbors(self, coords):
        x, y = coords
        neighbors = []

        if x - 1 >= 0 and self.maze[x - 1][y] == " ":
            neighbors.append((x - 1, y))

        if x + 1 < len(self.maze) and self.maze[x + 1][y] == " ":
            neighbors.append((x + 1, y))

        if y - 1 >= 0 and self.maze[x][y - 1] == " ":
            neighbors.append((x, y - 1))

        if y + 1 < len(self.maze[0]) and self.maze[x][y + 1] == " ":
            neighbors.append((x, y + 1))
        return neighbors

    def check_movement(self):
        self.calculate_path()
        self.move()

    def __str__(self):
        return f"Mob: {self.name} | Position: ({self.xcor()}, {self.ycor()})"
