from math import sqrt
from queue import PriorityQueue

def read_maze(filename):
    with open(filename) as file:
        maze = [[char for char in line.strip()] for line in file]
    return maze

#Соседние точки
def get_neighbors(maze, point: tuple[int, int]):
    x, y = point
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    neighbors_current = []
    for neighbor in neighbors:
        x, y = neighbor
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "#":
            neighbors_current.append(neighbor)
    return neighbors_current

#Поиск в ширину
def width_search(maze):
    start = (0, 1)
    end = (len(maze) - 1, len(maze[0]) - 2)
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

#Эвристическое расстояние
def get_heuristic(cell, end):
    return sqrt((cell[0] - end[0]) ** 2 + (cell[1] - end[1]) ** 2)

#A*
def way_to_exit(maze):
    start_point = (0, 1)
    end_point = (len(maze) - 1, len(maze[0]) - 2)
    queue = PriorityQueue()
    queue.put((0, start_point, [start_point]))
    visited_points = set()
    while not queue.empty():
        p, current_point, path = queue.get()
        if current_point == end_point:
            return p, path
        visited_points.add(current_point)
        for i in get_neighbors(maze, current_point):
            if i not in visited_points:
                new_way = path + [i]
                priority = len(new_way) + get_heuristic(i, end_point)
                queue.put((priority, i, new_way))
    return None

def main():
    #Width_search_alg
    filename = "maze-for-u.txt"
    maze = read_maze(filename)
    way_1 = width_search(maze)
    end = (len(maze) - 1, len(maze[0]) - 2)

    for place in way_1:
        maze[place[0]][place[1]] = "."
    maze[end[0]][end[1]] = "*"
    result_width = ""
    for j in maze:
        result_width += "".join(j) + "\n"

    with open("maze-for-me-done(width_search).txt", "w") as f:
        f.write(result_width)

    #A*_alg
    way_2 = way_to_exit(maze)
    way_2_ = way_2[1]

    for place in way_2_:
        maze[place[0]][place[1]] = ","
    maze[end[0]][end[1]] = "*"
    result_A = ""
    for i in maze:
        result_A += "".join(i) + "\n"

    with open("maze-for-me-done(A).txt", "w") as z:
        z.write(result_A)
main()