from Menubutton import MenuButton
from Algorithms.pathfinders import *

algo_num = 0
cnt = 0


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.init()

    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")

    BG = pygame.image.load("assets/Background.png")
    running_menu = True
    while running_menu:
        SCREEN.blit(BG, (0, 0))
        mousePositionX = pygame.mouse.get_pos()[0]
        mousePositionY = pygame.mouse.get_pos()[1]

        text = get_font(60).render("Pathfinder visualizer", True, "#b68f40")
        rect = text.get_rect(center=(640, 100))
        SCREEN.blit(text, rect)

        bfsButton = MenuButton(640, 250, text_input="BFS", font=get_font(75))
        aStarButton= MenuButton(640, 370, text_input="A Star", font=get_font(75))
        DijkstraButton = MenuButton(640, 490, text_input="Dijkstra", font=get_font(75))
        QuitButton = MenuButton(640, 620, text_input="QUIT", font=get_font(75))


        for button in [bfsButton, aStarButton, DijkstraButton, QuitButton]:
            button.changeColor(mousePositionX, mousePositionY)
            button.update(SCREEN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global algo_num

                if bfsButton.checkMouseClick(mousePositionX, mousePositionY):
                    algo_num = 1
                    finders_main(algo_num)
                    running_menu = False

                if aStarButton.checkMouseClick(mousePositionX, mousePositionY):
                    algo_num = 2
                    finders_main(algo_num)
                    running_menu = False

                if DijkstraButton.checkMouseClick(mousePositionX, mousePositionY):
                    algo_num = 3
                    finders_main(algo_num)
                    running_menu = False

                if QuitButton.checkMouseClick(mousePositionX, mousePositionY):
                    pygame.quit()
                    sys.exit()

