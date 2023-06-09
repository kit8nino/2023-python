import heapq

def input_coord(max_x, max_y, tip):
    while True:
        while True:
            try:
                if tip==1:
                    coord_x = int(input(f"Введите x координату АВАТАРА, x < {max_x}:"))
                elif tip==2 :
                    coord_x = int(input(f"Введите x координату ВЫХОДА, x < {max_x}:"))
                else:
                    coord_x = int(input(f"Введите x координату КЛЮЧА, x < {max_x}:")) 
                if coord_x>=max_x:
                    print("Warning!Out of range")
                else:
                    break;   
            except ValueError:
                print("Ошибка!Введите число.")
        
        while True:
            try:
                if tip==1:
                    coord_y = int(input(f"Введите y координату АВАТАРА, y < {max_y}:"))
                elif tip==2 :
                    coord_y = int(input(f"Введите y координату ВЫХОДА, y < {max_y}:"))
                else:
                    coord_y = int(input(f"Введите y координату КЛЮЧА, y < {max_y}:"))
                if coord_y>=max_y:
                    print("Warning!Out of range")
                else:
                    break;
            except ValueError:
                print("Ошибка!Введите число.")
                
        if (init_maze[coord_y][coord_x] == ' '):
            return coord_y, coord_x
        else:
            print("Это координаты стены!");
            
def dfs(maze, start, target, stack):
    #stack будет хранить итоговый путь
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
        if (neighbors[0] not in visited) and 0 <= neighbors[0][0] < len(maze) and 0 <= neighbors[0][1] < len(maze[0]) and maze[neighbors[0][0]][neighbors[0][1]]!=1:
            stack.append(current)
            current=neighbors[0]
            visited.add(current)
            
        elif (neighbors[3] not in visited) and 0 <= neighbors[3][0] < len(maze) and 0 <= neighbors[3][1] < len(maze[0]) and maze[neighbors[3][0]][neighbors[3][1]]!=1:
            stack.append(current)
            current=neighbors[3]
            visited.add(current)
            
        elif (neighbors[1] not in visited) and 0 <= neighbors[1][0] < len(maze) and 0 <= neighbors[1][1] < len(maze[0]) and maze[neighbors[1][0]][neighbors[1][1]]!=1:
            stack.append(current)
            current=neighbors[1]
            visited.add(current)

        elif (neighbors[2] not in visited) and 0 <= neighbors[2][0] < len(maze) and 0 <= neighbors[2][1] < len(maze[0]) and maze[neighbors[2][0]][neighbors[2][1]]!=1:
            stack.append(current)
            current=neighbors[2]
            visited.add(current)
        
        elif stack:
            current=stack.pop()
        else:
            return False
        
    stack.append(current)
    return True

def heuristic(point, goal):
        return abs(point[0] - goal[0]) + abs(point[1] - goal[1])
    
def accessible_paths(coord, graph):
        accessible = []
        for neighbors in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_coord = (coord[0] + neighbors[0], coord[1] + neighbors[1])
            if 0 <= new_coord[0] < len(graph) and 0 <= new_coord[1] < len(graph[0]) and graph[new_coord[0]][new_coord[1]] != '#':
                accessible.append(new_coord)
        return accessible
    
def a_star(maze, start, end):
    open_set = [(0, start)]
    closed_set = set()
    came_from = {}
    gs = {start: 0}
    fs = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        closed_set.add(current)

        for neighbor in accessible_paths(current, maze):
            tentative_gs = gs[current] + 1
            
            if neighbor in closed_set and tentative_gs >= gs.get(neighbor, float('inf')):
                continue
            
            if tentative_gs < gs.get(neighbor, float('inf')):
                came_from[neighbor] = current
                gs[neighbor] = tentative_gs
                fs[neighbor] = tentative_gs + heuristic(neighbor, end)
                if neighbor not in closed_set:
                    heapq.heappush(open_set, (fs[neighbor], neighbor))

    return None

def completed_maze(graph, size_w, size_h):
    for i in range(size_h):
        for j in range(size_w):
            if graph[i][j]==1:
                graph[i][j]='#'
                
            elif graph[i][j]==0:
                graph[i][j]=' '
                
            elif graph[i][j]==3:
                graph[i][j]='.'
                
            elif graph[i][j]==4:
                graph[i][j]=','
                
        graph[i][size_w-1]+='\n'
        
def create_blank_template(template, size_w, size_h):
    for i in range(size_h):
        template.append([])
        for j in range(size_w):
            template[-1].append(0)
 

#main
file_name='maze-for-u.txt'
init_maze = open(file_name).read().split('\n')[:]
height = len(init_maze)
width = len(init_maze[0])
print("Высота лабиринта", height)
print("Ширина лабиринт", width)

start = input_coord(width, height, 1)
end = input_coord(width, height, 2)
key = input_coord(width, height, 3)

labirint_graph = []
create_blank_template(labirint_graph, width, height)        
for i in range(height):
    for j in range(width):
        if init_maze[i][j] == '#':
            labirint_graph[i][j]=1;
            
key_coordpath=[]
dfs(labirint_graph, start, key, key_coordpath)

for i in range(len(key_coordpath)):
    x=key_coordpath[i][1]
    y=key_coordpath[i][0]
    labirint_graph[y][x]= 3
    
#Ищем оптимальный путь от ключа до выхода с помощью алгоритма A*
end_coordpath=[]
end_coordpath=a_star(init_maze, key, end)

for i in range(len(end_coordpath)):
    x=end_coordpath[i][1]
    y=end_coordpath[i][0]
    labirint_graph[y][x]= 4
#отрисовываем лабиринт с нашим проходом в изначальном виде
labirint_graph[key[0]][key[1]]= '*'#ставим на график *-ключ
completed_maze(labirint_graph, width, height)

#Преобразуем граф из массива символов в массив строк для печати в txt файл
new_maze_string=''
result_graph=[]
for i in range(height):
    for j in range(width):
        new_maze_string+=labirint_graph[i][j]

    result_graph.append(new_maze_string)
    new_maze_string=''

#Печатаем пройденный граф в файл 
with open('maze_result.txt', 'w') as file2:
    file2.writelines(result_graph)
print("Итоговый путь лежит в файле: maze_result.txt")
