import math


class Maze:
    def __init__(self, filename, start, key, finish):
        self.maze = []
        self.start = start
        self.key = key
        self.finish = finish
        self.get_maze(filename)
        self.width = len(self.maze[0])
        self.height = len(self.maze)
        self.add_stuff()

    def print_maze(self):
        for row in self.maze:
            for element in row:
                if element == 0:
                    print('#', end='')
                elif element == 1:
                    print(' ', end='')
                elif element == 2:
                    print('A', end='')
                elif element == 3:
                    print('*', end='')
                elif element == 4:
                    print('E', end='')
                elif element == 5:
                    print('.', end='')
                elif element == 6:
                    print(',', end='')
                elif element == 7:
                    print(';', end='')
            print()
        print()

    def get_maze(self, filename):
        f = open(filename)
        data = f.readlines()
        self.maze = []
        for i, row in enumerate(data):
            self.maze.append([])
            for element in row:
                if element == '#':
                    self.maze[i].append(0)
                else:
                    self.maze[i].append(1)

    def check(self, dot):
        y, x = dot[0], dot[1]
        if y < 0 or x < 0 or y >= self.height or x >= self.width:
            return False
        return self.maze[y][x] > 0

    def set(self, dot, number):
        y, x = dot[0], dot[1]
        if not self.check(dot):
            return False
        if self.maze[y][x] == 5:
            self.maze[y][x] = 7
        else:
            self.maze[y][x] = number
        return True

    def add_stuff(self):
        flag = True
        if not self.set(self.start, 2):
            print("Игрок не выставлен - ячейка занята")
            flag = False
        if not self.set(self.key, 3):
            print("Ключ не выставлен - ячейка занята")
            flag = False
        if not self.set(self.finish, 4):
            print("Выход не выставлен - ячейка занята")
            flag = False
        if not flag:
            exit(0)

    def move(self, dot: tuple, direction=""):
        y, x = dot[0], dot[1]
        if direction == "up":
            y -= 1
        elif direction == "down":
            y += 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
        return y, x

    def create_path(self, start, finish, prev):
        current = finish
        path = []
        while current != start:
            current = prev[current]
            path.append(current)
        path.pop()
        path = path[::-1]
        return path

    def paint_path(self, path, number):
        for cell in path:
            self.set(cell, number)

    def width_search(self, start, finish, number):
        prev = {}
        viewed = [start]
        queue = [start]
        directions = ["up", "down", "left", "right"]
        while queue:
            current = queue.pop(0)
            for direction in directions:
                y, x = self.move(current, direction)
                if self.check((y, x)) and (y, x) not in viewed:
                    queue.append((y, x))
                    viewed.append((y, x))
                    prev[(y, x)] = current
                    if (y, x) == finish:
                        path = self.create_path(start, finish, prev)
                        self.paint_path(path, number)
                        return 0
        print("Не найден путь")
        exit(0)

    def choose_element(self, queue, finish):
        y_finish, x_finish = finish[0], finish[1]
        min_value = 1e10
        min_element = queue[0]
        for element in queue:
            cell, dist = element[0], element[1]
            y, x = cell[0], cell[1]
            value = math.sqrt((y - y_finish) ** 2 + (x - x_finish) ** 2) + dist
            if value < min_value:
                min_element = element
        queue.remove(min_element)
        return queue, min_element

    def a_star_search(self, start, finish, number):
        prev = {}
        viewed = [start]
        queue = [(start, 0)]
        directions = ["up", "down", "left", "right"]
        while queue:
            queue, element = self.choose_element(queue, finish)
            current, dist = element[0], element[1]
            for direction in directions:
                y, x = self.move(current, direction)
                if self.check((y, x)) and (y, x) not in viewed:
                    queue.append(((y, x), dist + 1))
                    viewed.append((y, x))
                    prev[(y, x)] = current
                    if (y, x) == finish:
                        path = self.create_path(start, finish, prev)
                        self.paint_path(path, number)
                        return 0
        print("Не найден путь")
        exit(0)

    def processing(self, method):
        self.print_maze()
        if method == "width":
            self.width_search(self.start, self.key, 5)
            self.width_search(self.key, self.finish, 6)
        else:
            self.a_star_search(self.start, self.key, 5)
            self.a_star_search(self.key, self.finish, 6)
        self.print_maze()


def main():
    maze = Maze("maze-for-u.txt", (0, 1), (107, 85), (199, 198))
    maze.processing("width")


if __name__ == "__main__":
    main()
