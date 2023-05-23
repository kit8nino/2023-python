def add_path(maze, path1, path2):
    if path1 != "Тайлер дерден?" and path2 != "Тайлер дерден?":
        for y,x in path1:
            maze[y][x]='.'
        for y,x in path2:
            maze[y][x]=','
        with open('maze-for-me-done.txt', 'w') as f:
            for line in maze:
                f.write("".join(line) + "\n")
    else: print('Это Тайлер')


with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]

from BFS import bfs, Point_bfs
from A_star import A_star, Point_A_star

# start, key, end
for x in range(len(maze[0])):
    if maze[0][x]==' ': start = (0,x)
for x in range(len(maze[-1])):
    if maze[-1][x]==' ': end = (len(maze)-1, x)
y = len(maze)//2; x = len(maze[0])//3
while maze[y][x]!=' ': x+=1; y+=1
# отметить звездочкой обязательно
maze[y][x]='*'
key = (y,x)

path1 = bfs(maze, Point_bfs(*start), Point_bfs(*key))[:-1]
path2 = A_star(maze, Point_A_star(*key), Point_A_star(*end))[1:]

add_path(maze, path1, path2)
print("finally")
