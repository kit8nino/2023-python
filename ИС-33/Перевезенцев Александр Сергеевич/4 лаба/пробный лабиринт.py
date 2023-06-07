import turtle
from Avatar import Avatar
from Mob import Mob


def readMaze(file="test_maze.txt"):
    maze = [list(line.replace("#", "1").replace(" ", "0")) for line in open(file).read().split("\n")[:-1]]
    return maze


def mob_coords(maze):
    while 1:
        try:
            x = int(input(f"Введите координату X Моба в пределах от 0 до {len(maze) - 1}):"))
            if 0 <= x < len(maze):
                y = int(input(f"Введите координату Y Моба в пределах от 0 до {len(maze[0]) - 1}):"))
                if 0 <= y < len(maze[0]):
                    if str(maze[x][y]) == "1":
                        print("По этим координатам находится стена! Попробуйте ещё раз!")
                    else:
                        return x, y
                else:
                    print("Введённое значение выходит за пределы! Попробуйте ещё раз!")
                    continue
            else:
                print("Введённое значение выходит за пределы! Попробуйте ещё раз!")
                continue
        except Exception:
            print("Вы ввели неверное значение! Попробуйте ещё раз.")


def avatar_target(maze):
    for y in range(len(maze[0])):
        if maze[len(maze) - 1][y] == '0':
            return len(maze) - 1, y


def avatar_coords(maze):
    for y in range(len(maze[0])):
        if maze[0][y] == '0':
            return 0, y


def main():
    maze = readMaze()

    turtle.mode('logo')
    turtle.setup(width = 750, height = 750)

    maze_height = len(maze)
    maze_width = len(maze[0])

    wall = turtle.Turtle()
    wall.shape('square')
    wall.color('purple')
    wall.shapesize(2 / 20)
    wall.penup()
    wall.speed(5)

    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == "1":
                wall.goto(x * 3 - 50, -y * 3 + 50)
                wall.stamp()

    avatar_crds = avatar_coords(maze)
    avatar_crds = avatar_crds[0], avatar_crds[1]

    avatar_trg = avatar_target(maze)
    avatar_trg = avatar_trg[0], avatar_trg[1]

    mob_crds = mob_coords(maze)
    mob_crds = mob_crds[0], mob_crds[1]

    avatar = Avatar(avatar_crds, 1, 'blue', maze, avatar_trg)
    mob = Mob(mob_crds, 1, 'red')

    while True:
        avatar.make_move()

        if avatar.getPos() == avatar_trg:
            print("Аватар нашел выход и выжил")
            break

        if avatar.getPos() == mob.getPos():
            print("mob догнал и убил аватарика")
            break

        mob.make_move(maze, avatar.getPos())

        if avatar.getPos() == mob.getPos():
            print("mob догнал и убил аватарика")
            break


if __name__ == "__main__":
    main()
