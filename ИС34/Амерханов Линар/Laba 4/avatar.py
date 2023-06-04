import turtle


turtle.register_shape("Plank.gif")
class Avatar(turtle.Turtle):
    __secret = 'looks like a girlfriend'

    def __init__(self, name, x=-450, y=360):
        super().__init__()
        self.hideturtle()
        self.shape("Plank.gif")
        self.setheading(270)
        self.shapesize(3, 3)
        self.name = name
        self.speed(2)
        self.penup()
        self.goto(x, y)
        self.setheading(270)
        self.speed(1)


    def move(self, direction):
        if direction == "up":

            self.setheading(90)
        elif direction == "down":
            self.setheading(270)
        elif direction == "left":
            self.setheading(180)
        elif direction == "right":
            self.setheading(0)

        self.forward(60)

    def __str__(self):
        return f"Avatar: {self.name} | Position: ({self.x}, {self.y})"

    def get_coord(self):
        return (self.xcor(), self.ycor())

