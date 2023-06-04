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
lable = Scene()

#logica:
with open('maze.txt', 'r') as f:
    coord_for_normal_people = [list(line.strip()) for line in f.readlines()]
x_log = 1
y_log = 1





my_avatar = Avatar("Player")
my_mob = Mob("Jaba")

#Contol Panel:





# Функции обработки нажатия клавиш
def enter_btn(event):
    lable.hideturtle()
    my_avatar.showturtle()
    my_mob.showturtle()
def up_btn(event):
    if coord_for_normal_people[x_log][y_log + 1] != "#":
        return my_avatar.move("up")
        

def left_btn(event):
    my_avatar.move("left")
def down_btn(event):
    my_avatar.move("down") # кто даун? я даун?
def right_btn(event):
    my_avatar.move("right")
def quit_btn(event):
    turtle.bye()  # Выход
    sys.exit()

##
def ups_btn(event):
    my_mob.move("up")
def lefts_btn(event):
    my_mob.move("left")
def downs_btn(event):
    my_mob.move("down") # кто даун? я даун?
def rights_btn(event):
    my_mob.move("right")

##
# Привязываем кнопачки
keyboard.on_press_key("w", up_btn)
keyboard.on_press_key("up", ups_btn)
keyboard.on_press_key("s", down_btn)
keyboard.on_press_key("down", downs_btn)
keyboard.on_press_key("a", left_btn)
keyboard.on_press_key("left", lefts_btn)
keyboard.on_press_key("d", right_btn)
keyboard.on_press_key("right", rights_btn)
keyboard.on_press_key("q", quit_btn)
keyboard.on_press_key("enter", enter_btn)

# рест энд пис черепыха
turtle.done()