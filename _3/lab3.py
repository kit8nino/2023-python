from random import shuffle

wall, path, visited = 1, 0, 3


def read_maze(file_name='test_maze.txt'):
    maze_raw = open(file_name).read().split('\n')[:-1]
    height = len(maze_raw)
    width = len(maze_raw[0])
    return [wall if x[i] == '#' else path for x in maze_raw
            for i in range(width)], width, height


def is_exit(coord, exit_coord):
    return coord[0] == exit_coord[0] and coord[1] == exit_coord[1]


def add_new_possible_ways(coord, maze=read_maze()[0],
                          width=read_maze()[2], height=read_maze()[1]):
    global path
    possibles = []
    coord_down = (coord[0] + 1) * width + coord[1]
    coord_up = (coord[0] - 1) * width + coord[1]
    coord_right = coord[0] * width + coord[1] + 1
    coord_left = coord[0] * width + coord[1] - 1
    coords = [coord_up, coord_down, coord_left, coord_right]
    max_coord = width * height
    coords = [x for x in coords if x < max_coord and x > -1]
    shuffle(coords)
    for c in coords:
        if maze[c] == path:
            possibles.append(c)
    return possibles


def choose_way(possible_ways):
    return possible_ways[-1]


def init_values(max_x, max_y):
    x = int(input(f"Avatar coord, x < {max_x}: "))
    y = int(input(f"Avatar coord, y < {max_y}: "))
    x_e = int(input(f"Exit coord, x < {max_x}: "))
    y_e = int(input(f"Exit coord, y < {max_y}: "))
    return (x, y), (x_e, y_e)


possible_ways = []
maze, width, height = read_maze()
# coord - всегда координаты аватара (текущего узла)
coord, exit_coord = init_values(width, height)
while not is_exit(coord, exit_coord):
    maze[coord[0] * width + coord[1]] = visited
    for el in add_new_possible_ways(coord, maze, width, height):
        possible_ways.append(el)
    new_coord = choose_way(possible_ways)
    coord = (new_coord // width, new_coord % width)

print('Exit found!')
