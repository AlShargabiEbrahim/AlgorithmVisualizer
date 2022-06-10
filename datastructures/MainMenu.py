import pygame
from Menubutton import *
from trees import *
import sys


cnt = 0


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


pygame.init()
screen = pygame.display.set_mode((1280, 720))

#
GraphsButton = MenuButton(640, 250, text_input="GRAPHS", font=get_font(75))
TreesButton = MenuButton(640, 400, text_input="TREES", font=get_font(75))
QuitButton = MenuButton(640, 550, text_input="QUIT", font=get_font(75))

# trees
perfectTree = MenuButton(640, 250, text_input="Perfect tree", font=get_font(75))
balancedTree = MenuButton(640, 370, text_input="Balanced tree", font=get_font(75))
completeTree = MenuButton(640, 490, text_input="Complete tree", font=get_font(75))
fullTree = MenuButton(640, 610, text_input="Full tree", font=get_font(75))

# graphs
# undirected_path , directed_path , directed_cycle , undirected_cycle , undirected_complete_graph , undirected_tree_graph , directed_tree_graph


undirectedPath = MenuButton(640, 200, text_input="undirected path ",font=get_font(55))
directedPath = MenuButton(640, 200 + 75, text_input="directed path", font=get_font(55))

directedCycle = MenuButton(640, 275+ 75, text_input="directed cycle ", font=get_font(55))
undirectedCycle = MenuButton(640, 275 + 75  + 75 , text_input="undirected cycle", font=get_font(55))

undirectedCompleteGraph = MenuButton(640, 350+ 75  + 75, text_input="undirected complete graph ", font=get_font(48))
undirectedTreeGraph = MenuButton(640, 350 +75 + 75 + 75, text_input="undirected tree graph", font=get_font(55))

directedTreeGraph = MenuButton(640, 650, text_input="directed tree graph", font=get_font(55))



def main_menu():
    running_menu = True
    while running_menu:

        BG = pygame.image.load("assets/Background.png")
        pygame.display.set_caption("MENU")
        screen.blit(BG, (0, 0))
        text = get_font(48).render("Data Structures VISUALIZER", True, "#b68f40")
        rect = text.get_rect(center=(640, 100))

        mousePositionX = pygame.mouse.get_pos()[0]
        mousePositionY = pygame.mouse.get_pos()[1]
        screen.blit(text, rect)

        for button in [GraphsButton, TreesButton, QuitButton]:
            button.changeColor(mousePositionX, mousePositionY)
            button.update(screen)
        pygame.display.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GraphsButton.checkMouseClick(mousePositionX, mousePositionY):
                    """"graphs menu"""
                    graphs_menu()
                    running_menu = False

                if TreesButton.checkMouseClick(mousePositionX, mousePositionY):
                    """Trees menu"""
                    trees_menu()
                    running_menu = False

                if QuitButton.checkMouseClick(mousePositionX, mousePositionY):
                    pygame.quit()
                    sys.exit()


def graphs_menu():
    # undirected_path , directed_path , directed_cycle , undirected_cycle , undirected_complete_graph , undirected_tree_graph , directed_tree_graph

    running_menu = True

    while running_menu:

        BG = pygame.image.load("assets/Background.png")
        screen.blit(BG, (0, 0))
        text = get_font(55).render("Graphs", True, "#b68f40")
        rect = text.get_rect(center=(640, 100))
        mousePositionX = pygame.mouse.get_pos()[0]
        mousePositionY = pygame.mouse.get_pos()[1]
        screen.blit(text, rect)

        for button in [undirectedPath, directedPath,directedCycle,undirectedCycle, undirectedCompleteGraph , undirectedTreeGraph, directedTreeGraph]:
            button.changeColor(mousePositionX, mousePositionY)
            button.update(screen)
        pygame.display.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if undirectedPath.checkMouseClick(mousePositionX, mousePositionY):
                    """undirectedPath"""
                    pygame.quit()
                    edges = undirected_path_matplotlib(6)
                    graph = undirected_path(6)
                    render_graph(graph)
                    render_graph_matplotlib(edges)

                if directedPath.checkMouseClick(mousePositionX, mousePositionY):
                    """directedPath"""
                    pygame.quit()
                    edges = directed_path_matplotlib(6)
                    graph = directed_path(6)
                    render_graph(graph)
                    render_graph_matplotlib(edges)

                if directedCycle.checkMouseClick(mousePositionX, mousePositionY):
                    """directedCycle"""
                    pygame.quit()
                    edges = directed_cycle_matplotlib(6)
                    graph = directed_cycle(6)
                    render_graph(graph)
                    render_graph_matplotlib(edges)

                if undirectedCycle.checkMouseClick(mousePositionX, mousePositionY):
                    """undirectedCycle"""
                    pygame.quit()
                    edges = undirected_cycle_matplotlib(6)
                    graph = undirected_cycle(6)
                    render_graph(graph)
                    render_graph_matplotlib(edges)

                if undirectedCompleteGraph.checkMouseClick(mousePositionX, mousePositionY):
                    """undirectedCompleteGraph"""
                    pygame.quit()
                    edges = undirected_complete_graph_matplotlib(6)
                    graph = undirected_complete_graph(6)
                    render_graph(graph)
                    render_graph_matplotlib(edges)

                if undirectedTreeGraph.checkMouseClick(mousePositionX, mousePositionY):
                    """undirectedTreeGraph"""
                    pygame.quit()
                    edges = undirected_tree_graph_matplotlib(6)
                    graph = undirected_tree_graph(6)
                    render_graph(graph)
                    render_graph_matplotlib(edges)

                if directedTreeGraph.checkMouseClick(mousePositionX, mousePositionY):
                    """undirectedCycle"""
                    pygame.quit()
                    edges = directed_tree_graph_matplotlib(6)
                    graph = directed_tree_graph(6)
                    render_graph(graph)
                    render_graph_matplotlib(edges)

                sys.exit()


def trees_menu():
    # perfect_tree , balanced_tree , complete_tree , full_tree

    running_menu = True
    while running_menu:

        BG = pygame.image.load("assets/Background.png")
        screen.blit(BG, (0, 0))
        text = get_font(55).render("Trees", True, "#b68f40")
        rect = text.get_rect(center=(640, 100))

        mousePositionX = pygame.mouse.get_pos()[0]
        mousePositionY = pygame.mouse.get_pos()[1]
        screen.blit(text, rect)
        for button in [perfectTree, balancedTree, completeTree, fullTree]:
            button.changeColor(mousePositionX, mousePositionY)
            button.update(screen)
        pygame.display.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if perfectTree.checkMouseClick(mousePositionX, mousePositionY):
                    """Perfect tree"""
                    pygame.quit()
                    edges = perfect_tree(6)
                    draw_tree_matplotlib(edges)
                    #main_menu()

                if balancedTree.checkMouseClick(mousePositionX, mousePositionY):
                    """Balanced tree"""
                    pygame.quit()
                    edges = balanced_tree(6)
                    draw_tree_matplotlib(edges)

                if completeTree.checkMouseClick(mousePositionX, mousePositionY):
                    """complete tree"""
                    pygame.quit()
                    edges = complete_tree(6)
                    draw_tree_matplotlib(edges)

                if fullTree.checkMouseClick(mousePositionX, mousePositionY):
                    """Full tree"""
                    pygame.quit()
                    edges = full_tree(6)
                    draw_tree_matplotlib(edges)


main_menu()