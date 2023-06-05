import turtle

from _turtle import Turtle
from achilles import Achilles

wn = turtle.Screen()

_turtle = Turtle(speed=10, target=(300, 200))
_turtle.init_path()
_turtle.pensize(2)
_turtle.color("blue")

achilles = Achilles(speed=1, target_turtle=_turtle)
achilles.pensize(2)
achilles.color("red")

while not _turtle.is_finish:
    _turtle.make_step()
    achilles.make_step()


wn.exitonclick()
