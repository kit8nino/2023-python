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
        return 1

    def initialize_path(self):
        self.path = self.dijkstra((0, 0), self.target)

    def take_step(self):
        if self.current_step >= len(self.path):
            self.is_finish = True
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1
