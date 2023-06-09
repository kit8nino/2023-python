import sys
import heapq

sys.setrecursionlimit(10000)


def readMaze():
    maze = []

    # Открываем файл с лабиринтом и считываем его в матрицу
    with open("maze-for-u.txt", "r") as f:
        file = f.readlines()

        height = len(file)
        width = len(file[0]) - 1

        for line in file:
            tmp_line = [0 if sym == "#" else 1 for sym in line[:-1]]
            maze.append(tmp_line[:])

    return maze, height, width



# Функция с алгоритмом поиска пути в глубину в лабиринте от точки Start до точки End
def depth_first_search(maze, height, width, start, end):
    def dfs(curr):
        nonlocal visited, path

        if curr == end:  
            path.append(curr)
            return True

        visited.add(curr)  

        # перебираем соседние вершины
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = curr[0] + dx, curr[1] + dy

            if 0 <= x < height and 0 <= y < width and maze[x][y] == 1 and (x, y) not in visited:
                # если соседняя вершина проходима и еще не была посещена
                if dfs((x, y)):  # рекурсивно вызываем функцию для этой вершины
                    path.append(curr)
                    return True

        return False  # если не нашли путь, возвращаем False

    visited = set()  
    path = []  

    dfs(start)

    return path[::-1]  # возвращаем путь в обратном порядке


# Функция с алгоритмом A* поиска пути в лабиринте от точки Start до точки End
def a_star(maze, height, width, start, end):
    def heuristic(curr, end):
        # эвристическая функция - оценка расстояния до целевой точки
        return abs(curr[0] - end[0]) + abs(curr[1] - end[1])

    pq = []  # очередь с приоритетом
    parent = {}  # словарь для хранения предков вершин
    g_score = {start: 0}  # словарь для хранения стоимости пути до вершины
    f_score = {start: heuristic(start, end)}  # словарь для хранения эвристической оценки стоимости пути

    heapq.heappush(pq, (f_score[start], start))  # добавляем начальную вершину в очередь

    while pq:
        curr_f, curr = heapq.heappop(pq)

        if curr == end:  # если достигли конечной точки, возвращаем путь
            path = []
            while curr in parent:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            return path[::-1]

        # перебираем соседние вершины
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = curr[0] + dx, curr[1] + dy

            if 0 <= x < height and 0 <= y < width and maze[x][y] == 1:
                # если соседняя вершина проходима
                next_node = (x, y)
                new_g_score = g_score[curr] + 1  # стоимость пути до соседней вершины

                if next_node not in g_score or new_g_score < g_score[next_node]:
                    # если соседняя вершина еще не обрабатывалась или найден новый более короткий путь до нее
                    parent[next_node] = curr
                    g_score[next_node] = new_g_score
                    f_score[next_node] = new_g_score + heuristic(next_node, end)
                    heapq.heappush(pq, (f_score[next_node], next_node))

    return []  # если не нашли путь, возвращаем пустой список


def writeMaze():
    # Выводим лабиринт с путями в текстовый файл
    with open("maze-for-me-done.txt", "w") as f:
        for x in range(height):
            for y in range(width):
                if (x, y) == key_pos:
                    f.write("*")
                elif (x, y) in path_to_key:
                    f.write(".")
                elif (x, y) in path_to_exit:
                    f.write(",")
                elif maze[x][y] == 0:
                    f.write("#")
                else:
                    f.write(" ")
            f.write("\n")


maze, height, width = readMaze()

'''

# Ввод исходных данных
print(f"Координаты аватара через пробел: ", end="")
avatar_pos = tuple([int(_) for _ in input().split()])
print(f"\nКоординаты ключа через пробел: ", end="")
key_pos = tuple([int(_) for _ in input().split()])
print(f"\nКоординаты выхода через пробел: ", end="")
exit_pos = tuple([int(_) for _ in input().split()])

'''

print("Координаты аватара через пробел: 0 1")
print("Координаты ключа через пробел: 466 592")
print("Координаты выхода через пробел: 599 798")

avatar_pos = 0, 1
key_pos = 466, 592
exit_pos = 599, 798

# Вычисляем пути от входа до ключа и от ключа до выхода
path_to_key = depth_first_search(maze, height, width, avatar_pos, key_pos)
path_to_exit = a_star(maze, height, width, key_pos, exit_pos)

writeMaze()
