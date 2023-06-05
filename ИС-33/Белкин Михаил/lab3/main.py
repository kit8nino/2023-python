# Класс узла
class Node:
    def __init__(self, parent=None, pos=None):  # Конструктор узла
        self.parent = parent  # Родитель из которого можно попасть в этот узел
        self.pos = pos  # Коорди наты узла

        self.g = 0  # Стоимость пути от начального узла до этого узла
        self.h = 0  # Эвристическое приближение стоимости пути от этого узла до конечного узла
        self.f = 0  # Минимальная стоимость перехода в этот узел

    def __eq__(self, other):  # Перегрузка оператора равенства (==)
        return self.pos == other.pos


# Функция с алгоритмом A* поиска пути в лабиринте от точки Start до точки End
def Search_Astar(maze, height, width, start, end):
    start_node = Node(None, start)  # Создаем стартовый узел
    end_node = Node(None, end)  # Создаем конечный узел

    start_node.g = 0
    start_node.h = (((start_node.pos[0] - end_node.pos[0]) ** 2) +
                    ((start_node.pos[1] - end_node.pos[1]) ** 2)) ** 0.5
    start_node.f = start_node.g + start_node.h

    not_visited = [start_node]  # Список непосещенных узлов
    visited = []  # Список посещенных узлов

    while len(not_visited) > 0:  # Пока список непосещенных узлов непустой
        cur_node = not_visited[0]  # Берем первый узел в списке непосещенных
        cur_ind = 0  # Его индекс

        # Перебираем индексы непосещенных узлов, чтобы найти узел с наименьшей стоимостью перемещения
        for ind in range(len(not_visited)):
            if not_visited[ind].f < cur_node.f:
                cur_node = not_visited[ind]
                cur_ind = ind

        not_visited.pop(cur_ind)  # Удаляем узел с наименьшей стоимостью перемещения из списка непосещенных
        visited.append(cur_node)  # Добавляем его в список посещенных

        if cur_node == end_node:  # Если узел, в котором мы сейчас находимся, является финальным узлом
            path = []

            cur = cur_node
            while cur is not None:  # Проходимся по ветке узлов
                path.append(cur.pos)  # Генерируем путь
                cur = cur.parent

            return path

        for new_pos in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Перебираем все возможные перемещения
            node_pos = (cur_node.pos[0] + new_pos[0], cur_node.pos[1] + new_pos[1])  # Вычисляем позицию соседнего узла

            # Если координаты соседнего узла не за границами лабиринта и не является стеной
            if (0 <= node_pos[0] < height and
                    0 <= node_pos[1] < width and
                    maze[node_pos[0]][node_pos[1]]):
                new_node = Node(cur_node, node_pos)  # Создаем новый узел

                if new_node not in visited:
                    # Вычисляем веса
                    new_node.g = cur_node.g + 1
                    new_node.h = (((new_node.pos[0] - end_node.pos[0]) ** 2) +
                                  ((new_node.pos[1] - end_node.pos[1]) ** 2)) ** 0.5
                    new_node.f = new_node.g + new_node.h

                    eq_nodes = []

                    # Ищем этот узел в списке непосещенных и удаляем те,
                    # у которых узлы имеет стоимость перемещения больше
                    for i in range(len(not_visited)):
                        if new_node == not_visited[i]:
                            if new_node.f > not_visited[i].f:
                                eq_nodes.append(not_visited[i])
                            else:
                                not_visited.pop(i)

                    # Если есть нет узлов, которые соответствуют данному узлу, то добавляем его в список непосещенных
                    if len(eq_nodes) <= 0:
                        not_visited.append(new_node)

    return []


# Функция с жадным алгоритмом поиска пути в лабиринте от точки Start до точки End
def Search_BestFirst(maze, height, width, start, end):
    path = [start]  # Путь до выхода
    x, y = start

    while path:  # Пока есть путь
        if (x, y) == end:  # Если точка соответствует координатам выхода
            return path

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Перебираем все возможные перемещения
            nx, ny = x + dx, y + dy

            # Если соседняя позиция не выходит за границы лабиринта и не является стеной
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny]:
                path.append((nx, ny))  # Добавляем точку в путь до выхода
                maze[nx][ny] = 0  # Закрываем путь назад

                x, y = nx, ny

                break
        else:  # Если пришли в тупик
            path.pop()  # Удаляем последнюю точку из пути
            if path:
                x, y = path[-1]  # Возвращаемся в предыдущую точку

    return []


# Имя файла с лабиринтом
# input_file_name = "test_maze.txt"
input_file_name = "maze-for-u.txt"
output_file_name = "maze-for-me-done.txt"

# Лабиринты
maze = []
key_maze = []
exit_maze = []

# Открываем файл с лабиринтом и считываем его в матрицу
with open(input_file_name, "r", encoding="utf-8") as f:
    file = f.readlines()

    height = len(file)
    width = len(file[0]) - 1

    for line in file:
        tmp_line = [0 if sym == "#" else 1 for sym in line[:-1]]
        maze.append(tmp_line[:])
        key_maze.append(tmp_line[:])
        exit_maze.append(tmp_line[:])

# Ввод исходных данных
print("Координаты аватара:")
avatar_ = (int(input(f"[0 <= x <= {width - 1}]: ")), int(input(f"[0 <= y <= {height - 1}]: ")))

print("\nКоординаты ключа:")
key_ = (int(input(f"[0 <= x < {width - 1}]: ")), int(input(f"[0 <= y < {height - 1}]: ")))

print("\nКоординаты выхода:")
exit_ = (int(input(f"[0 <= y < {width - 1}]: ")), int(input(f"[0 <= y < {height - 1}]: ")))

# Вычисляем пути от входа до ключа и от ключа до выхода
path_to_key = Search_BestFirst(key_maze, height, width, avatar_, key_)
path_to_exit = Search_Astar(exit_maze, height, width, key_, exit_)

# Выводим лабиринт с путями в текстовый файл
with open(output_file_name, "w", encoding="utf-8") as f:
    for x in range(height):
        for y in range(width):
            if (x, y) == key_:
                f.write("*")
            elif ((x, y) in path_to_exit and
                  (x, y) in path_to_key):
                f.write(";")
            elif (x, y) in path_to_key:
                f.write(".")
            elif (x, y) in path_to_exit:
                f.write(",")
            elif maze[x][y] == 0:
                f.write("#")
            else:
                f.write(" ")
        f.write("\n")

"""
Входные данные для файла maze-for-u.txt

INPUT:

0
1
212
605
599
798

OR

0
1
146
631
599
798

Входные данные для файла test_maze.txt

INPUT:

0
1
1
3
9
8
"""
