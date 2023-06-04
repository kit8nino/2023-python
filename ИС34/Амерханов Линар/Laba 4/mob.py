
import turtle


turtle.register_shape("MrCrabs.gif")
class Mob(turtle.Turtle):

    __secret = 'looks like a girlfriend'
    coord_for_normal_people = [0,0]

    def __init__(self, name, x=-450, y=360):
        super().__init__()
        self.hideturtle()
        self.shape("MrCrabs.gif")
        self.setheading(270)
        self.shapesize(3, 3)
        self.name = name
        #self.shape("square")
        #self.color("green")
        self.speed(2)
        self.penup()
        self.goto(x, y)
        self.setheading(270)

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



