#функция для преобразования лабиринта
def readmaze(file_name):
    with open(file_name) as f:
        maze = [list(line.strip()) for line in f]#создаем список который содержит строки текстового файла
    return maze

#поиск точек начало и конца
def tochky_start_end(maze):
    start = (0, maze[0].index(" "))            #Ищем вход в первой линии
    end = (len(maze)-1, maze[-1].index(" "))   #Ищем выход в последней
    return start, end

#поиск ключа
def key_tochka(maze):
    for i, g in enumerate(maze): #мы ищем координаты ключа(i,g.index("*"))
        if "*" in g:
            print(i,g.index("*"))
            return(i, g.index("*"))

#Жадный алгоритм для поиска пути в лабиринте
def Gadniy_algoritm(maze, start, end):
    #Создаем список соседних клеток
    neighbors=[(0,1),(0,-1),(1,0),(-1,0)]
    #Создаем список посещенных клеток
    visited=set()
    #создадим очередь для хранения пути
    queue = [[start]]
    #пока очередь не пуста
    while queue:
        path = queue.pop(0) #достаем 1 путь из очереди
        current = path[-1] #берем последнюю точку пути
        if current not in visited:
            visited.add(current)
            for neighbor in neighbors:  #для каждого соседа текущей точки
                #находим координаты точки
                x = current[0] + neighbor[0]
                y = current[1] + neighbor[1]
                if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "#":#Если сосед находится в пределах лабиринта и не стена
                    new_path = path+[(x,y)] #создаем новый путь до соседа
                    # если сосед равен конечной точку то возвращаем путь
                    if(x, y) == end:
                        return new_path
                    else:  # иначе добавляем новый путь в очередь
                        queue.append(new_path)
    return[]# Если не удалось найти путь до конечной точки, возвращаем пустой список
def new_maze(maze, path, mark): #обьявляем лабиринт и помечаем путь
    for cord in path:
        x, y = cord
        maze[x][y] = mark
    return maze
def new_file(maze, file_name): #запись лабиринта в отдельный файл
    with open(file_name, "w") as f:
        for g in maze:
            f.write("".join(g)+"\n")

maze = readmaze("maze-for-u.txt")
start, end = tochky_start_end(maze)
key = key_tochka(maze)
path1 = Gadniy_algoritm(maze, start, key)
path2 = Gadniy_algoritm(maze, key, end)
maze = new_maze(maze, path1, ".")
maze = new_maze(maze, path2, ",")
x, y = key
maze[x][y] = "*"
new_file(maze, "maze-for-me-done.txt")
