with open('maze-for-me-done.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]

import pygame

CELL_SIZE = len(maze[0])//450

WIDTH = len(maze[0]) * CELL_SIZE
HEIGHT = len(maze) * CELL_SIZE

WALL_COLOR = (0, 0, 0)
START_COLOR = (0, 0, 255)
END_COLOR = (255, 0, 0)
STAR_COLOR = (255, 255, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill((255, 255, 255))

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == "#":
            pygame.draw.rect(screen, WALL_COLOR, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        elif maze[y][x] == ".":
            pygame.draw.rect(screen, START_COLOR, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        elif maze[y][x] == ",":
            pygame.draw.rect(screen, END_COLOR, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        elif maze[y][x] == "*":
            pygame.draw.rect(screen, STAR_COLOR, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
