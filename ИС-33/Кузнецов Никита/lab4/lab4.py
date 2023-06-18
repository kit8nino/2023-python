import turtle
from _avatar import Avatar
from _mob import Mob

def main():
    win = turtle.Screen()
    avatar = Avatar(speed=10, target=(380, -380))
    avatar.init_path()
    avatar.pensize(2)
    avatar.color("black")
    mob = Mob(speed=1, target_turtle=avatar)
    mob.pensize(2)
    mob.color("green")
    while not avatar.is_finish:
        avatar.move().__next__()
        mob.move().__next__()
    win.exitonclick()

if __name__ == "__main__":
    main()