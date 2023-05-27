from queue import Queue

def read_maze(fileMaze="maze-for-me.txt"):
    maze = [list(line.replace("#", "1").replace(" ", "0")) for line in open(fileMaze).read().split("\n")[:-1]]
    return maze

# Узнаём размеры лабиринта
try:
    maze = read_maze()
    size_x = len(maze)
    size_y = len(maze[0])
except Exception:
    print("Исходный файл не найден!")

def near(x, y, maze):
    near = []
    if y == 0:
        if x == 0:
            near = [["#", maze[x][y + 1]],
                    [maze[x + 1][y], maze[x + 1][y + 1]]]
        elif x == (size_x - 1):
            near = [[maze[x - 1][y], maze[x - 1][y + 1]],
                    ["#", maze[x][y + 1]]]
        else:
            near = [[maze[x - 1][y], maze[x - 1][y + 1]],
                    ["#", maze[x][y + 1]],
                    [maze[x + 1][y], maze[x + 1][y + 1]]]
    elif y == (size_y - 1):
        if x == 0:
            near = [[maze[x][y - 1], "#"],
                    [maze[x + 1][y - 1], maze[x + 1][y]]]
        elif x == (size_x - 1):
            near = [[maze[x - 1][y - 1], maze[x - 1][y]],
                    [maze[x][y - 1], "#"]]
        else:
            near = [[maze[x - 1][y - 1], maze[x - 1][y]],
                    [maze[x][y - 1], "#"],
                    [maze[x + 1][y - 1], maze[x + 1][y]]]
    elif x == 0:
        near = [[maze[x][y - 1], "#", maze[x][y + 1]],
                [maze[x + 1][y - 1], maze[x + 1][y], maze[x + 1][y + 1]]]
    elif x == (size_x - 1):
        near = [[maze[x - 1][y - 1], maze[x - 1][y], maze[x - 1][y + 1]],
                [maze[x][y - 1], "#", maze[x][y + 1]]]
    else:
        near = [[maze[x - 1][y - 1], maze[x - 1][y], maze[x - 1][y + 1]],
                [maze[x][y - 1], "#", maze[x][y + 1]],
                [maze[x + 1][y - 1], maze[x + 1][y], maze[x + 1][y + 1]]]
    return near # Возможные пути

def sel_start(maze): # узнаем координаты входа
    while 1:
        try:
            x = int(input("Введите точку входа X: "))
            if x >= 0 and x < size_x:
                y = int(input("Введите точку входа Y: "))
                if y >= 0 and y < size_y:
                    if str(maze[x][y]) == "1":
                        print("\nТут нет входа..")
                    else:
                        return (x, y)
                else:
                    print("\nВы ушли за пределы карты")
                    continue
            else:
                print("\nВы ушли за пределы карты")
                continue
        except Exception:
            print("\nЧто-то не то, давайте попробуем ещё раз")

def sel_tresuaerr(maze): # узнаём координаты нашего сокровища
    while 1:
        try:
            x = int(input("Координата ключа X: "))
            if x >= 0 and x < size_x:
                y = int(input("Координата ключа Y: "))
                if y >= 0 and y < size_y:
                    if str(maze[x][y]) == "1":
                        print("\nТут стенка")
                    else:
                        return (x, y)
                else:
                    print("\nВы ушли за пределы карты")
                    continue
            else:
                print("\nВы ушли за пределы карты")
                continue
        except Exception:
            print("\nЧто-то не то, давайте попробуем ещё раз")

def sel_exit(maze): # находим доступный выход
    for y in range(size_y):
        if int(maze[size_x-1][y]) == 0:
            return (size_x - 1,y)

start = sel_start(maze) # задаём точку старта
zvezda = sel_tresuaerr(maze) # задаём точку сокровища
end = sel_exit(maze) # задаём выход


def get_moves(pos, maze): # доступные движения (вверх, вниз, влево, вправо)
    moves = []
    if pos[0] > 0 and not int(maze[pos[0] - 1][pos[1]]):
        moves.append((pos[0] - 1, pos[1]))
    if pos[0] < size_x - 1 and not int(maze[pos[0] + 1][pos[1]]):
        moves.append((pos[0] + 1, pos[1]))
    if pos[1] > 0 and not int(maze[pos[0]][pos[1] - 1]):
        moves.append((pos[0], pos[1] - 1))
    if pos[1] < size_y - 1 and not int(maze[pos[0]][pos[1] + 1]):
        moves.append((pos[0], pos[1] + 1))
    return moves

def bfs(start, end): # делаем поиск в ширину 
    queue = Queue()
    queue.put((start, [start]))
    while not queue.empty():
        pos, path = queue.get()
        if pos == end:
            return path
        for move in get_moves(pos, maze):
            if move not in path:
                queue.put((move, path + [move]))
    return None

way_bfs = bfs(start, zvezda) # поиск в ширину ДО сокровища

def heuristic(current, end): # узнаём цену выхода
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

def a(maze, start, end): # делаем метод A звёздочка
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

        for neighbor in get_moves(current, maze):
            if neighbor in closed_list:
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None

way_a = a(maze, zvezda, end) # находим путь от сокровища до выхода

try:
    for point in way_bfs:
        maze[point[0]][point[1]] = "." # От входа, до сокровища

    # Заносим путь от ключа до выхода
    for point in way_a:
        maze[point[0]][point[1]] = "," # От сокровища, до выхода

    maze[zvezda[0]][zvezda[1]] = "*"

    with open("itog.txt", "w") as f:
        f.write('\n'.join([''.join(map(str, line)) for line in maze]))
except Exception:
    print("Ошибка поиска пути")        

with open('itog.txt') as f:
    text = f.read()
    
text = text.replace('0', ' ').replace('1', '#')
 
with open('itog.txt', 'w') as f:
    f.write(text)
