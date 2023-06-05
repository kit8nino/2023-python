import turtle
from math import sqrt
class Avatar(turtle.Turtle):
    def __init__(self, speed=10, target=None):
        super().__init__()
        self.shape("triangle")
        self.speed = speed
        self.target = target
        self.penup()
        self.parent = {}
        self.color("blue")
        self.path = []

    def exit(self):
        if self.target == self.position():
            return False
        else:
            return True

    def run(self):
        if self.path == []:
            self.set_path()
            self.path.pop(0)
            for coords in self.path:
                self.goto(coords[0], coords[1])
                break
        else:
            self.path.pop(0)
            for coords in self.path:
                self.goto(coords[0], coords[1])
                break

    def set_coord(self):
        avatar_x, avatar_y = map(int, input("Введите координаты аватара через пробел: ").split())
        self.goto(avatar_x, avatar_y)
        self.pendown()

    def set_target(self):
        target_x, target_y = map(int, input("Введите координаты ключевой точки через пробел: ").split())
        self.target = (target_x,target_y)

    def set_speed(self):
        avatar_speed = int(input("Введите скорость аватара: "))
        self.speed = avatar_speed

    def set_path(self):
        self.path = self.get_next_coordinates_astar()
    def get_distance(self, neighbor, goal):
        if self.target:
            x1, y1 = neighbor
            x2, y2 = goal
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        else:
            return None

    def get_distance_to_target(self):
        if self.target:
            x1, y1 = self.position()
            x2, y2 = self.target
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        else:
            return None

    def get_next_coordinates_astar(self):
        while self.get_distance_to_target() > 0:
            start = (self.xcor(), self.ycor())
            goal = self.target

            open_list = [start]
            closed_list = []

            g_score = {start: 0}
            h_score = {start: self.get_distance_to_target()}

            while open_list:
                current_node = min(open_list, key=lambda x: g_score[x] + h_score[x])

                if current_node == goal:
                    path = [current_node]
                    while current_node in self.parent:
                        current_node = self.parent[current_node]
                        path.append(current_node)
                    path.reverse()
                    return path

                open_list.remove(current_node)
                closed_list.append(current_node)

                neighbors = []
                for dx, dy in [(0, 1 * self.speed), (0, -1 * self.speed), (1 * self.speed, 0), (-1 * self.speed, 0)]:
                    if sqrt((closed_list[-1][0] - self.target[0]) ** 2 + (closed_list[-1][1] - self.target[1]) ** 2) <= self.speed:
                        neighbor = (self.target[0], self.target[1])
                    else:
                        neighbor = (current_node[0] + dx, current_node[1] + dy)
                    neighbors.append(neighbor)

                for neighbor in neighbors:
                    if neighbor in closed_list:
                        continue

                    tentative_g_score = g_score[current_node] + 1

                    if neighbor not in open_list:
                        open_list.append(neighbor)
                        h_score[neighbor] = self.get_distance(neighbor, goal)
                        g_score[neighbor] = tentative_g_score
                        self.parent[neighbor] = current_node

                    elif tentative_g_score < g_score[neighbor]:
                        g_score[neighbor] = tentative_g_score
                        self.parent[neighbor] = current_node

            return self.xcor(), self.ycor()
