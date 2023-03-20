maze_raw = open('test_maze.txt').read().split('\n')[:-1]
height = len(maze_raw)
width = len(maze_raw[0])
wall, path, visited = 1, 0, 3
maze = [wall if x[i] == '#' else path for x in maze_raw for i in range(width)]
is_exit = False
st_p = 1


def is_path(coord, maze=maze, path=path):
    return maze[coord] == path


def check_routes(coord):
    new_coord = coord
    if is_path(coord - 1):
        new_coord -= 1
    elif is_path(coord + 1):
        new_coord += 1
    elif is_path(coord + width):
        new_coord += width
    elif is_path(coord - width):
        new_coord -= width
    else:
        new_coord = None
    return new_coord


while not is_exit:
    maze[st_p] = visited
    st_p = check_routes(st_p)
    if st_p is None:
        print('Dead end!')
        f = open('result.txt', 'w')
        for i in range(height):
            f.write(f'{maze[i * width:(i + 1) * width]}')
            f.write('\n')
        break
    if st_p // width == height - 1:
        is_exit = True
