from Algorithms.pathfinders import *
from tkinter import *

import pygame, sys
from Menubutton import MenuButton

algo_num = 0
cnt = 0


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def main_menu():
    pygame.init()

    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")

    BG = pygame.image.load("assets/Background.png")
    running_menu = True
    while running_menu:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        BFS_BUTTON = MenuButton(640, 250,text_input="BFS", font=get_font(75))
        A_BUTTON = MenuButton(640, 400 , text_input="A Star", font=get_font(75))

        #QUI_BUTTON = Button(None, pos=(640, 550),
        #                     text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = MenuButton(640, 700,text_input="QUIT", font=get_font(75))

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [BFS_BUTTON, A_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global algo_num
                if BFS_BUTTON.checkMouseClick(MENU_MOUSE_POS):
                    algo_num = 1
                    finders_main(algo_num)
                    running_menu = False

                if A_BUTTON.checkMouseClick(MENU_MOUSE_POS):
                    algo_num = 2
                    finders_main(algo_num)
                    running_menu = False

                if QUIT_BUTTON.checkMouseClick(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


main_menu()

