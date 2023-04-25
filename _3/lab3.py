from random import shuffle

wall, path, visited = 1, 0, 3
a, b = 1, 1
max_path_length = 1000


def read_maze(file_name='test_maze.txt'):
    maze_raw = open(file_name).read().split('\n')[:-1]
    height = len(maze_raw)
    width = len(maze_raw[0])
    return [wall if x[i] == '#' else path for x in maze_raw
            for i in range(width)], width, height


def check_init_coord(x, y, maze=read_maze()[0]):
    return True


def init_values(max_x, max_y):
    x = int(input(f"Avatar coord, x < {max_x}: "))
    y = int(input(f"Avatar coord, y < {max_y}: "))
    check_init_coord(x, y)
    x_e = int(input(f"Exit coord, x < {max_x}: "))
    y_e = int(input(f"Exit coord, y < {max_y}: "))
    check_init_coord(x_e, y_e)
    return (x, y), (x_e, y_e)


possible_ways = {}
maze, width, height = read_maze()
# coord - всегда координаты аватара (текущего узла)
start_coord, exit_coord = init_values(width, height)
coord = start_coord


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


def choose_way(possible_ways, max_len=max_path_length):
    possible_ways = sorted(possible_ways, key=possible_ways.get,
                           reversed=False)
    if len(possible_ways) > max_len:
        possible_ways = possible_ways[:max_len]
    coord = possible_ways.keys()[0]
    possible_ways.pop(coord)
    return coord


def calc_cost(c, maze=maze, width=width, height=height,
              sc=start_coord, se=exit_coord,
              alpha=a, beta=b):
    x, y = c // width, c % width
    sx, sy = sc // width, sc % width
    ex, ey = se // width, se % width
    deixt = ((x - sx)**2 + (y - sy)**2)**0.5
    greed = ((x - ex)**2 + (y - ey)**2)**0.5
    return alpha * deixt + beta * greed


while not is_exit(coord, exit_coord):
    maze[coord[0] * width + coord[1]] = visited
    for el in add_new_possible_ways(coord, maze, width, height):
        possible_ways[el] = calc_cost(el, maze=maze)
    new_coord = choose_way(possible_ways)
    coord = (new_coord // width, new_coord % width)

print('Exit found!')
