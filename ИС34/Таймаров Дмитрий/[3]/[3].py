import heapq
def Greedy(maze, height, width, start, key): #Жадный алгоритм
    way = [start]
    x, y = start
    while way:
        if (x, y) == key:
            return way
        for delta_x, delta_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + delta_x, y + delta_y
            if 0 <= new_x < height and 0 <= new_y < width and maze[new_x][new_y]:
                way.append((new_x, new_y))
                maze[new_x][new_y] = 0
                x, y = new_x, new_y
                break
        else:
                way.pop()
                if way:
                    x, y = way[-1]
    return []

def Heuristic(row, column): #Эвристическая стоимость
    return abs(column[0] - row[0]) + abs(column[1] - row[1])

def Astar(maze,height,width,start,end): #Алогритм A*
    open_heap = [(0, start)]
    closed_heap = set()
    cost = {start: 0}
    previous = {}
    while open_heap:
        current = heapq.heappop(open_heap)[1]
        if current == end:
            way = []
            while current in previous:
                way.append(current)
                current = previous[current]
            way.append(start)
            way.reverse()
            return way
        closed_heap.add(current)
        for row, column in [(current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0], current[1] - 1), (current[0], current[1] + 1)]:
            if 0 <= row < height and 0 <= column < width and maze[row][column] != 0:
                expected_cost = cost[current] + 1
                if (row, column) in closed_heap and expected_cost >= cost.get((row, column), float("inf")):
                    continue
                if expected_cost < cost.get((row, column), float("inf")):
                    cost[(row, column)] = expected_cost
                    previous[(row, column)] = current
                    heapq.heappush(open_heap, (expected_cost + Heuristic((row, column), end), (row, column)))
    return []

mazefile = "maze-for-u.txt"
maze = []
greedymaze = []
astarmaze = []

with open(mazefile, "r", encoding="utf-8") as readfile:
    file = readfile.readlines()
    for line in file:
        shear = [0 if sym == "#" else 1 for sym in line[:-1]]
        maze.append(shear[:])
        greedymaze.append(shear[:])
        astarmaze.append(shear[:])

height = len(file)
width = len(file[0]) - 1
start = (58, 25)
print("Координаты аватара: ", start,"\n")
key = (542, 510)
continuator = key
print("\nКоординаты ключа: ", key,"\n")
escape = (355,421)
print("\nКоординаты выхода: ", escape,"\n")

greedyway = Greedy(greedymaze, height, width, start, key) #Поиск пути до ключа через жадный алгоритм
astarway = Astar(astarmaze, height, width, continuator, escape) #Поиск пути до выхода от ключа через алгоритм А*

print(greedyway,'\n',astarway)

with open("maze-for-me-done.txt", "w", encoding="utf-8") as writefile:
    for x in range(height):
        for y in range(width):
            if (x, y) == key:
                writefile.write("*")
            elif ((x, y) in astarway and (x, y) in greedyway):
                writefile.write(";")
            elif (x, y) in greedyway:
                writefile.write(".")
            elif (x, y) in astarway:
                writefile.write(",")
            elif maze[x][y] == 0:
                writefile.write("#")
            else:
                writefile.write(" ")
        writefile.write("\n")
print("Лабиринт пройден! Был создан файл: maze-for-me-done.txt")