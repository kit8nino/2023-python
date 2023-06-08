
def get_neighbors(point, maze):
    x, y = point
    neighbors_list = []

    if x > 0:
        neighbors_list.append((x - 1, y))
    if y > 0:
        neighbors_list.append((x, y - 1))
    if x < len(maze) - 1:
        neighbors_list.append((x + 1, y))
    if y < len(maze[0]) - 1:
        neighbors_list.append((x, y + 1))

    return neighbors_list


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def greedy(maze, start, end):
    open_list = [(start, 0)]
    closed_list = set()
    came_from = {}

    while len(open_list) > 0:
        current, _ = open_list.pop(0)
        if current == end:
            return path(came_from, end)

        closed_list.add(current)
        for neighbor in get_neighbors(current, maze):
            if neighbor in closed_list or maze[neighbor[0]][neighbor[1]] == 0:
                continue
            if neighbor not in [x[0] for x in open_list]:
                came_from[neighbor] = current
                priority = manhattan_distance(neighbor, end)
                open_list.append((neighbor, priority))

        open_list.sort(key=lambda x: x[1])

    return None


def astar(maze, start, end):
    open_list = [start]
    closed_list = []
    g_scores = {start: 0}
    f_scores = {start: manhattan_distance(start, end)}
    came_from = {}

    while open_list:
        current = min(open_list, key=lambda x: f_scores[x])

        if current == end:
            return path(came_from, end)

        open_list.remove(current)
        closed_list.append(current)

        for neighbor in get_neighbors(current, maze):
            if neighbor in closed_list or maze[neighbor[0]][neighbor[1]] == 0:
                continue

            tentative_g_score = g_scores[current] + 1

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g_score >= g_scores[neighbor]:
                continue

            came_from[neighbor] = current
            g_scores[neighbor] = tentative_g_score
            f_scores[neighbor] = g_scores[neighbor] + manhattan_distance(neighbor, end)

    return None


def read_maze(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

        h = len(lines)
        w = len(lines[0]) - 1
        maze = []

        for line in lines:
            tmp_line = [0 if sym == "#" else 1 for sym in line[:-1]]
            maze.append(tmp_line[:])

    return h, w, maze


def write_maze(filename, h, w, maze, key_pos, path_k, path_e):
    with open(filename, "w") as file:
        for x in range(h):
            for y in range(w):
                if (x, y) == key_pos:
                    file.write("*")
                elif (x, y) in path_k:
                    file.write(".")
                elif (x, y) in path_e:
                    file.write(",")
                elif maze[x][y] == 0:
                    file.write("#")
                else:
                    file.write(" ")
            file.write("\n")


input_file_name = "maze-for-u.txt"
output_file_name = "maze-for-me-done.txt"

h, w, maze = read_maze(input_file_name)

print("coordinates of avatar:")
avatar_x, avatar_y = int(input(f"0 <= x <= {w - 1}: ")), int(input(f"0 <= y <= {h - 1}: "))
avatar_pos = (avatar_x, avatar_y)

print("coordinates of key:")
key_x, key_y = int(input(f"0 <= x < {w - 1}: ")), int(input(f"0 <= y < {h - 1}: "))
key_pos = (key_x, key_y)

print("coordinates of exit:")
exit_x, exit_y = int(input(f"0 <= y < {w - 1}: ")), int(input(f"0 <= y < {h - 1}: "))
exit_pos = (exit_x, exit_y)

path_key = greedy(maze, avatar_pos, key_pos)
path_exit = astar(maze, key_pos, exit_pos)

write_maze(output_file_name, h, w, maze, key_pos, path_key, path_exit)

"""

0
1
456
444
599
798
"""

