import math
import turtle

class Avatar(turtle.Turtle):
    def __init__(self, target: tuple, speed=10):
        super().__init__()
        self.speed(speed)
        self.is_finish = False
        self.target = target
        self.path = None
        self.current_step = 0

    def heuristic_for_astar(self, coord):
        target_x, target_y = self.target
        x, y = coord
        distance = math.sqrt((target_x - x) ** 2 + (target_y - y) ** 2)
        return distance

    def astar(self, start, goal):
        open_set = []
        closed_set = set()
        path_scores = {start: 0}
        estimated_scores = {start: self.heuristic_for_astar(start)}
        current = start

        while current != goal:
            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue
                tentative_path_score = path_scores[current] + self.get_cost(current, neighbor)
                if neighbor not in path_scores or tentative_path_score < path_scores[neighbor]:
                    path_scores[neighbor] = tentative_path_score
                    estimated_score = tentative_path_score + self.heuristic_for_astar(neighbor)
                    estimated_scores[neighbor] = estimated_score
                    neighbor_data = [estimated_score, neighbor]
                    found_flag = False
                    for idx, item in enumerate(open_set):
                        if estimated_score < item[0]:
                            open_set.insert(idx, neighbor_data)
                            found_flag = True
                            break
                    if not found_flag:
                        open_set.append(neighbor_data)

            closed_set.add(current)
            if not open_set:
                return None
            current = open_set.pop(0)[1]
        path = [current]
        while current != start:
            current = min(
                [neighbor for neighbor in self.get_neighbors(current) if neighbor in path_scores],
                key=lambda neighbor: path_scores[neighbor]
            )
            path.insert(0, current)
        return path

    def get_neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 5, y), (x + 1, y), (x, y - 5), (x, y + 1)]
        return neighbors

    def get_cost(self, current, neighbor):
        return 1

    def init_path(self):
        self.path = self.astar((0, 0), self.target)
    def step(self):
        if self.current_step == len(self.path):
            self.is_finish = True
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1

        return self.heading()
