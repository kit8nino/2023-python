from collections import deque

class Point_bfs:
    def __init__(self, y, x, prev_point=None):
        self.x = x
        self.y = y
        self.prev_point = prev_point

def bfs(maze, start, end):
    if maze[start.y][start.x] == '#' or maze[end.y][end.x] == '#':
        return "Тайлер дерден?"
    if (start.y, start.x) == (end.y, end.x):
        return [(start.y, start.x)]
    # очередь точек типа
    queue = deque([start])
    # бывалые...
    visited = [start]

    # пока здесь кто нибудь есть
    while queue:
        # буквально украл
        cur = queue.popleft()

        # ееее
        if (cur.y, cur.x) == (end.y, end.x):
            path = []
            while cur != None:
                path.append((cur.y, cur.x))
                cur = cur.prev_point
                # попой вперед как и в прошлый раз
            return path[::-1]
        
        # рамки приличия
        pos = [Point_bfs(y, x, cur) for y, x in [(cur.y+1,cur.x),(cur.y-1,cur.x),(cur.y,cur.x+1),(cur.y,cur.x-1)] \
         if 0<=y<len(maze) and 0<=x<len(maze[0]) and maze[y][x]!='#']
        for new_point in pos:
            # Впервые здесь?
            if not any((point.y,point.x) == (new_point.y,new_point.x) for point in visited):
                # добавляем клетку в очередь и отмечаем ее как бывалую
                queue.append(new_point)
                visited.append(new_point)
    # Опять?
    return "Тайлер дерден?"
