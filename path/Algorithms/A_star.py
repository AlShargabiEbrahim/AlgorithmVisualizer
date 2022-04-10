from queue import PriorityQueue
from path.Board import *
import math


def a_star_algo(nodes_grid, start_node, end_node, screen, delay):
    cnt = 0
    pq = PriorityQueue()
    pq.put((0, cnt, start_node))
    parent_nodes = {}
    nodes_g_score = {}
    nodes_f_score = {}

    pq_hash = {start_node}

    for row in nodes_grid:
        for node in row:
            nodes_g_score[node] = float('inf')

    nodes_g_score[start_node] = 0

    for row in nodes_grid:
        for node in row:
            nodes_f_score[node] = float('inf')

    x1, y1 = start_node.get_pos()
    x2, y2 = end_node.get_pos()
    nodes_f_score[start_node] = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

    while not pq.empty():
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.exit()

        current_node = pq.get()[2]
        pq_hash.remove(current_node)

        if current_node == end_node:
            end_node.set_color("PURPLE")
            draw_shorties_path(parent_nodes, end_node, nodes_grid, screen)
            start_node.set_color("TEAL")
            return True

        for neighbor in current_node.neighbors_nodes:
            g_score = nodes_g_score[current_node] + 1

            if g_score < nodes_g_score[neighbor]:
                """Shorter path"""
                parent_nodes[neighbor] = current_node
                nodes_g_score[neighbor] = g_score

                x1, y1 = neighbor.get_pos()
                x2, y2 = end_node.get_pos()
                nodes_f_score[neighbor] = g_score + math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

                if neighbor not in pq_hash:
                    cnt = cnt + 1
                    pq.put((nodes_f_score[neighbor], cnt, neighbor))
                    pq_hash.add(neighbor)

                    neighbor.set_color("GREY")
        draw(nodes_grid, screen)

        if current_node != start_node:
            clock.tick(delay)
            current_node.set_color("BLUE")
    return False
