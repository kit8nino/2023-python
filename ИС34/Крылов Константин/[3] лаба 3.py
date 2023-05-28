#функция для преобразования лабиринта
def readmaze(filename):
    with open(filename)as f:
        lines=f.read().splitlines()
    maze=[list(line)for line in lines]
    return maze

#поиск точек начала и конца
def points_start_end(maze):
    start = None
    end = None
    for y in range(len(maze[0])):
        if maze[0][y]==" ":
            start=(0,y)
        if maze[len(maze)-1][y]==" ":
            end=((len(maze)-1),y)
    return start,end

#Поиск ключа
def key_point(maze):
    key= None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]== "*":
                key = (i,j)
                break
    return key

#получение соседних точек
def get_neighbor(maze,point):
    row, col=point
    neighbors=[]
    if row > 0 and maze[row-1][col] !="#":
        neighbors.append((row-1,col))
    if row < len(maze)-1 and maze[row+1][col] != "#":
        neighbors.append((row+1,col))
    if col > 0 and maze[row][col-1] != "#":
        neighbors.append((row,col-1))
    if col < len(maze[0])-1 and maze[row][col+1] !="#":
        neighbors.append((row,col+1))
    return  neighbors

#Поиcк пути с помощью DFS
def DFS(maze,start,end):
    #создаем стек и добавляем наяальную точку в него
    stack=[start]
    #создаем словарь для оьслеживания посещенных точек
    visited={start:None}
    while stack:
        #извлекаем вершину из стека
        current=stack.pop()
        #если достигли конечной точки,то возвращаем путь
        if current==end:
            path=[]
            while current is not None:
                path.append(current)
                current=visited[current]
            return path[::-1]
        #добавляем в стек все соседние точки, которые еще не были посещены
        for neighbor in get_neighbor(maze,current):
            if neighbor not in visited:
                stack.append(neighbor)
                visited[neighbor]=current
    #если не нашли путь
    return  None
#объявление лабиранта с пометкой пути
def new_maze(maze,path,simvol):
    for coordinata in path:
        x,y=coordinata
        maze[x][y]=simvol
    return maze
#запись лабиринта в отдельный файл
def new_file(maze,filename):
    with open(filename,"w")as f:
        for row in maze:
            for elem in row:
                f.write(str(elem))
            f.write("\n")

maze=readmaze("maze-for-u.txt")
start,end=points_start_end(maze)
key=key_point(maze)
path1=DFS(maze,start,key)
path2=DFS(maze,key,end)
maze=new_maze(maze,path1,".")
maze=new_maze(maze,path2,",")
x,y=key
maze[x][y]="*"
new_file(maze,"maze-for-me-done.txt")
