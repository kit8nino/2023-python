import turtle
turtle.register_shape("Lable.gif")
turtle.register_shape("GmOv.gif")
turtle.register_shape("Win.gif")
turtle.register_shape("ChumBucket.gif")
class Scene(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("Lable.gif")
        self.setheading(270)
        self.shapesize(3, 3)
        self.penup()

class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("GmOv.gif")
        self.setheading(270)
        self.shapesize(3, 3)
        self.penup()
class Congratulation(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("Win.gif")
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

    def find_last_coordinate(self):
        last_coordinate = None
        for i in range(len(self.maze_data) - 1, -1, -1):
            for j in range(len(self.maze_data[i]) - 1, -1, -1):
                if self.maze_data[i][j] == " ":
                    last_coordinate = (i, j)
                    return last_coordinate
        return last_coordinate

    def win(self):
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        turtle.delay(0)
        turtle.shape("ChumBucket.gif")

        win_point = self.find_last_coordinate()
        x = -480 + 60 * win_point[1] - 60 + 30
        y = 390 - 60 * win_point[0] + 60 - 30

        turtle.goto(x, y)
        turtle.showturtle()



    def draw_maze(self):
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        turtle.delay(0)
        turtle.color("#e4ac24")

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
        self.win()




