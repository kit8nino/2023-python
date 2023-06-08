import keyboard
import sys
import turtle

from scene import Scene
from scene import MazeDrawer
from scene import GameOver
from scene import Congratulation
from avatar import Avatar
from mob import Mob
import mazegen

width = 960
height = 780
turtle.setup(width=width+10, height=height+10)
turtle.screensize(width, height)
#turtle.bgcolor("#1bc1c1")

# Рисуй!
maze_drawer = MazeDrawer("maze.txt")
maze_drawer.run()
lable = Scene()

#logica:
with open('maze.txt', 'r') as f:
    maze_for_normal_people = [list(line.strip()) for line in f.readlines()]

my_avatar = Avatar("Player")
my_avatar.set_maze(maze_for_normal_people)

my_mob = Mob("MrCrabs", maze=maze_for_normal_people, avatar=my_avatar)
my_mob.set_avatar(my_avatar)

'''
WASD - Управление
Q - Выход
Enter - Начать игру
Чтобы изменить сложность, установить другое значение в set_difficult
'''

my_mob.set_difficult(3)

def caught(avat_cord,mob_cord,step,diff,end_coord):
    if step >= diff and avat_cord == mob_cord:
        GameOver()

    elif avat_cord == end_coord:
        Congratulation()



##Contol Panel:
def enter_btn(event):
    lable.hideturtle()
    my_avatar.showturtle()
    my_mob.showturtle()

def up_btn(event):
    my_avatar.move("up")
    my_mob.get_avatar_coord()
    my_mob.check_movement()
    turtle.update()
    caught(my_mob.get_avatar_coord(),my_mob.get_self_cood(),my_mob.get_self_moves(),my_mob.get_diff(),maze_drawer.find_last_coordinate())


def left_btn(event):
    my_avatar.move("left")
    my_mob.get_avatar_coord()
    my_mob.check_movement()
    turtle.update()
    caught(my_mob.get_avatar_coord(),my_mob.get_self_cood(),my_mob.get_self_moves(),my_mob.get_diff(),maze_drawer.find_last_coordinate())



def down_btn(event):
    my_avatar.move("down")
    my_mob.get_avatar_coord()
    my_mob.check_movement()
    turtle.update()
    caught(my_mob.get_avatar_coord(),my_mob.get_self_cood(),my_mob.get_self_moves(),my_mob.get_diff(),maze_drawer.find_last_coordinate())



def right_btn(event):
    my_avatar.move("right")
    my_mob.check_movement()
    turtle.update()
    caught(my_mob.get_avatar_coord(),my_mob.get_self_cood(),my_mob.get_self_moves(),my_mob.get_diff(),maze_drawer.find_last_coordinate())

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