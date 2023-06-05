import heapq
def read_maze(file):
    with open(file, 'r') as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze

# Поиск координат стартовой точки, ключа и выхода

def find_coordinates(maze):
    start = (0, maze[0].index(' '))
    key = None
    exit = (len(maze)-1, maze[len(maze)-1].index(' '))
    for row in range(len(maze)):
        if '*' in maze[row]:
            key = (row, maze[row].index('*'))
            break
    return start, key, exit

#Эвристическая стоимость

def heuristic_cost(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

# Жадный алгоритм поиска пути до ключа
# он отображает посещения всех точек, в которых побывал аватар в поисках ключа

def greedy_algorithm(maze, start, end):
    pq = []
    visited = set()
    heapq.heappush(pq, (0, start))
    while pq:
        current_cost, current_pos = heapq.heappop(pq)
        if current_pos == end:
            break
        if current_pos in visited:
            continue
        visited.add(current_pos)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            x, y = current_pos[0] + dx, current_pos[1] + dy
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                priority = heuristic_cost(end, (x, y))
                heapq.heappush(pq, (priority, (x, y)))
    return visited

#А_star алгоритм поиска кратчайшего пути
#оцениваем стоимость вариантов путей

def a_star(maze, start, end):
    open_set = set([start])
    came_from = {} #предыдущая точка
    g_score = {start: 0}
    f_score = {start: heuristic_cost(start, end)}

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end:
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

#Функция для определения соседних точек, относительно текущей

def get_neighbors(coord, maze):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    neighbors = []
    for dx, dy in directions: #dx,dy - дельта направления
        x, y = coord[0] + dx, coord[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
            if maze[x][y] != "#":
                neighbors.append((x, y))
    return neighbors

#Функции для перевода путей в символы и записи в новый файл

def write_maze_greedy(maze, path, key):
    for pos in path:
        maze[pos[0]][pos[1]] = '.'
    maze[key[0]][key[1]] = '*'
    with open('maze-for-me-done.txt', 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

def write_maze_astar(maze, path, key):
    for pos in path:
        maze[pos[0]][pos[1]] = ','
    maze[key[0]][key[1]] = '*'
    with open('maze-for-me-done.txt', 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')

#Основной код:

#Считываем лабиринт в массив

maze = read_maze('maze-for-u2.txt')

#Находим координаты (x,y) для Точки старта, Точки финиша и Точки ключа

start, key, exit = find_coordinates(maze)

print(start,key,exit)

#Находим путь до ключа с помощью Жадного алгоритма

path1 = greedy_algorithm(maze,start,key)

#Находим путь от ключа до выхода с помощью A*

path2 = a_star(maze,key,exit)

#Записываем пути в новый текстовый документ "maze-for-me-done.txt" (создается автоматически)

write_maze_greedy(maze,path1,key)
write_maze_astar(maze,path2,key)
