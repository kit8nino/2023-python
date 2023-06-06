from turtle import Turtle


class Avatar(Turtle):
    def __init__(self, coords, speed, color, maze, target):
        super().__init__()
        self.penup()
        self.__pos = coords
        self.goto(coords[1] * 3 - 50, - coords[0] * 3 + 50)
        self.speed(speed)
        self.shape('square')
        self.color(color)
        self.shapesize(2 / 20)
        self.path = self.astar(maze, self.__pos, target)
        self.step = 1

    def getPos(self):
        return self.__pos
    def make_move(self):
        self.goto(self.path[self.step][1] * 3 - 50, -self.path[self.step][0] * 3 + 50)
        self.__pos = self.path[self.step]
        self.step += 1
    def astar(self, maze, start, end):
        path = []
        distances = {start: 0}
        previous = {}
        to_visit = [start]
        while to_visit:
            current = to_visit.pop(0)
            if current == end:
                break
            neighbors = self.get_neighbors(maze, current)
            
            for neighbor in neighbors:
                distance = distances[current] + 1
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    to_visit.append(neighbor)
                    to_visit.sort(key = lambda x: distances[x] + self.heuristic(x, end))
                    
        if end in previous:
            current = end
            while current != start:
                path.insert(0, current)
                current = previous[current]
            path.insert(0, start)
        return path

    def heuristic(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    def get_neighbors(self, maze, pos):
        row, col = pos
        candidates = [(row - 1, col),
                      (row + 1, col),
                      (row, col - 1),
                      (row, col + 1)]
        
        result = []
        for r, c in candidates:
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == "0":
                result.append((r, c))

        return result
