import heapq

def read_maze(filename):
    with open(filename) as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze

def get_coord_key(size_w, size_h, maze):
    while True:
        while True:
            try:
                x = int(input(f"Введите x координату КЛЮЧА, x < {size_w}:"))
                if x>=size_w:
                    print("Вы вышли за пределы!")
                else:
                    break
            except ValueError:
                print("Вы ввели неверное значение!Введите число.")
            
        while True:
            try:
                y = int(input(f"Введите y координату КЛЮЧА, y < {size_h}:"))
                if y>=size_h:
                    print("Вы вышли за пределы!")
                else:
                    break
            except ValueError:
                print("Вы ввели неверное значение!Введите число.")
            
        if maze[y][x]==' ':
            return y, x
        else:
            print("Это координаты стены.")

def dfs(maze, start, target):
    coord_path=[]# хранит итоговый путь
    visited = set()#список посещенных координат
    current = (start[0], start[1])#текущая позиция
    visited.add(current)
    
    while current!=target:
        row, col = current
        #Список всех возможных соседей
        neighbors = [
            (row - 1, col), (row + 1, col),
            (row, col - 1), (row, col + 1)]

        dead_end=0
        for neighbor in neighbors:
            if (neighbor not in visited) and (0 <= neighbor[0] < len(maze)) and ((0 <= neighbor[1] < len(maze[0])) and maze[neighbor[0]][neighbor[1]] != '#'):
                coord_path.append(current)
                current=neighbor
                visited.add(current)
                dead_end+=1
                
        if dead_end==0:
            current=coord_path.pop()#зашли в тупик
                       
    coord_path.append(current)
    return coord_path

def heuristic(cur, finish):
        return abs(cur[0] - finish[0]) + abs(cur[1] - finish[1])

def neighbors_available(coord, graph):
        available = []
        neighbors = [
            (0, 1), (1, 0),
            (0, - 1), (-1, 0)]
        
        for neighbor in neighbors:
            new_coord = (coord[0] + neighbor[0], coord[1] + neighbor[1])
            if 0 <= new_coord[0] < len(graph) and 0 <= new_coord[1] < len(graph[0]) and graph[new_coord[0]][new_coord[1]] != '#':
                available.append(new_coord)
        return available
    
def a_star(maze, start, end):
    open_set = [(0, start)]
    visited = set()
    result_path = {}
    distance = {start: 0}
    previous = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == end:
            path = [end]
            while current in result_path:
                current = result_path[current]
                path.append(current)
            return path[::-1]

        visited.add(current)

        for neighbor in neighbors_available(current, maze):
            tentative_distance = distance[current] + 1
            
            if neighbor in visited and tentative_distance >= distance.get(neighbor, float('inf')):
                continue
            
            if tentative_distance < distance.get(neighbor, float('inf')):
                result_path[neighbor] = current
                distance[neighbor] = tentative_distance
                previous[neighbor] = tentative_distance + heuristic(neighbor, end)
                if neighbor not in visited:
                    heapq.heappush(open_set, (previous[neighbor], neighbor))

    return None

def main():
    file_name='maze-for-u.txt'
    init_maze = read_maze(file_name)

    start = (0, 1)
    end = (len(init_maze)-1, len(init_maze[0])-2)
    key = get_coord_key(len(init_maze[0]), len(init_maze), init_maze)

    key_path=dfs(init_maze, start, key)
    end_path=a_star(init_maze, key, end)
    
    for coord in key_path:
        init_maze[coord[0]][coord[1]]='.'
        
    for coord2 in end_path:
        init_maze[coord2[0]][coord2[1]]=','
        
    init_maze[key[0]][key[1]]='*'  
    result_maze=[]
    for line in init_maze:
        result_line=""
        for symbol in line:
            result_line+=symbol
        result_line+='\n'
        result_maze.append(result_line)
            
    with open('maze-for-me-done.txt', 'w') as file2:
        file2.writelines(result_maze)
        print("Лабиринт пройден успешно!Итоговый путь лежит в файле: maze-for-me-done.txt")
main()