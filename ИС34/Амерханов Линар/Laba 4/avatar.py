import turtle


turtle.register_shape("Plank.gif")
class Avatar(turtle.Turtle):
    __secret = 'looks like a girlfriend'
    def __init__(self, name, x=-450, y=360):
        super().__init__()
        self.__x_log = 1
        self.__y_log = 1
        self.__make_step = 0
        self.mazeFNP = []
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
        self.caught = False

    def set_maze(self, maze_data):
        self.maze_FNP = maze_data

    def move(self, direction):
        if direction == "up":
            if self.__x_log > 0 and self.maze_FNP[self.__x_log - 1][self.__y_log] != "#":
                self.__x_log -= 1
                self.setheading(90)
                self.forward(60)
        elif direction == "down":
            if self.__x_log < len(self.maze_FNP) - 1 and self.maze_FNP[self.__x_log + 1][self.__y_log] != "#":
                self.__x_log += 1
                self.setheading(270)
                self.forward(60)
        elif direction == "left":
            if self.__y_log > 0 and self.maze_FNP[self.__x_log][self.__y_log - 1] != "#":
                self.__y_log -= 1
                self.setheading(180)
                self.forward(60)
        elif direction == "right":
            if self.__y_log < len(self.maze_FNP[0]) - 1 and self.maze_FNP[self.__x_log][self.__y_log + 1] != "#":
                self.__y_log += 1
                self.setheading(0)
                self.forward(60)

        self.__make_step += 1


    def get_coord(self):
        return (self.xcor(), self.ycor())
    def get_coord_log(self):
        return (self.__x_log,self.__y_log)
    def get_make_step(self):
        return self.__make_step
    def __str__(self):
        return f"Mob: {self.name} | Position: ({self.xcor()}, {self.ycor()}"

