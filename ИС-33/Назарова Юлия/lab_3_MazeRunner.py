import heapq
def heuristic(point, goal):
        return abs(point[0] - goal[0]) + abs(point[1] - goal[1])
    
def available_paths(position, grid):
        available = []
        for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_position = (position[0] + delta[0], position[1] + delta[1])
            if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]) and grid[new_position[0]][new_position[1]] != '#':
                available.append(new_position)
        return available
    
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

        for neighbor in available_paths(current, maze):
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

def dfs(maze, start, target, stack):
    #stack будет хранить итоговый путь
    #так же с каждым шагом увеличивая или уменьшая k будем заполнять dfs_graph номерами всевозможных шагов из каждой текущей клетки
    #По итогу в dfs_graph будут все возможные обходы произведенные алгоритмом dfs
    visited = set()#список посещенных координат
    k=1
    current = (start[0], start[1])
    visited.add(current)
    dfs_graph[current[0]][current[1]]=k
    
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
            k+=1
            dfs_graph[current[0]][current[1]]=k
            
        elif (neighbors[3] not in visited) and 0 <= neighbors[3][0] < len(maze) and 0 <= neighbors[3][1] < len(maze[0]) and maze[neighbors[3][0]][neighbors[3][1]]!=1:
            stack.append(current)
            current=neighbors[3]
            visited.add(current)
            k+=1
            dfs_graph[current[0]][current[1]]=k
            
        elif (neighbors[1] not in visited) and 0 <= neighbors[1][0] < len(maze) and 0 <= neighbors[1][1] < len(maze[0]) and maze[neighbors[1][0]][neighbors[1][1]]!=1:
            stack.append(current)
            current=neighbors[1]
            visited.add(current)
            k+=1
            dfs_graph[current[0]][current[1]]=k
        elif (neighbors[2] not in visited) and 0 <= neighbors[2][0] < len(maze) and 0 <= neighbors[2][1] < len(maze[0]) and maze[neighbors[2][0]][neighbors[2][1]]!=1:
            stack.append(current)
            current=neighbors[2]
            visited.add(current)
            k+=1
            dfs_graph[current[0]][current[1]]=k
        
        elif stack:
            current=stack.pop()
            k-=1
        else:
            return False
        
    stack.append(current)
    return True

        
def create_temple(temple, size_w, size_h):
    for i in range(size_h):
        temple.append([])
        for j in range(size_w):
            temple[-1].append(0)

def crawl_graph(graph, size_w, size_h):
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
                
        maze_graph[i][size_w-1]+='\n'
 
def get_coord(max_x, max_y, style):
    while True:
        while True:
            try:
                if style==1:
                    coord_y = int(input(f"Enter y coordinate of AVATAR coord, y < {max_y}:"))
                elif style==2 :
                    coord_y = int(input(f"Enter y coordinate of EXIT coord, y < {max_y}:"))
                else:
                    coord_y = int(input(f"Enter y coordinate of KEY coord, y < {max_y}:"))
                if coord_y>=max_y:
                    print("Out of range")
                else:
                    break;
            except ValueError:
                print("Enter number")
        while True:
            try:
                if style==1:
                    coord_x = int(input(f"Enter x coordinate of Avatar coord, x < {max_x}:"))
                elif style==2 :
                    coord_x = int(input(f"Enter x coordinate of EXIT coord, x < {max_x}:"))
                else:
                    coord_x = int(input(f"Enter x coordinate of KEY coord, x < {max_x}:")) 
                if coord_x>=max_x:
                    print("Out of range")
                else:
                    break;   
            except ValueError:
                print("Enter a number")
        if (maze_raw[coord_y][coord_x] == ' '):
            return coord_y, coord_x
        else:
            print("Those are coordinates of a wall");


file_name='maze-for-u.txt'
maze_raw = open(file_name).read().split('\n')[:]
height = len(maze_raw)
width = len(maze_raw[0])
print("Height of Maze", height)
print("Width of Maze", width)

start = get_coord(width, height, 1)
end = get_coord(width, height, 2)
key = get_coord(width, height, 3)

maze_graph = []
create_temple(maze_graph, width, height)        
for i in range(height):
    for j in range(width):
        if maze_raw[i][j] == '#':
            maze_graph[i][j]=1;
#Ищем любой путь от старта до ключа с помощью алгоритма dfs(поиск в глубину)
coord_path_key=[]
dfs_graph=[]
create_temple(dfs_graph, width, height)

dfs(maze_graph, start, key, coord_path_key)

for i in range(len(coord_path_key)):
    x=coord_path_key[i][1]
    y=coord_path_key[i][0]
    maze_graph[y][x]= 3
    
#Ищем оптимальный путь от ключа до выхода с помощью алгоритма A*
coord_path_end=[]
coord_path_end=a_star(maze_raw, key, end)

for i in range(len(coord_path_end)):
    x=coord_path_end[i][1]
    y=coord_path_end[i][0]
    maze_graph[y][x]= 4
#отрисовываем лабиринт с нашим проходом в изначальном виде
maze_graph[key[0]][key[1]]= '*'#ставим на график *-ключ
crawl_graph(maze_graph, width, height)

#Преобразуем граф из массива символов в массив строк для печати в txt файл
string_row=''
result_path_graph=[]
for i in range(height):
    for j in range(width):
        string_row+=maze_graph[i][j]

    result_path_graph.append(string_row)
    string_row=''
#Печатаем пройденный граф в файл 
with open('maze_path_result.txt', 'w') as file2:
    file2.writelines(result_path_graph)
print("End of the algorithm!\nSee the result in the file: maze_path_result.txt")