import turtle
from avatar import Avatar
from mob import Mob

wn = turtle.Screen()

avatar = Avatar(speed=10, target=(-100, 200))
avatar.init_path()
avatar.pensize(3)
avatar.color("green")

mob = Mob(speed=1, target_turtle=avatar)
mob.pensize(3)
mob.color("pink")

while not avatar.is_finish:
    avatar.make_step()
    mob.make_step()

wn.exitonclick()

