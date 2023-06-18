import turtle
from AvataR import Avatar
from MoB import Mob

wn = turtle.Screen()

avatar = Avatar(speed=10, target=(250, 350))
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