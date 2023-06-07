def available_paths(point, maze):
    x, y = point
    x_length = len(maze)
    y_length = len(maze[0])
    awailable_ways = []

    if (x - 1) >= 0 and maze[x - 1][y] == " ":
        waypoint = (x - 1, y)
        awailable_ways.append(waypoint)

    if (y + 1) < y_length and maze[x][y + 1] == " ":
        waypoint = (x, y + 1)
        awailable_ways.append(waypoint)

    if (x + 1) < x_length and maze[x + 1][y] == " ":
        waypoint = (x + 1, y)
        awailable_ways.append(waypoint)

    if (y - 1) >= 0 and maze[x][y - 1] == " ":
        waypoint = (x, y - 1)
        awailable_ways.append(waypoint)
    return awailable_ways


def dijkstra(maze, start, end):
    open_list = [start]
    closed_list = []
    came_from = {}
    g_score = {start: 0}

    while open_list:
        current = min(open_list, key=lambda x: g_score[x])
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in available_paths(current, maze):
            if neighbor in closed_list:
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                if neighbor not in open_list:
                    open_list.append(neighbor)
    return open_list


def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])


def a_star(maze, start, end):
    open_list = [start]
    closed_list = []
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_list:
        current = min(open_list, key=lambda x: f_score[x])
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in available_paths(current, maze):
            if neighbor in closed_list:
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return open_list


def replace_path(maze, path, symbol):
    for x, y in path:
        if maze[x][y] != ' ':
            maze[x][y] = ';'
        else:
            maze[x][y] = symbol
    return maze


if __name__ == '__main__':
    with open('maze-for-u.txt', 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]

    for Y in range(len(maze[0])):
        if maze[0][Y] == " ":
            start = (0, Y)
            break

    for Y in range(len(maze[0])):
        if maze[len(maze) - 1][Y] == " ":
            end = (len(maze) - 1, Y)
            break

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "*":
                key = (i, j)
                maze[i][j] = " "
                break

    path_to_key = dijkstra(maze, start, key)
    path_to_end = a_star(maze, key, end)

    result = replace_path(replace_path(maze, path_to_key, '.'), path_to_end, ',')
    x_key, y_key = key
    result[x_key][y_key] = '*'

    with open('maze-for-me-done.txt', 'w') as f:
        for line in result:
            f.write("".join(line) + "\n")
