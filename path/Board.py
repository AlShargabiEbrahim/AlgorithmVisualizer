import pygame
from .Colors import colors
from .Node import Node
import sys


width = 600
rows, columns = 40, 40
node_width = width // rows
clock = pygame.time.Clock()
delay = 10 #IMP LATER


def create_grid_of_nodes():
    nodes_grid = []
    for row in range(rows):
        nodes_grid.append([])
        for column in range(columns):
            n = Node(row, column, node_width)
            if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
                n.set_color("BLACK")
            nodes_grid[row].append(n)

    return nodes_grid


def draw_grid_lines(screen):
    for i in range(rows):
        pygame.draw.line(screen, colors["GREY"], (0, i*node_width), (width, i*node_width)) # horizontal
        for j in range(columns):
            pygame.draw.line(screen, colors["GREY"], (j * node_width, 0), (j * node_width, width))  # vertical


def draw(grid, screen):
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            pygame.quit()
            sys.exit()
        else:
            screen.fill(colors["WHITE"])
    for row in grid:
        for node in row:
            pygame.draw.rect(screen, node.color, (node.x, node.y, node_width, node_width))

    draw_grid_lines(screen)
    pygame.display.update()


def draw_shorties_path(parent_nodes, current, grid, screen):
    cnt = 0
    while current in parent_nodes:
        clock.tick(delay)
        current = parent_nodes[current]
        current.set_color("YELLOW")
        cnt = cnt + 1
        draw(grid, screen)

