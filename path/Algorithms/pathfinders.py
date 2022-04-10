#from .Dijkstra import *
from .A_star import *
#from .Bfs import *
import random


def finders_main(num):
    pygame.init()
    screen = pygame.display.set_mode((width, width))

    if num == 1:
        pygame.display.set_caption('bfs Path Finding Visualizer')
    elif num == 2:
        pygame.display.set_caption('A *  Path Finding Visualizer')
    elif num == 3:
        pygame.display.set_caption('Dijkstra  Path Finding Visualizer')

    nodes_grid = create_grid_of_nodes()
    still_running = True
    algo_started = False
    algo_finished = False
    start_node = None
    end_node = None

    while still_running:
        draw(nodes_grid, screen)
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                still_running = False

            if algo_started:
                continue

            if pygame.mouse.get_pressed()[0]:
                """Left click to delete the color form any node """
                y, x = pygame.mouse.get_pos()
                row, col = y // node_width, x // node_width

                new_node = nodes_grid[row][col]
                if row == 0 or row == rows - 1 or col == 0 or col == columns - 1:
                    new_node.set_color("BLACK")
                elif new_node != end_node and not start_node:
                    """CHECK plz"""
                    """First node to be drawn"""
                    new_node.set_color("TEAL")
                    start_node = new_node

                elif new_node != start_node and not end_node:
                    """CHECK plz"""
                    """Second node to be drawn"""
                    new_node.set_color("PURPLE")
                    end_node = new_node

                elif start_node and end_node and new_node != start_node and new_node != end_node and not algo_finished:
                    """Nodes that will be drawn after the first and second nodes"""
                    new_node.set_color("BLACK")

            elif pygame.mouse.get_pressed()[2] and not algo_finished:
                """Right click to choose start , end , barriers nodes"""
                y, x = pygame.mouse.get_pos()
                row, col = y // node_width, x // node_width

                new_node = nodes_grid[row][col]
                if new_node.color != colors["WHITE"]:
                    new_node.set_color("WHITE")

                    if new_node == start_node:
                        start_node = None
                    elif new_node == end_node:
                        end_node = None

            if pygame.mouse.get_pressed()[1] and start_node and end_node:
                """Middle click to start the algo"""
                for row in nodes_grid:
                    for node in row:
                        node.update_neighbors_nodes(nodes_grid)
                if num == 1:
                    a_star_algo(nodes_grid, start_node, end_node, screen)
                elif num == 2:
                    a_star_algo(nodes_grid, start_node, end_node, screen) #
                elif num == 3:
                    a_star_algo(nodes_grid, start_node, end_node, screen)#
                algo_finished = True

            if pygame.KEYDOWN == event.type:
                #menu = MainMenu(screen)
                if event.key == pygame.K_SPACE and start_node and end_node and not algo_finished:
                    """Space click to start the algo """
                    for row in nodes_grid:
                        for node in row:
                            node.update_neighbors(nodes_grid)

                    if num == 1:
                        a_star_algo(nodes_grid, start_node, end_node, screen) #
                    elif num == 2:
                        a_star_algo(nodes_grid, start_node, end_node, screen)
                    elif num == 3:
                        a_star_algo(nodes_grid, start_node, end_node, screen) #
                    algo_finished = True

    pygame.quit()
