import turtle
from collections import deque


class Mob(turtle.Turtle):
    
    def __init__(self, target: tuple, speed: int = 15):
        super().__init__()
        self.target = target
        self._speed = speed
        self.is_finish = False
        self.speed(self._speed)
        self.current_step = 0
        self.path = None
        self.maze = open('maze-for-u.txt').read().split('\n')[:]
        
    def dfs(self, maze, start, target):
        #stack будет хранить итоговый путь
        stack=[]
        visited = set()#список посещенных координат
        current = (start[0], start[1])
        visited.add(current)
        
        while current!=target:
            
            row, col = current
            #Список всех возможных соседей
            neighbors = [
                (row - 1, col), (row + 1, col),
                (row, col - 1), (row, col + 1)
            ]
            #Проверка имеет ли текущая клетка свободных, непосещенных соседей
            if (neighbors[0] not in visited) and 0 <= neighbors[0][0] < len(maze) and 0 <= neighbors[0][1] < len(maze[0]) and maze[neighbors[0][0]][neighbors[0][1]]!='#':
                stack.append(current)
                current=neighbors[0]
                visited.add(current)
                
            elif (neighbors[3] not in visited) and 0 <= neighbors[3][0] < len(maze) and 0 <= neighbors[3][1] < len(maze[0]) and maze[neighbors[3][0]][neighbors[3][1]]!='#':
                stack.append(current)
                current=neighbors[3]
                visited.add(current)
                
            elif (neighbors[1] not in visited) and 0 <= neighbors[1][0] < len(maze) and 0 <= neighbors[1][1] < len(maze[0]) and maze[neighbors[1][0]][neighbors[1][1]]!='#':
                stack.append(current)
                current=neighbors[1]
                visited.add(current)

            elif (neighbors[2] not in visited) and 0 <= neighbors[2][0] < len(maze) and 0 <= neighbors[2][1] < len(maze[0]) and maze[neighbors[2][0]][neighbors[2][1]]!='#':
                stack.append(current)
                current=neighbors[2]
                visited.add(current)
            
            elif stack:
                current=stack.pop()
            else:
                return False
            
        stack.append(current)
        return stack
    
    def init_path(self):
        self.path = self.dfs(self.maze, (0, 1), self.target)[::self._speed]
        
    
    def make_step(self):
        if self.current_step == len(self.path):
            self.is_finish=True
            return

        self.goto(self.path[self.current_step][0], self.path[self.current_step][1])
        self.current_step += 1
        return self.heading()