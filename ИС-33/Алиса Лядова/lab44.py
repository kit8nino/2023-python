import turtle
from avatar import Avatar
from mob import Mob

window = turtle.Screen()

avatar = Avatar(target=(150, 200))
avatar.init_path()
avatar.pensize(1)
avatar.color("blue")

mob = Mob(target_turtle=avatar)
mob.pensize(1)
mob.color("black")

while not avatar.is_finish:
    avatar.make_step()
    mob.make_step()

window.exitonclick()
