def readMaze(file="maze-for-u.txt"):
    maze = [list(line.replace("#", "1").replace(" ", "0")) for line in open(file).read().split("\n")[:-1]]
    return maze


def key(maze):
    while 1:
        try:
            x = int(input(f"Введите координату X ключевой точки в пределах от 0 до {len(maze)-1}):"))
            if x >= 0 and x < len(maze):
                y = int(input(f"Введите координату Y ключевой точки в пределах от 0 до {len(maze[0]) - 1}):"))
                if y >= 0 and y < len(maze[0]):
                    if str(maze[x][y]) == "1":
                        print("По этим координатам находится стена! Попробуйте ещё раз!")
                    else:
                        return (x, y)
                else:
                    print("Введённое значение выходит за пределы! Попробуйте ещё раз!")
                    continue
            else:
                print("Введённое значение выходит за пределы! Попробуйте ещё раз!")
                continue
        except Exception:
            print("Вы ввели неверное значение! Попробуйте ещё раз.")


def end(maze):
    for y in range(len(maze[0])):
        if maze[len(maze)-1][y] == '0':
            return (len(maze)- 1,y)


def start(maze):
    for y in range(len(maze[0])):
        if maze[0][y] == '0':
            return (0,y)

def heuristic(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def get_neighbors(maze, pos):
    row, col = pos
    candidates = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]
    result = []
    for r, c in candidates:
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == "0":
            result.append((r, c))

    return result

def greedy_first_search(maze, start, goal):
    frontier = [start]
    visited = []
    currentList = [start]
    while len(frontier) != 0:
        current = min(frontier, key=lambda n: heuristic(n, goal))
        currentList.append(current)
        if current == goal:
            return get_path(currentList)
        frontier.remove(current)
        visited.append(current)
        neighbors = get_neighbors(maze, current)
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in frontier:
                frontier.append(neighbor)

def get_path(current):
    path = [current[-1]]
    current = list(reversed(current))
    i = len(current)
    for j in range(i-1):
        if ((current[0][0]-path[-1][0])**2 + (current[0][1]-path[-1][1])**2)**(1/2) == 1:
            path.append(current[0])
            del current[0]
        else:
            del current[0]
    return list(reversed(path))


def astar(maze, start, end):
    path = []
    distances = {start: 0}
    previous = {}
    to_visit = [start]
    while to_visit:
        current = to_visit.pop(0)
        if current == end:
            break
        neighbors = get_neighbors(maze, current)
        for neighbor in neighbors:
            distance = distances[current] + 1
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                to_visit.append(neighbor)
                to_visit.sort(key=lambda x: distances[x] + heuristic(x, end))
    if end in previous:
        current = end
        while current != start:
            path.insert(0, current)
            current = previous[current]
        path.insert(0, start)
    return path

def main():
    maze = readMaze()
    key_coords = key(maze)
    greedyPath = greedy_first_search(maze,start(maze),key_coords)
    astarPath = astar(maze, key_coords, end(maze))
    for point in greedyPath:
        maze[point[0]][point[1]] = "."

    for point in astarPath:
        maze[point[0]][point[1]] = ","

    maze[key_coords[0]][key_coords[1]] = "*"
    with open("maze-for-me-done.txt", "w") as f:
        f.write('\n'.join([''.join(map(str, line)) for line in maze]))
        print("Лабиринт пройден!\nПуть находится в файле 'maze-for-me-done.txt'!")

main()
