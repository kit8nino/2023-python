import keyboard
import sys
import turtle

from scene import Scene
from scene import MazeDrawer
from avatar import Avatar
from mob import Mob

width = 960
height = 780
turtle.setup(width=width+10, height=height+10)
turtle.screensize(width, height)



# Рисуй!
maze_drawer = MazeDrawer("maze.txt")
maze_drawer.run()
#lable = Scene()

#logica:


with open('maze.txt', 'r') as f:
    maze_for_normal_people = [list(line.strip()) for line in f.readlines()]


my_avatar = Avatar("Player")
my_avatar.set_maze(maze_for_normal_people)


my_mob = Mob("MrCrabs", maze=maze_for_normal_people, avatar=my_avatar)
my_mob.set_avatar(my_avatar)

print(my_avatar.get_coord_log())
print(my_mob.get_self_cood())



#Contol Panel:

# Функции обработки нажатия клавиш
def enter_btn(event):
    #lable.hideturtle()
    my_avatar.showturtle()
    my_mob.showturtle()

def up_btn(event):
    my_avatar.move("up")
    my_mob.get_avatar_coord()
    my_mob.check_movement()
    turtle.update()
    print(my_avatar.get_coord_log())
    print(my_mob.get_self_cood())

def left_btn(event):
    my_avatar.move("left")
    my_mob.get_avatar_coord()
    my_mob.check_movement()
    turtle.update()
    print(my_avatar.get_coord_log())
    print(my_mob.get_self_cood())

def down_btn(event):
    my_avatar.move("down")
    my_mob.get_avatar_coord()
    my_mob.check_movement()
    turtle.update()
    print(my_avatar.get_coord_log())
    print(my_mob.get_self_cood())

def right_btn(event):
    my_avatar.move("right")
    my_mob.check_movement()
    turtle.update()
    print(my_avatar.get_coord_log())
    print(my_mob.get_self_cood())
def quit_btn(event):
    turtle.bye()  # Выход
    sys.exit()


# Привязываем кнопачки
keyboard.on_press_key("w", up_btn)

keyboard.on_press_key("s", down_btn)

keyboard.on_press_key("a", left_btn)

keyboard.on_press_key("d", right_btn)

keyboard.on_press_key("q", quit_btn)
keyboard.on_press_key("enter", enter_btn)



# рест энд пис черепыха
turtle.done()