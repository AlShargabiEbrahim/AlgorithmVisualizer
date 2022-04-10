from Menubutton import *
import pygame


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
BG = pygame.image.load("assets/Background.png")
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

