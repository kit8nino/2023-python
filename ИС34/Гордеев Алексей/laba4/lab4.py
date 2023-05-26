import turtle
from Avatar import Avatar
from Mob import Mob

wn = turtle.Screen()

avatar = Avatar(speed=10, target=(100, 200))
avatar.init_path()
avatar.pensize(3)
avatar.color("black")

mob = Mob(speed=1, target_turtle=avatar)
mob.pensize(3)
mob.color("green")

while not avatar.is_finish:
    avatar.make_step()
    mob.make_step()

wn.exitonclick()