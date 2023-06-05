import turtle
from ava import Avatar
from mobik import Mob


ava = Avatar(target=(-20, -150))
ava.init_path()

mob = Mob(target_turtle = ava)

while not ava.is_finish:
    ava.make_step()
    mob.make_step()
