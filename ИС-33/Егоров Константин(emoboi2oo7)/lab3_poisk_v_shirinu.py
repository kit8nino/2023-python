def read_maze(filename):
    """
    Считывает лабиринт из текстового файла и возвращает его в виде двумерного массива
    """
    with open(filename) as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze


def get_neighbors(maze, cell: tuple[int, int]):
    """
    Возвращает список соседних ячеек, в которые можно перейти
    """
    row, col = cell
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    valid_neighbors = []
    for neighbor in neighbors:
        row, col = neighbor
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#":
            valid_neighbors.append(neighbor)
    return valid_neighbors


def find_path(maze):
    """
    Ищет путь от начальной точки до конечной точки в лабиринте
    """
    start = (0, 1)
    end = (len(maze) - 1, len(maze[0]) - 2)

    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None


def main():
    filename = "maze-for-u.txt"
    maze = read_maze(filename)

    path = find_path(maze)


    # for i, row in enumerate(maze):                            -  -   -     -   -   --   -    -     - -   -  _  -    -  -      -  - -  -  -  -
    #     for j, item in enumerate(row):                        =-   - =- = - =  -  =- =   _.----~~~~~~-----..__ =   =-   -=-  - = =  -=--  = -
    #         if item == "#":                                   =#-=  =-# - == ##= -__..------~~~~-     .._     ~~-. #== -#- = =-  ##=-= =#- -
    #             maze[i][j] = "1"                              #===#==___.--.--~~~~     --~~~~---~ __  ~~----.__   ~~~~~~~---...._____#== =##=
    #         if item == " ":                                   ##(~~~~_..----~       ~~--=< O >- .----. -< O >=--~~             ..   .)#=#=##=
    #             maze[i][j] = "0"                              ###~-..__..--         ..  ___-----_...__-----___        _.  ~-=___..-~#########
    #                                                           ##==#===#==`   _    ..   (     " :_.}{._; " "   )      _-     '==#=##=====#=#==
    # for place in path:                                        =#-==-== =# \   ~~-      `   " " __###__  ""    '    -~     .'==-=#===#- -=- #=
    #     maze[place[0]][place[1]] = "3"  # тут точечка         -= == -=  -= `-._  ~-.    _`--~~~VvvvvVV~~---'_     ~..    _. #= =  =  ==# - ==
    #                                                            = -==  - = - == -.     `~##\(            )/###~' .     _.~    -=- = -= -=- -
    #                                                            = -  -= -   - -    -    `.###\#    {     #/####.'    _-~  - =  - - -  -    = -
    #                                                             -    -       -  -  -_    -####    !     #####-  ..    -    -       -   -   - -
    #                                                                                  -._  ~.###   }     ###-~ ___.-~
    #                                                                                     ~-  \##  / "   ##.~ /~
    #                                                                                       \ |###  "   ###' /
    #                                                                                         \`/\#######/\' ;
    #                                                                                          ~-.^^^^^^^ .-~
    #                                                                                            ~~~~~~~~
    for place in path:
        maze[place[0]][place[1]] = "."

    result = ""
    for line in maze:
        result += "".join(line) + "\n"

    with open("res.txt", "w") as f:
        f.write(result)


main()
