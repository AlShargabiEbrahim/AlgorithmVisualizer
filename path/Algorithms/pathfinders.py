#from .Dijkstra import *
from .A_star import *
#from .Bfs import *
import random


def finders_main(num, delay_num):
    pygame.init()
    screen = pygame.display.set_mode((width, width))

    if num == 1:
        pygame.display.set_caption('bfs Path Finding Visualizer')
    elif num == 2:
        pygame.display.set_caption('A *  Path Finding Visualizer')
    elif num == 3:
        pygame.display.set_caption('Dijkstra  Path Finding Visualizer')

    nodes_grid = create_grid_of_nodes(delay_num)
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
                    """First node to be drawn"""
                    new_node.set_color("TEAL")
                    start_node = new_node

                elif new_node != start_node and not end_node:
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
                    a_star_algo(nodes_grid, start_node, end_node, screen,delay_num)
                elif num == 2:
                    a_star_algo(nodes_grid, start_node, end_node, screen,delay_num)
                elif num == 3:
                    a_star_algo(nodes_grid, start_node, end_node, screen,delay_num)
                algo_finished = True

            if pygame.KEYDOWN == event.type:
                if event.key == pygame.K_SPACE and start_node and end_node and not algo_finished:
                    """Space click to start the algo """
                    for row in nodes_grid:
                        for node in row:
                            node.update_neighbors(nodes_grid)

                    if num == 1:
                        a_star_algo(nodes_grid, start_node, end_node, screen, delay_num)
                    elif num == 2:
                        a_star_algo(nodes_grid, start_node, end_node, screen, delay_num)
                    elif num == 3:
                        a_star_algo(nodes_grid, start_node, end_node, screen, delay_num)
                    algo_finished = True

                if event.key == pygame.K_r:
                    """R click to restart"""
                    start_node = None
                    end_node = None
                    nodes_grid = create_grid_of_nodes(delay_num)
                    algo_finished = False

                if event.key == pygame.K_m and start_node and end_node and not algo_finished:
                    """M click to gen Basic random maze"""
                    barriers = []
                    for _ in range(1, rows - 1):
                        for _ in range(1, rows - 1):
                            row, col = random.randint(1, rows - 2), random.randint(1, rows - 2)
                            n = nodes_grid[row][col]
                            while n in barriers or n == start_node or n == end_node:
                                row, col = random.randint(1, rows - 2), random.randint(1, rows - 2)
                                n = nodes_grid[row][col]

                            n.set_color("BLACK")
                            barriers.append(n)

                            if len(barriers) >= rows ** 2 * 0.3:
                                break

                if event.key == pygame.K_v and start_node and end_node and not algo_finished:
                    """recursive division maze vertical"""
                    row_s, col_s = start_node.get_pos()
                    row_e, col_e = end_node.get_pos()

                    for row in range(1, rows - 1):

                        col2 = random.randint(1, columns - 2)
                        while (col2 == col_s and row_s == row) or (col2 == col_e and row_e == row) :
                            col2 = random.randint(1, columns - 2)
                        n = nodes_grid[row][col2]
                        n.set_color("WHITE")

                        col3 = random.randint(1, columns - 2)
                        while (col3 == col_s and row_s == row) or (col3 == col_e and row_e == row) or (col3 == col2):
                            col3 = random.randint(1, columns - 2)
                        n = nodes_grid[row][col3]
                        n.set_color("WHITE")

                        for column in range(1, columns - 1):
                            n = Node(row, column, node_width)

                            if row_s == row and col_s == column:
                                continue
                            elif row_e == row and col_e == column:
                                continue

                            else:
                                if row % 2 == 1:

                                    if not (row_s == row and col_s == column) and not (
                                            row_e == row and col_e == column) and not (column == col2) and not (column == col3):
                                        n = nodes_grid[row][column]
                                        n.set_color("BLACK")

                if event.key == pygame.K_h and start_node and end_node and not algo_finished:
                    """recursive division maze horizontal"""

                    row_s, col_s = start_node.get_pos()
                    row_e, col_e = end_node.get_pos()

                    for column in range(1, columns - 1):

                        white_node = random.randint(1, 3)
                        for _ in range(white_node):
                            row2 = random.randint(1, rows - 2)
                            while (column == col_s and row_s == row2) or (column == col_e and row_e == row2):
                                row2 = random.randint(1, rows - 2)
                            n = nodes_grid[row2][column]
                            n.set_color("WHITE")

                        row3 = random.randint(1, rows - 2)
                        while (column == col_s and row_s == row3) or (column == col_e and row_e == row3):
                            row3 = random.randint(1, rows - 2)
                        n = nodes_grid[row3][column]
                        n.set_color("WHITE")

                        for row in range(1, rows - 1):

                            n = Node(row, column, node_width)

                            if row_s == row and col_s == column:
                                continue
                            elif row_e == row and col_e == column:
                                continue

                            else:
                                if column % 2 == 1:

                                    if not (row_s == row and col_s == column) and not (
                                            row_e == row and col_e == column) and not (row == row2) and not (
                                            row == row3):
                                        n = nodes_grid[row][column]
                                        n.set_color("BLACK")

    pygame.quit()
