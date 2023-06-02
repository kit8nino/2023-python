import turtle
from Avatar import Avatar
from Mob import Mob

window= turtle.Screen()

a = Avatar(target=(-200, -90))
a.init_path()
a.color("black")

m = Mob(speed=1, target_turtle=a)
m.color("red")
while not a.is_finish:
    a.make()
    m.greedy()
window.exitonclick()