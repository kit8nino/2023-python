import sys
sys.setrecursionlimit(1500)

def find_start_end_points(maze):
    for Y in range(len(maze[0])):
        if maze[0][Y] == " ":
            start = (0, Y)
            break
    for Y in range(len(maze[0])):
        if maze[len(maze) - 1][Y] == " ":
            end = (len(maze) - 1, Y)
            break
    return start, end


def find_key_position(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "*":
                key = (i, j)
                break
    return key


def dfs(maze, start, end, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    if start == end:
        return [start]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for direction in directions:
        x, y = start[0] + direction[0], start[1] + direction[1]

        if (0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] != "#" and (x, y) not in visited):
            path_found = dfs(maze, (x, y), end, visited)

            if path_found:
                return [(start)] + path_found

    return None



def a_star(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    l = [[0 for i in range(cols)] for j in range(rows)]

    l[start[0]][start[1]] = 1

    check_list = [(start[0], start[1], 0)]

    while len(check_list) > 0:
        check_list.sort(key=lambda x: x[2])
        i, j, d = check_list.pop(0)
        if i == end[0] and j == end[1]:
            path = []
            while d != 0:
                path.append((i, j))
                if i > 0 and l[i - 1][j] == d - 1:
                    i, j, d = i - 1, j, d - 1
                elif j > 0 and l[i][j - 1] == d - 1:
                    i, j, d = i, j - 1, d - 1
                elif i < rows - 1 and l[i + 1][j] == d - 1:
                    i, j, d = i + 1, j, d - 1
                elif j < cols - 1 and l[i][j + 1] == d - 1:
                    i, j, d = i, j + 1, d - 1
            path.append((i, j))
            path.reverse()
            return path

        if i > 0 and maze[i - 1][j] != "#" and l[i - 1][j] == 0:
            check_list.append((i - 1, j, d + 1))
            l[i - 1][j] = d + 1

        if j > 0 and maze[i][j - 1] != "#" and l[i][j - 1] == 0:
            check_list.append((i, j - 1, d + 1))
            l[i][j - 1] = d + 1

        if i < rows - 1 and maze[i + 1][j] != "#" and l[i + 1][j] == 0:
            check_list.append((i + 1, j, d + 1))
            l[i + 1][j] = d + 1

        if j < cols - 1 and maze[i][j + 1] != "#" and l[i][j + 1] == 0:
            check_list.append((i, j + 1, d + 1))
            l[i][j + 1] = d + 1

    return None


def modify_maze_path(maze, pathToKey, pathToExit):
    for coords in pathToKey:
        x, y = coords
        if maze[x][y] == " ":
            maze[x][y] = "."
    for coords in pathToExit:
        x, y = coords
        if maze[x][y] == " ":
            maze[x][y] = ","
    return maze


def write_modified_maze_to_file(maze, file_name):
    with open(file_name, 'w') as f:
        for line in maze:
            f.write("".join(line) + "\n")


if __name__ == '__main__':
    with open('maze-for-u.txt', 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]

    start, end = find_start_end_points(maze)
    key = find_key_position(maze)

    pathToKey = dfs(maze, start, key)
    pathToExit = a_star(maze, key, end)
    modified_maze = modify_maze_path(maze, pathToKey, pathToExit)
    write_modified_maze_to_file(modified_maze, 'maze-for-me-done.txt')
