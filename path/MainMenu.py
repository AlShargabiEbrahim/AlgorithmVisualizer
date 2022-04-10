import pygame

from Menubutton import MenuButton
from Algorithms.pathfinders import *


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
algo_num = 0
cnt = 0
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Background.png")
screen.blit(BG, (0, 0))
text = get_font(60).render("Pathfinder Visualizer", True, "#b68f40")
rect = text.get_rect(center=(640, 100))
instructionsButton = MenuButton(640, 250, text_input="Instructions", font=get_font(75))
OptionsButton = MenuButton(640, 400, text_input="Options", font=get_font(75))
QuitButton = MenuButton(640, 550, text_input="QUIT", font=get_font(75))
bfsButton = MenuButton(640, 250, text_input="BFS", font=get_font(75))
aStarButton = MenuButton(640, 370, text_input="A Star", font=get_font(75))
DijkstraButton = MenuButton(640, 490, text_input="Dijkstra", font=get_font(75))
bfsButton = MenuButton(640, 250, text_input="BFS", font=get_font(75))
aStarButton = MenuButton(640, 370, text_input="A Star", font=get_font(75))
DijkstraButton = MenuButton(640, 490, text_input="Dijkstra", font=get_font(75))
BackButton = MenuButton(640, 610, text_input="Back", font=get_font(75))
slowButton = MenuButton(640, 250, text_input="Slow", font=get_font(75))
averageButton = MenuButton(640, 370, text_input="Average", font=get_font(75))
fastButton = MenuButton(640, 490, text_input="Fast", font=get_font(75))


def main_menu():
    running_menu = True
    while running_menu:

        mousePositionX = pygame.mouse.get_pos()[0]
        mousePositionY = pygame.mouse.get_pos()[1]
        screen.blit(text, rect)

        for button in [instructionsButton, OptionsButton, QuitButton]:
            button.changeColor(mousePositionX, mousePositionY)
            button.update(screen)
        pygame.display.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if instructionsButton.checkMouseClick(mousePositionX, mousePositionY):
                    """"""
                    #finders_main(algo_num)
                    running_menu = False

                if OptionsButton.checkMouseClick(mousePositionX, mousePositionY):
                    algosOptions()
                    running_menu = False

                if QuitButton.checkMouseClick(mousePositionX, mousePositionY):
                    pygame.quit()
                    sys.exit()


def algosOptions():
    running_menu = True

    while running_menu:

        BG = pygame.image.load("assets/Background.png")
        screen.blit(BG, (0, 0))
        text = get_font(55).render("Pathfinding Algorithms", True, "#b68f40")
        rect = text.get_rect(center=(640, 100))

        mousePositionX = pygame.mouse.get_pos()[0]
        mousePositionY = pygame.mouse.get_pos()[1]
        screen.blit(text, rect)
        for button in [bfsButton, aStarButton, DijkstraButton, BackButton]:
            button.changeColor(mousePositionX, mousePositionY)
            button.update(screen)
        pygame.display.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global algo_num

                if bfsButton.checkMouseClick(mousePositionX, mousePositionY):
                    algo_num = 1
                    running_menu = False
                    delayOptions()

                if aStarButton.checkMouseClick(mousePositionX, mousePositionY):
                    algo_num = 2
                    running_menu = False
                    delayOptions()

                if DijkstraButton.checkMouseClick(mousePositionX, mousePositionY):
                    algo_num = 3
                    running_menu = False
                    delayOptions()

                if BackButton.checkMouseClick(mousePositionX, mousePositionY):
                    BG = pygame.image.load("assets/Background.png")
                    screen.blit(BG, (0, 0))
                    text = get_font(60).render("Pathfinder Visualizer", True, "#b68f40")
                    rect = text.get_rect(center=(640, 100))
                    main_menu()
                    sys.exit()


def delayOptions():
    while True:
        BG = pygame.image.load("assets/Background.png")
        screen.blit(BG, (0, 0))
        text = get_font(60).render("Speed of the Algorithm", True, "#b68f40")
        rect = text.get_rect(center=(640, 100))

        mousePositionX = pygame.mouse.get_pos()[0]
        mousePositionY = pygame.mouse.get_pos()[1]
        screen.blit(text, rect)
        for button in [slowButton, averageButton, fastButton, BackButton]:
            button.changeColor(mousePositionX, mousePositionY)
            button.update(screen)
        pygame.display.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if BackButton.checkMouseClick(mousePositionX, mousePositionY):
                    BG = pygame.image.load("assets/Background.png")
                    screen.blit(BG, (0, 0))
                    text = get_font(55).render("Pathfinding Algorithms", True, "#b68f40")
                    rect = text.get_rect(center=(640, 100))

                else:
                    finders_main(algo_num)
                    sys.exit()
