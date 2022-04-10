from Algorithms.pathfinders import *
from Buttons import *


algo_num = 0
delay = 0
cnt = 0
pygame.display.set_caption("Menu")
screen.blit(BG, (0, 0))
text = get_font(60).render("Pathfinder Visualizer", True, "#b68f40")
rect = text.get_rect(center=(640, 100))


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
    running_menu = True
    while running_menu:
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
                global delay

                if BackButton.checkMouseClick(mousePositionX, mousePositionY):
                    BG = pygame.image.load("assets/Background.png")
                    screen.blit(BG, (0, 0))
                    text = get_font(55).render("Pathfinding Algorithms", True, "#b68f40")
                    rect = text.get_rect(center=(640, 100))
                    algosOptions()

                if slowButton.checkMouseClick(mousePositionX, mousePositionY):
                    delay = 5
                    running_menu = False
                    finders_main(algo_num, delay)

                if averageButton.checkMouseClick(mousePositionX, mousePositionY):
                    delay = 15
                    running_menu = False
                    finders_main(algo_num, delay)

                if fastButton.checkMouseClick(mousePositionX, mousePositionY):
                    delay = 30
                    running_menu = False
                    finders_main(algo_num, delay)
                sys.exit()
