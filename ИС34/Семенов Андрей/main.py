import turtle
from avatar import Avatar
from mob import Mob

window = turtle.Screen()

avatar = Avatar(target=(200, 300))
avatar.init_path()
avatar.pensize(3)
avatar.color("blue")

mob = Mob(target_turtle=avatar)
mob.pensize(3)
mob.color("green")

while not avatar.is_finish:
    avatar.make_step()
    mob.make_step()

window.exitonclick()