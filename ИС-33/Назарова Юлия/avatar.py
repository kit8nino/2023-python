import turtle
import math
from collections import deque
import heapq

class Avatar(turtle.Turtle):
    def __init__(self, target: tuple, speed: int = 10):
        super().__init__()
        self._speed = speed
        self.speed(speed)
        self.is_finish = False
        self.target = target
        self.path = None
        self.current_step = 0
        self.maze = open('maze-for-u.txt').read().split('\n')[:]
        
    
    def heuristic(self, point, goal):
        return abs(point[0] - goal[0]) + abs(point[1] - goal[1])
    
    def accessible_paths(self, coord, graph):
        accessible = []
        for neighbors in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_coord = (coord[0] + neighbors[0], coord[1] + neighbors[1])
            if 0 <= new_coord[0] < len(graph) and 0 <= new_coord[1] < len(graph[0]) and graph[new_coord[0]][new_coord[1]] != '#':
                accessible.append(new_coord)
        return accessible
    
    def a_star(self, start, end):
        open_set = [(0, start)]
        closed_set = set()
        came_from = {}
        gs = {start: 0}
        fs = {start: self.heuristic(start, end)}

        while open_set:
            current = heapq.heappop(open_set)[1]
            
            if current == end:
                path = [end]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return path[::-1]

            closed_set.add(current)

            for neighbor in self.accessible_paths(current, self.maze):
                tentative_gs = gs[current] + 1
                
                if neighbor in closed_set and tentative_gs >= gs.get(neighbor, float('inf')):
                    continue
                
                if tentative_gs < gs.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    gs[neighbor] = tentative_gs
                    fs[neighbor] = tentative_gs + self.heuristic(neighbor, end)
                    if neighbor not in closed_set:
                        heapq.heappush(open_set, (fs[neighbor], neighbor))

        return None
    
    def init_path(self):
        self.path = self.a_star((0, 1), self.target)[::self._speed]
        
    
    def make_step(self):
        if self.current_step == len(self.path):
            self.is_finish = True
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1
        return self.heading()