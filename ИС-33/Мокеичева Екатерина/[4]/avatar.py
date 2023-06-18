import turtle
class Avatar(turtle.Turtle):
    def __init__(self, speed=10, target=None):
        super().__init__()
        self.shape("circle")
        self.speed = speed
        self.target = target
        self.penup()
        self.parent = {}
        self.color("blue")

    def exit(self):
        if self.target == self.position():
            return False
        else:
            return True

    def go(self,coords):
        self.goto(coords[0], coords[1])

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

    def heuristic(self, point):
        x1, y1 = self.target
        x2, y2 = point
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

    def neighbors(self):
        return [(self.xcor(), self.ycor() + self.speed), (self.xcor(), self.ycor() - self.speed), (self.xcor() + self.speed, self.ycor()), (self.xcor() - self.speed, self.ycor())]

    def run(self):
        min_dis = min([self.heuristic(neighbor) for neighbor in self.neighbors()])
        for point in self.neighbors():
            if self.heuristic(self.position()) <= self.speed:
                self.go(self.target)
                break
            if self.heuristic(point) == min_dis:
                self.go(point)
                break
                
