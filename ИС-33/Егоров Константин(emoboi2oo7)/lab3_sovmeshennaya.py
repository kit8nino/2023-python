from queue import PriorityQueue
from math import sqrt

def read_maze(filename):
    """
    Считывает лабиринт из текстового файла и возвращает его в виде двумерного массива
    """
    with open(filename) as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze


def get_neighbors(maze, cell: tuple[int, int]):
    """
    Возвращает список соседних ячеек, в которые можно перейти
    """
    row, col = cell
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    valid_neighbors = []
    for neighbor in neighbors:
        row, col = neighbor
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
            valid_neighbors.append(neighbor)
    return valid_neighbors

#Поиск в ширину
def find_path(maze):
    """
    Ищет путь от начальной точки до конечной точки в лабиринте
    """
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

#А*
def get_heuristic(cell, end):
    """
    Вычисляет эвристическое расстояние от ячейки до конечной точки
    """
    return sqrt((cell[0] - end[0]) ** 2 + (cell[1] - end[1]) ** 2)

def find_path_a_star(maze):
    """
    Ищет путь от начальной точки до конечной точки в лабиринте, используя алгоритм A*
    """
    start = (0, 1)
    end = (len(maze) - 1, len(maze[0]) - 2)
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    visited = set()
    while not queue.empty():
        p, current, path = queue.get()
        if current == end:
            return p, path
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                priority = len(new_path) + get_heuristic(neighbor, end)
                queue.put((priority, neighbor, new_path))
    return None


def main():
    filename = "maze-for-u.txt"
    maze = read_maze(filename)
    """
    Реализация создания выходного файла для поиска в ширину
    """
    path1 = find_path(maze)
    
    for place in path1:
        maze[place[0]][place[1]] = "."

    result1 = ""
    for line in maze:
        result1 += "".join(line) + "\n"

    with open("res1.txt", "w") as f:
        f.write(result1)

    """
    Реализация создания выходного файла для А*
    """
    path2 = find_path_a_star(maze)
    path22 = path2[1]

    for place in path22:
        maze[place[0]][place[1]] = ","

    result2 = ""
    for line in maze:
        result2 += "".join(line) + "\n"

    with open("res2.txt", "w") as f:
        f.write(result2)
main()
