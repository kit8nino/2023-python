from math import sqrt
from queue import PriorityQueue

def ReadMaze(file):
    with open(file, "r") as f:
        lns = f.read().splitlines()
    maze = [list(line) for line in lns]
    return maze

def StartEnd(maze):
    start = None
    end = None
    for i in range(len(maze[0])):
        if maze[0][i]==" ":
            start = (0,i)
        if maze[len(maze)-1][i] == " ":
            end = (int(len(maze)-1),int(i))
    return start, end

def Key(maze):
    key=None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "*":
                key = (i,j)
    return key

def shag(maze, Cord):
    glb, dln = Cord
    neig = [(glb-1,dln),(glb,dln+1),(glb+1,dln),(glb,dln-1)]
    shagi = []
    for nei in neig:
        glb,dln = nei
        if 0<=glb<len(maze) and 0<=dln<len(maze[0]) and maze[glb][dln]!="#":
            shagi.append(nei)
    return shagi

def pathtoend(RM):
    path=[]
    start,end = StartEnd(RM)
    queue = [(start, [start])]
    visited=[]
    av = start
    while av != end:
        av, path = queue.pop(0)
        visited.append(av)
        for cells in shag(RM,av):
            if cells not in visited:
                queue.append((cells, path + [cells]))
    return path

def pathstartkey(RM):
    path=[]
    start,end = StartEnd(RM)
    end = Key(RM)
    queue = [(start, [start])]
    visited=[]
    av = start
    while av != end:
        av, path = queue.pop(0)
        visited.append(av)
        for cells in shag(RM,av):
            if cells not in visited:
                queue.append((cells, path + [cells]))
    return path

def pathfromkey(RM):
    pathkey=[]
    start = Key(RM)
    queue = [(start,[start])]
    visited=[]
    av = start
    while av not in pathtoend(RM):
        av, path = queue.pop(0)
        visited.append(av)
        for cells in shag(RM,av):
            if cells not in visited:
                queue.append((cells, path + [cells]))
    return path

def MakeFPath(pathtoend,pathfromkey):
    f = []
    s = pathfromkey[len(pathfromkey)-1]
    for i in pathtoend:
        if i == s:
            return f
        else:
            f.append(i)

def MakeSPath(MakeFPath, pathfromkey):
    s = pathfromkey[len(pathfromkey)-1]
    l = []
    path=[]
    for k in range(len(pathfromkey)-1,0,-1):
        l.append(pathfromkey[k])
    for i in MakeFPath:
        path.append(i)
    for i in l:
        path.append(i)
    print(path)

def heur(cell,end):
    return sqrt((cell[0]-end[0]) ** 2 + (cell[1]-end[1]) ** 2)

def star(RM, st, en):
    start = st
    end = en
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    visited = set()
    while not queue.empty():
        p, av, path = queue.get()
        if av == end:
            return p, path
        visited.add(av)
        for cells in shag(RM, av):
            if cells not in visited:
                path1 = path + [cells]
                pr = len(path1) + heur(cells, end)
                queue.put((pr, cells, path1))
    return None

def main():
    RM = ReadMaze("maze-for-u.txt")
    k = Key(RM)
    pathtokey = pathstartkey(RM)
    start, end = StartEnd(RM)
    PathToEnd = star(RM, Key(RM), end)

    for i in pathtokey:
        RM[i[0]][i[1]] = "."

    for i in star(RM, k, end)[1]:
        RM[i[0]][i[1]] = ","

    RM[k[0]][k[1]] = "*"

    result = ""
    for line in RM:
        result += "".join(line) + "\n"

    with open("maze-for-me-done.txt", "w") as f:
        f.write(result)
    print("смотрите файл")
main()