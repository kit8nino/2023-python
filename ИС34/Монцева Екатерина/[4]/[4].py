import turtle
from Avatar import Avatar
from Mob import Mob

wind = turtle.Screen()
avat = Avatar(speed=10, target=(250, 350))
avat.init_path()
avat.pensize(5)
avat.color("red")
mob = Mob(speed=1, target_turtle=avat)
mob.pensize(3)
mob.color("green")

while not avat.finish:
    avat.do_step()
    mob.stingy()
wind.exitonclick()
