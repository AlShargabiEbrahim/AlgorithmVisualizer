from Menubutton import *
import pygame


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Lato-Black.ttf", size)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
BG = pygame.image.load("assets/menuback.jpg")

instructionsButton = MenuButton(640, 250, text_input="INSTRUCTIONS", font=get_font(75))
OptionsButton = MenuButton(640, 400, text_input="OPTIONS", font=get_font(75))
QuitButton = MenuButton(640, 550, text_input="QUIT", font=get_font(75))

#options
bfsButton = MenuButton(640, 250, text_input="BFS", font=get_font(75))
aStarButton = MenuButton(640, 370, text_input="A Star", font=get_font(75))
DijkstraButton = MenuButton(640, 490, text_input="Dijkstra", font=get_font(75))
bfsButton = MenuButton(640, 250, text_input="BFS", font=get_font(75))
aStarButton = MenuButton(640, 370, text_input="A Star", font=get_font(75))
DijkstraButton = MenuButton(640, 490, text_input="Dijkstra", font=get_font(75))

#
BackButton = MenuButton(640, 610, text_input="BACK", font=get_font(75))
contButton = MenuButton(640, 650, text_input="CONTINUE", font=get_font(75))

#delay
slowButton = MenuButton(640, 250, text_input="SLOW", font=get_font(75))
averageButton = MenuButton(640, 370, text_input="AVERAGE", font=get_font(75))
fastButton = MenuButton(640, 490, text_input="FAST", font=get_font(75))


#instructions
contButton2 = MenuButton(640, 200, text_input="LEFT-CLICK: draws start node (TEAL square), end node (PURPPLE square), ",font=get_font(19))
contButton22 = MenuButton(640, 200 + 25, text_input="and obstacle (BLACK square)", font=get_font(19))

contButton32 = MenuButton(640, 275, text_input="RIGHT-CLICK: removes obstacle, start node, or end node ", font=get_font(19))
contButton3 = MenuButton(640, 275 + 25, text_input="depending on the square that is clicked.", font=get_font(19))

contButton42 = MenuButton(640, 350, text_input="MIDDLE-CLICK or SPACE KEY: starts the chosen algorithm  ", font=get_font(19))
contButton4 = MenuButton(640, 350 + 25, text_input="according to the given start and end nodes", font=get_font(19))

contButton5 = MenuButton(640, 425, text_input="R KEY: restarts the board", font=get_font(19))

contButton6 = MenuButton(640, 425+50, text_input="M KEY: draws a basic random maze", font=get_font(19))
contButton62 = MenuButton(640, 425+100, text_input="H KEY: draws a horizontal maze", font=get_font(19))
contButton63 = MenuButton(640, 425+150, text_input="V KEY: draws a vertical maze", font=get_font(19))
