import turtle
import heapq

class Mob(turtle.Turtle):

    max_x, max_y = 101, 101
    _step_count = 0

    def __init__(self, x=0, y=0, name='Frog', speed=5):
        super().__init__()
        self.shape(name='turtle')
        self.x, self.y = x, y
        self.speed = speed
        self.name = name

    def set_coord(self, x, y):
        if x < self.max_x:
            self.x = x
        if y < self.max_y:
            self.y = y

    def step(self, direction='up'):
        if direction == 'up':
            self.y += self.speed
        if direction == 'down':
            self.y -= self.speed
        if direction == 'left':
            self.x -= self.speed
        if direction == 'right':
            self.x += self.speed
        self.move()
        return (self.x, self.y)

    def move(self):
        self._step_count += 1
        self.goto(self.x, self.y)

    def get_neighbors(self, current):
        x, y = current
        neighbors = []

        if x > 9:
            neighbors.append((x - self.speed, y))
        if x < 91:
            neighbors.append((x + self.speed, y))
        if y > 9:
            neighbors.append((x, y - self.speed))
        if y < 91:
            neighbors.append((x, y + self.speed))
            return neighbors

    def dijkstra(self, end):
        start = (self.x, self.y)

        if start == end:
            return None
        queue = []
        heapq.heappush(queue, (0, start))
        distances = {(x, y): float('inf') for x in range(100) for y in range(100)}
        distances[start] = 0
        previous = {(x, y): None for x in range(100) for y in range(100)}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous[current_node]
                path = path[::-1]

                if len(path) > 1:
                    next_node = path[1]
                    if next_node[0] > start[0]:
                        return 'right'
                    elif next_node[0] < start[0]:
                        return 'left'
                    elif next_node[1] < start[1]:
                        return 'down'
                    elif next_node[1] > start[1]:
                        return 'up'

            for neighbor in self.get_neighbors(current_node):
                new_distance = current_distance + 5

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node
                    heapq.heappush(queue, (new_distance, neighbor))

        return None
