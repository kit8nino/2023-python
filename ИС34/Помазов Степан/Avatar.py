import turtle
import heapq
import math

class Avatar(turtle.Turtle):
    def __init__(self, target: tuple, speed: int = 15):
        super().__init__()
        self.speed(speed)
        self.is_finish = False
        self.target = target
        self.path = None
        self.current_step = 0

    def calculate_heuristic(self, coord):
        target_x, target_y = self.target
        x, y = coord
        distance = math.sqrt((target_x - x) ** 2 + (target_y - y) ** 2)
        return distance

    def dijkstra(self, start, target):
        pq = [(0, start)]
        visited = set()
        distances = {start: 0}
        path = {}

        while pq:
            (dist, current) = heapq.heappop(pq)

            if current == target:
                break

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.get_neighbors(current):
                cost = self.calculate_cost(current, neighbor)
                new_distance = distances[current] + cost

                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
                    path[neighbor] = current

        if target not in path:
            return None

        final_path = [target]
        while target != start:
            target = path[target]
            final_path.append(target)

        return final_path[::-1]

    def get_neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return neighbors

    def calculate_cost(self, current, neighbor):
        # modify according to the cost function
        return 1

    def initialize_path(self):
        self.path = self.dijkstra((0, 0), self.target)

    def take_step(self):
        if self.current_step >= len(self.path):
            self.is_finish = True
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1

"""import turtle


class Avatar(turtle.Turtle):
    _algorythm = 'a_star'

    name = 'Noname'
    max_x, max_y = 100, 100
    _step_count = 0

    def __init__(self, name='Noname', x=0, y=0, target=(10, 10), speed=5, coord = (1,1)):
        self.x, self.y = x, y
        self.x0, self.y0 = x, y
        self.name = name
        self.target = target
        self.shape(name='arrow')
        self.penup()
        self.coord = list((x,y))
        self.goto(coord)
        self.speed = speed
        self.finish = (50,100)
        print(f'Avatar {self.name} created at ({self.x}, {self.y})')

    class Avatar(turtle.Turtle):
        def __init__(self, speed):
            super().__init__(speed)
            self.target = (50,100)

        def move(self):
            if self.target is None:
                return

            # Получение текущих координат аватара
            current_position = self.get_current_position()

            # Вызов алгоритма A* для поиска пути к целевой точке
            path = self.astar(current_position, self.target)

            if path:
                # Выбор следующей позиции из найденного пути
                next_position = path[1]  # Пропускаем текущую позицию

                # Вычисление направления движения
                diff_x = next_position[0] - current_position[0]
                diff_y = next_position[1] - current_position[1]

                if diff_x > 0:
                    direction = "right"
                elif diff_x < 0:
                    direction = "left"
                elif diff_y > 0:
                    direction = "up"
                else:
                    direction = "down"

                # Перемещение аватара на величину его скорости
                if direction == "right":
                    self.move_right()
                elif direction == "left":
                    self.move_left()
                elif direction == "up":
                    self.move_up()
                elif direction == "down":
                    self.move_down()

        def astar(self, start, target):
            open_set = set([start])
            came_from = {}  # предыдущая точка
            g_score = {start: 0}
            f_score = {start: heuristic_cost(start, end)}

            while open_set:
                current = min(open_set, key=lambda x: f_score[x])
                if current == target:
                    path = [current]
                    while current in came_from:
                        current = came_from[current]
                        path.append(current)
                    path.reverse()
                    return path
                open_set.remove(current)
                for neighbor in get_neighbors(current, maze):
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic_cost(neighbor, end)
                        if neighbor not in open_set:
                            open_set.add(neighbor)
            return None
        # Реализация алгоритма A* для поиска пути от start до target
        # ...

        def get_current_position(self):

        # Возвращает текущие координаты аватара
        # ...

        def move_right(self):

        # Перемещение аватара вправо на величину его скорости
        # ...

        def move_left(self):

        # Перемещение аватара влево на величину его скорости
        # ...

        def move_up(self):

        # Перемещение аватара вверх на величину его скорости
        # ...

        def move_down(self):
    # Перемещение аватара вниз на величину его скорости
    # ...

"""