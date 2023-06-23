from avatar import Avatar
from mob import Mob
import turtle

window= turtle.Screen()

avatar = Avatar()
avatar.set_coord()
avatar.set_target()
avatar.set_speed()

mob = Mob(avatar=avatar)
mob.set_coord()
mob.set_speed()

while avatar.exit() and mob.exit():
    avatar.run()
    mob.run()
print("Выполнено! Кликните по окну с объектами, чтобы завершить!")
window.exitonclick()
