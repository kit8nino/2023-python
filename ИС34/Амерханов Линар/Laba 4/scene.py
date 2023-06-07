import turtle
turtle.register_shape("Lable.gif")
class Scene(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("Lable.gif")
        self.setheading(270)
        self.shapesize(3, 3)
        self.penup()



class MazeDrawer:
    def __init__(self, filename):
        self.filename = filename
        self.maze_data = []

    def read_maze(self):
        with open(self.filename, "r") as file:
            self.maze_data = file.readlines()

    def draw_maze(self):
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        turtle.delay(0)

        x = -480 - 60
        y = 390 + 60

        for row in self.maze_data:
            for cell in row:
                if cell == "#":
                    turtle.goto(x, y)
                    turtle.pendown()
                    turtle.begin_fill()
                    for _ in range(4):
                        turtle.forward(60)
                        turtle.right(90)
                    turtle.end_fill()
                    turtle.penup()
                x += 60
            y -= 60
            x = -480 - 60

    def run(self):
        self.read_maze()
        self.draw_maze()




