class Point_A_star:
    def __init__(self, y, x, end_point=None, prev_point=None):
        self.x = x
        self.y = y
        self.g = prev_point.g + 1 if prev_point != None else 0
        # От начальной точки до текущей точки
        self.h = abs(end_point.x - self.x) + abs(end_point.y - self.y) if end_point != None else 0
        # ерет.. эврик.. еврейская функция короче
        self.prev_point = prev_point
        # Папа

def A_star(maze, start, end):
    if maze[start.y][start.x] == '#' or maze[end.y][end.x] == '#':
        return "Тайлер дерден?"
    if (start.y, start.x) == (end.y, end.x):
        return [(start.y, start.x)]
    # ну типа бывалые
    points_set = [start]
    
    # пока здесь кто нибудь есть
    while points_set:
        cur = min(points_set, key=lambda x: x.g+x.h)
        # Выбор точки с наименьшей оценкой f(x) = g(x) + h(x)
        points_set.remove(cur)
        # Пакета
        
        if (cur.y, cur.x) == (end.y, end.x):
            # Если текущая точка является конечной точкой
            path = []
            while cur != None:
                # Восстановление пути
                path.append((cur.y, cur.x))
                cur = cur.prev_point
            # т.к. попа впереди то
            return path[::-1]
        
        pos = [Point_A_star(y, x, end, cur) for y, x in [(cur.y+1,cur.x),(cur.y-1,cur.x),(cur.y,cur.x+1),(cur.y,cur.x-1)] \
         if 0<=y<len(maze) and 0<=x<len(maze[0]) and maze[y][x]!='#']
        # Соседние точки в пределах рамок приличия
        for new_point in pos:
            old_point = next((point for point in points_set if (point.y,point.x) == (new_point.y,new_point.x)), None)
            # Пытемся понять была ли эта точка до new_point
            if old_point != None:
                # Если была, то надо бы объективно понять, действительно ли раньше было лучше
                if new_point.g < old_point.g:
                    # Сравнение путей от начала говорит о том что раньше лучше не было (((
                    old_point.g = new_point.g
                    old_point.prev_point = new_point.prev_point
                    # Добавим свежести
            else:
                points_set.append(new_point)
                # Или же это не хорошо забытое старое, а что то новое
    # Тайлер дерден?
    return "Тайлер дерден?"
