from collections import deque
from math import sqrt
from queue import PriorityQueue

parents = {}


def get_lab(filename):
    with open(filename) as file:
        maze = file.read().split('\n')
        for i in range(len(maze) - 1):
            maze[i] = [char for char in maze[i]]
    return maze


# поиск соседей
def get_valid_neighbors(coord, maze):
    neighbors = [(coord[0] + 1, coord[1]), (coord[0], coord[1] - 1), (coord[0], coord[1] + 1),
                 (coord[0] - 1, coord[1])]  # Снизу, слева, справа, сверху
    valid_neighbors = []
    for el in neighbors:
        row, col = el
        if row >= 0 and row < len(maze) and col >= 0 and col < len(maze[0]) and maze[row][col] != '#':
            valid_neighbors.append(el)
    return valid_neighbors


# Проходка вширь для поиска пути (родитель записывается в словарь)
def search_in_width(maze, start, end):
    search_deque = deque()
    search_deque.append(start)
    searched = set()
    while search_deque:
        coord = search_deque.popleft()
        if coord == end:
            print("Success!")
            return
        searched.add(coord)
        neighbors = get_valid_neighbors(coord, maze)
        for n in neighbors:
            if n not in searched:
                parents[n] = coord  # запись родителя
                search_deque.append(n)
    return


parents2 = {}


def get_heuristic(cell, end):
    return sqrt((cell[0] - end[0]) ** 2 + (cell[1] - end[1]) ** 2)


# проход по родителям для поиска пути к выходу
def get_path_1(node, start, path):
    while node != start:
        path.append(parents[node])
        node = parents[node]


def search_in_A(maze, start, end):
    path_new = []
    queue = PriorityQueue()
    queue.put((0, start))
    searched = set()
    while not queue.empty():
        p, coord = queue.get()
        if coord == end:
            print("Success for A*")
            return p
        searched.add(coord)
        neighbors = get_valid_neighbors(coord, maze)
        for n in neighbors:
            if n not in searched:
                parents2[n] = coord  # запись родителя
                if coord == start:
                    get_path_1(n, start, path_new)
                else:
                    path_new.append(n)
                priority = len(path_new) + get_heuristic(n, end)
                queue.put((priority, n))
    return


def main():
    filename = 'maze-for-u.txt'

    # преобразование лабиринта в матрицу
    maze = get_lab(filename)

    start = (0, 1)
    end = (len(maze) - 2, len(maze[0]) - 2)
    path = []

    # поиск путей
    search_in_width(maze, start, end)
    # получение пути к выходу
    get_path_1(end, start, path)

    # заполнение матрицы лабиринта
    for place in path:
        maze[place[0]][place[1]] = "."
    maze[end[0]][end[1]] = "*"
    result1 = ""
    # преобразование матрицы в строку
    for line in maze:
        result1 += "".join(line) + "\n"
    # запись лабиринта в файл
    with open("res3.txt", "w") as f:
        f.write(result1)

    # для А*
    path2 = []
    search_in_A(maze, start, end)
    get_path_1(end, start, path2)

    for place in path2:
        maze[place[0]][place[1]] = ","
    maze[end[0]][end[1]] = "*"
    result2 = ""
    for line in maze:
        result2 += "".join(line) + "\n"

    with open("res4.txt", "w") as f:
        f.write(result2)


if __name__ == '__main__':
    main()
