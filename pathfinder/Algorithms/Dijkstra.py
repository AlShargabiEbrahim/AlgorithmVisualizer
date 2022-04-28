import sys
from queue import PriorityQueue
import pygame
from path.Board import draw_shorties_path, draw, clock, delay


def dijkstra_algo(nodes_grid, start_node, end_node, screen):
    cnt = 0
    pq = PriorityQueue()
    pq.put((0, cnt, start_node))
    parent_nodes = {}
    nodes_score = {}
    pq_hash = {start_node}

    for row in nodes_grid:
        for node in row:
            nodes_score[node] = float('inf')

    nodes_score[start_node] = 0

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
            g_score = nodes_score[current_node] + 1

            if g_score < nodes_score[neighbor]:
                """Shorter path"""
                parent_nodes[neighbor] = current_node
                nodes_score[neighbor] = g_score

                if neighbor not in pq_hash:
                    cnt = cnt + 1
                    pq.put((nodes_score[neighbor], cnt, neighbor))
                    pq_hash.add(neighbor)

                    neighbor.set_color("GREY")
        draw(nodes_grid, screen)

        if current_node != start_node:
            #for _ in range(10000):
            #    print("")
            #time.sleep(0.05) # slow
            clock.tick(delay)
            #time.sleep(0.015)  # avg
            current_node.set_color("BLUE")
    return False

"""
def algo_check(nodes_grid, start_node, end_node, screen):
    cnt = 0
    pq = PriorityQueue()
    pq.put((0, cnt, start_node))
    parent_nodes = {}
    nodes_score = {}
    pq_hash = {start_node}

    for row in nodes_grid:
        for node in row:
            nodes_score[node] = float('inf')

    nodes_score[start_node] = 0

    while not pq.empty():
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.exit()

        current_node = pq.get()[2]
        pq_hash.remove(current_node)

        if current_node == end_node:
            return True

        for neighbor in current_node.neighbors_nodes:
            g_score = nodes_score[current_node] + 1

            if g_score < nodes_score[neighbor]:
                #Shorter path
                parent_nodes[neighbor] = current_node
                nodes_score[neighbor] = g_score

                if neighbor not in pq_hash:
                    cnt = cnt + 1
                    pq.put((nodes_score[neighbor], cnt, neighbor))
                    pq_hash.add(neighbor)

                    #neighbor.set_color("GREY")
        draw(nodes_grid, screen)

        if current_node != start_node:
            pass
            #for _ in range(10000):
            #    print("")
            #time.sleep(0.05) # slow
            #time.sleep(0.015)  # avg
            #current_node.set_color("BLUE")
    return False
"""