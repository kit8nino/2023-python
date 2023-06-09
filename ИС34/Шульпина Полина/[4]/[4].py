import turtle
import time
from mob import Mob
from avatar import Avatar
target =(100,100)
av = Avatar(target)
av.init_path()
av.color("white")
mob = Mob(target_turtle = av, speed =1)
mob.color("red")

while not av.is_finish:
    av.step()
    mob.greedy()
time.sleep(1)


