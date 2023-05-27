import turtle
from math import sqrt
class Mob(turtle.Turtle):
    def __init__(self, speed=5, avatar=None):
        super().__init__()
        self.shape("turtle")
        self.speed = speed
        self.avatar = avatar
        self.penup()
        self.color("red")


    def exit(self):
        if self.avatar.position() == self.position():
            return False
        else:
            return True

    def set_coord(self):
        mob_x, mob_y = map(int, input("Введите координаты моба через пробел: ").split())
        self.goto(mob_x, mob_y)
        self.pendown()

    def set_speed(self):
        mob_speed = int(input("Введите скорость моба: "))
        self.speed = mob_speed

    def run(self):
        for new_mob_x, new_mob_y in self.get_next_coordinates():
            self.goto(new_mob_x, new_mob_y)
            break
    def get_distance(self, neighbor, goal):
        if self.avatar:
            x1, y1 = neighbor
            x2, y2 = goal
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        else:
            return None

    def get_next_coordinates(self):
        while self.avatar and self.distance(self.avatar) > 0:
            avatar_pos = self.avatar.position()

            distances = {}
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x = self.xcor() + dx * self.speed
                new_y = self.ycor() + dy * self.speed
                distances[(new_x, new_y)] = self.get_distance((new_x, new_y), avatar_pos)

            min_dist = float('inf')
            next_pos = None
            for pos, dist in distances.items():
                if dist < min_dist:
                    min_dist = dist
                    if dist <= self.speed:
                        next_pos = self.avatar.position()
                        break
                    else:
                        next_pos = pos

            if next_pos:
                yield next_pos

        yield self.xcor(), self.ycor()