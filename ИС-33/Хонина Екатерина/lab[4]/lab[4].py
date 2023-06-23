import turtle
from _avatar import Avatar
from _mob import Mob

win = turtle.Screen()

avatar = Avatar(speed=10, target=(200, 200))
avatar.init_path()
avatar.pensize(2)
avatar.color("black")

mob = Mob(speed=1, target_turtle=avatar)
mob.pensize(2)
mob.color("green")

while not avatar.is_finish:
    avatar.make_step()
    mob.move().__next__()

win.exitonclick()
