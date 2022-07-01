import sys
import pygame
from random import randint
from time import time
from math import ceil
colors = {'WHITE': (255, 255, 255), #nodes
          'BLACK': (0, 0, 0), #barriers
          'GREY': (128, 128, 128),
          'BLUE': (0, 51, 102), #visted_node
          'YELLOW': (255, 255, 153), #path
          'PURPLE': (128,0,128), #end_node
          'TEAL': (0, 153, 153), #start_node
}
pygame.init()

# Display settings
w , h = 900,500

windowSize = (w, h)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Data Structures Visualizer')


def get_font(size):
    """Returns Press-Start-2P in the desired size"""
    #return pygame.font.Font('./images/font.ttf', size)
    return pygame.font.SysFont('./images/font.ttf', size)

# Font
baseFont = get_font(24)
#
line_thickness = 5

class BinaryTree:
    def __init__(self, rect):
        self.rect = rect
    def add(self, item): pass
    def remove(self, item): pass
    def search(self, item): pass
    #line y=mx+b
    #circle (x-h)^2+(y-k)^2=r^2
    def draw(self):
        level = 1
        parentCenters = {}
        allcenters = []
        centers = [(self.rect.left + self.rect.width // 2, self.rect.top + space // 4)]
        while True:
            allcenters.append(centers)
            for center in centers:                
                if center in parentCenters: pygame.draw.line(screen, colors['BLACK'], center, parentCenters[center])
            nextcenters = []
            for i in range(len(centers)):
                c = (centers[i][0] - space // (2 ** (level-1)), self.rect.top + space // 4 + space // 2 * level)
                parentCenters[c] = centers[i]
                nextcenters.append(c)
                c = (centers[i][0] + space // (2 ** (level-1)), self.rect.top + space // 4 + space // 2 * level)
                parentCenters[c] = centers[i]
                nextcenters.append(c)
            level += 1
            centers = nextcenters
            if level == 5: break
        for centers in allcenters:
            for center in centers:                
                pygame.draw.circle(screen, colors['BLUE'], center, space // 8)
        
class LinkedList:
    def __init__(self, rect):
        self.rect = rect
        self.linkedlist = []
    def push(self, item):
        self.linkedlist.append(item)
    def pop(self):
        self.linkedlist.pop()
    def enqueue(self, item):
        self.linkedlist.insert(0, item)
    def pop0(self):
        self.linkedlist.pop(0)
    def draw(self):
        offset = 0
        for x in self.linkedlist:
            rect = pygame.Rect(self.rect.left + offset, self.rect.top, space // 2, self.rect.height)
            offset += space // 2
            pygame.draw.rect(screen, colors['BLUE'], rect, line_thickness)
            screen.blit(baseFont.render(str(x), True, colors['BLUE']), (rect.x + rect.width//4, rect.y + rect.height//4))
        rect = pygame.Rect(self.rect.left + offset, self.rect.top, space // 2, self.rect.height)
        pygame.draw.rect(screen, colors['GREY'], rect, line_thickness)
        screen.blit(baseFont.render("NULL", True, colors['GREY']), (rect.x + rect.width//4, rect.y + rect.height//4))

class SizeField:
    def __init__(self, rect, size):
        self.hover = False
        self.rect = rect
        self.size = size
        self.max_size = 2999

    def draw(self):
        """Draw the field with the starting number"""
        if (isinstance(self.size, int)):
            screen.blit(baseFont.render("Value", True, colors['BLACK']), (self.rect.x - self.rect.width//2, self.rect.y - self.rect.height//2))
        pygame.draw.rect(screen, colors['BLACK'], self.rect, line_thickness)
        screen.blit(baseFont.render(str(self.size), True, colors['BLACK']), (self.rect.x + self.rect.height//4, self.rect.y + self.rect.height//4))
        #self.rect.w = 65

    def update(self, event):
        """Updating the size if the user hovers over the size field , the size is between 1 and 1999"""
        if self.rect.collidepoint(pygame.mouse.get_pos()) == 1:
            self.hover = True
        else:
            self.hover = False

        if self.hover and event.type == pygame.KEYDOWN and isinstance(self.size, int):
            #if int(self.size) > 9:
            if event.key == pygame.K_BACKSPACE:
                    self.size = int(str(self.size)[:-1])

            if self.size == '':
                if event.unicode.isdigit() and int(event.unicode) <= 2 and int(event.unicode) != 0:
                    self.size = int(str(self.size) + event.unicode)
            else:
                if event.unicode.isdigit():
                    if int(self.size) + int(event.unicode) < self.max_size:
                        self.size = int(str(self.size) + event.unicode)
        self.mousePos = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed() != (0, 0, 0)

        if self.rect.collidepoint(self.mousePos):
            self.isClicked = True
        else :
            self.isClicked = False

        if self.isClicked and self.clicked:
            self.isClicked = True
        else:
            self.isClicked = False                        

space = 200
sizeBox = SizeField(pygame.Rect( (w // 4) + space + space, (h - 60), line_thickness, line_thickness * 10), 1)  # x,y , w, h
pushButton = SizeField(pygame.Rect( (w // 4) + space + space + space//2, (h - 60), line_thickness * 10, line_thickness * 10), "Push")
popButton = SizeField(pygame.Rect( (w // 4) + space + space + space, (h - 60), line_thickness * 10, line_thickness * 10), "Pop") #/Dequeue
enqueueButton = SizeField(pygame.Rect( (w // 4) + space + space + space//2, (h - 100), line_thickness * 10+20, line_thickness * 10), "Enqueue")
removeFrontButton = SizeField(pygame.Rect( (w // 4) + space + space + space, (h - 100), line_thickness * 10+20, line_thickness * 10), "Pop(0)")

#linkedList = LinkedList(pygame.Rect(space // 4, space, w - space // 2, space // 2))
binaryTree = BinaryTree(pygame.Rect(space // 4, space // 8, w - space // 2, space * 2))

def updateWidgets(event):
    """"Update the menu"""
    sizeBox.update(event)
    pushButton.update(event)
    popButton.update(event)
    enqueueButton.update(event)
    removeFrontButton.update(event)
def renderBottomMenu():
    """"Draw the menu"""
    sizeBox.draw()
    pushButton.draw()
    popButton.draw()
    enqueueButton.draw()
    removeFrontButton.draw()
    #linkedList.draw()
    binaryTree.draw()
def render():
    """render the window"""
    screen.fill(colors["WHITE"])
    renderBottomMenu()
    pygame.display.update()

def data_visualizer():
    array_to_be_sorted = []
    running = True
    alg_iterator = None
    timer_delay = time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


            updateWidgets(event)
            if pushButton.isClicked:
                linkedList.push(sizeBox.size)
            if popButton.isClicked:
                linkedList.pop()
            render()



if __name__ == '__main__':
    data_visualizer()
