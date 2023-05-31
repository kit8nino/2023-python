import turtle
from Avatar import Avatar
from Mob import Mob

wn = turtle.Screen()

avatar = Avatar(target=(150, 320), speed=50)
avatar.initialize_path()
avatar.pensize(5)
avatar.color("red")

mob = Mob(target=avatar, speed=0.2)
mob.initialize_path()
mob.pensize(5)
mob.color("green")

while not avatar.is_finish:
    avatar.take_step()
    mob.take_step()

wn.exitonclick()