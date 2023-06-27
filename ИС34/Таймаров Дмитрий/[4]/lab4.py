import turtle
from avatar import Avatar
from mob import Mob

window = turtle.Screen()

avatar = Avatar(target=(-200, 250))
avatar.init_way()
avatar.color("green")
avatar.pensize(2)
avatar.pendown()
mob = Mob(target=avatar)
mob.color("red")
mob.pensize(2)
mob.pendown()

while not avatar.finish:
    avatar.make_step()
    mob.Greedy()

window.exitonclick()
