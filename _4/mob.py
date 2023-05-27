import turtle


class Mob(turtle.Turtle):
    _algorythm = 'a_star'

    def __init__(self, coord=(0, 0), name='Frog', img='frog.gif',
                 speed=15):
        self.register_shape('frog.gif')
        self.shape('frog.gif')
        self.up()
        self.goto(coord)
        self.speed = speed
        self.name = name

    def step(self):
        pass
