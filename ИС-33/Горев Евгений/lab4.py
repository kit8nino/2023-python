import turtle
from avatar import Avatar
from mob import Mob

window = turtle.Screen()

a = Avatar(target=(150, -250))
a.init_path()
a.color("blue")

m = Mob(speed=1, target_turtle=a)
m.color("red")
while not a.is_finish:
    a.make()
    m.greedy()
window.exitonclick()