import turtle
from mob import Mob
from avatar import Avatar

terminal = turtle.Screen()
avatar = Avatar(speed=10, target=(110, 120))
avatar.init_path()
avatar.pensize(2)
avatar.color("red")

mob = Mob(speed=1, target=(110, 120))
mob.init_path()
mob.pensize(2)
mob.color("blue")

while not avatar.is_finish or not mob.is_finish:
    if not avatar.is_finish:
        avatar.make_step()
    if not mob.is_finish:
        mob.make_step()

terminal.exitonclick()
