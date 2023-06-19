import turtle
import heapq

class Mob(turtle.Turtle):

    _algorithm = 'dijkstra'

    def __init__(self, target_turtle: turtle.Turtle, speed: int = 15):
        super().__init__()
        self.target_turtle = target_turtle
        self._speed = speed
        self.speed(self._speed)
        self.current_step = 0
        self.path = None

    def dijkstra(self, start_coord, target_coord):
        priority_queue = [(0, start_coord)]
        visited = set()
        distances = {start_coord: 0}
        path = {}

        while priority_queue:
            (distance, current) = heapq.heappop(priority_queue)

            if current == target_coord:
                break

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.get_neighbors(current):
                cost = self.get_cost(current, neighbor)
                new_distance = distances[current] + cost

                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
                    path[neighbor] = current

        if target_coord not in path:
            return None

        final_path = [target_coord]
        while target_coord != start_coord:
            target_coord = path[target_coord]
            final_path.append(target_coord)

        return final_path[::-1]

    def get_neighbors(self, coordinate):
        x, y = coordinate
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return neighbors

    def get_cost(self, current, neighbor):
        # modify according to cost function
        return 1

    def make_step(self):
        if self.position() == self.target_turtle.position():
            return

        position = tuple(map(int, self.position()))
        target_position = tuple(map(int, self.target_turtle.position()))
        self.path = self.dijkstra(position, target_position)[::self._speed]

        if self.current_step > len(self.path):
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1
        return self.heading()
