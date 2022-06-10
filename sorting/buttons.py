import pygame
from math import ceil
from colors import colors
from algs import algorithmsDict

pygame.init()

# Display settings
w , h = 900,500

windowSize = (w, h)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Sorting Algorithms Visualizer')


def get_font(size):
    """Returns Press-Start-2P in the desired size"""
    #return pygame.font.Font('./images/font.ttf', size)
    return pygame.font.SysFont('./images/font.ttf', size)

# Font
baseFont = get_font(24)
#
line_thickness = 5



class options:
    def __init__(self,  rect):
        self.clicked = False
        self.rect = rect
        #self.list_of_rects = []
        self.algorithms = list(algorithmsDict)
        self.algorithms_options = pygame.Rect((self.rect.x, 0, ceil((len(self.algorithms) - 1) * self.rect.height / self.rect.y) * self.rect.width, self.rect.y))

    def draw(self):
        """"Draw the algorithms field"""
        screen.blit(baseFont.render("Algorithm", True, colors['BLACK']), (self.rect.x + self.rect.w // 4, self.rect.y - self.rect.h // 2))
        pygame.draw.rect(screen, colors['BLACK'], self.rect, line_thickness)
        screen.blit(baseFont.render(self.algorithms[0], line_thickness, colors["BLACK"]), (self.rect.x + self.rect.w //4, self.rect.y + self.rect.h // 4) )

        if self.clicked:
            col = 0
            num_of_algo = 0

            #rect = self.rect.copy()
            #rect.y = rect.y - ((num_of_algo + 1) * self.rect.height)
            #rect.x = self.rect.x +  self.rect.width
            #self.list_of_rects.append(rect)

            for i in range(1, len(self.algorithms)):
                rect = self.rect.copy()
                rect.y = rect.y - ((num_of_algo + 1) * self.rect.height )
                if rect.y <= self.algorithms_options.y:
                    col += 1
                    num_of_algo = 0
                    rect.y = self.rect.y - self.rect.height
                num_of_algo += 1
                rect.x = self.rect.x + col * self.rect.width
                #if i != len(self.algorithms)-1:
                #    self.list_of_rects.append(rect)

                pygame.draw.rect(screen, colors["WHITE"], rect, 0)
                pygame.draw.rect(screen, colors["BLACK"], rect, line_thickness)
                screen.blit(baseFont.render(self.algorithms[i][:], line_thickness, colors["BLACK"]), (rect.x + rect.w // 4, rect.y + rect.h // 4))

    def update(self):
        """Updating the algorithm if the user chooses another algorithm """
        col = 0
        num_of_algo = 0
        for i in range(len(self.algorithms)-1):
            rect = self.rect.copy()
            rect.y = rect.y - ((num_of_algo + 1) * self.rect.height)
            if rect.y <= self.algorithms_options.y:
                col += 1
                num_of_algo = 0
                rect.y = self.rect.y - self.rect.height
            num_of_algo += 1
            rect.x = self.rect.x + col * self.rect.width
            if rect.collidepoint(pygame.mouse.get_pos()):
                self.working_options = i

        if pygame.mouse.get_pressed() != (0, 0, 0):
            if self.algorithms_options.collidepoint(pygame.mouse.get_pos()):

                self.algorithms[0], self.algorithms[self.working_options + 1] = \
                    self.algorithms[self.working_options + 1], self.algorithms[0]
                self.working_options = 0
            self.clicked = self.rect.collidepoint(pygame.mouse.get_pos())


class Slider:
    def __init__(self, rect):
        self.hover = False
        self.rect = rect
        self.speed = self.rect.x + line_thickness

    def draw(self):
        """Draw the slider"""
        screen.blit(baseFont.render("Speed", True, colors['BLACK']), (self.rect.x + self.rect.w//3, self.rect.y - self.rect.h//2))
        self.rect.w +=1
        pygame.draw.rect(screen, colors['BLACK'], self.rect, line_thickness)
        self.rect.w -=1
        pygame.draw.line(screen, colors['BLACK'], (self.rect.x + line_thickness, self.rect.y + self.rect.h//2), (self.rect.x + self.rect.w - line_thickness, self.rect.y + self.rect.h//2), line_thickness//2)
        pygame.draw.line(screen, colors['BLACK'], (self.speed, self.rect.y + line_thickness), (self.speed, self.rect.y + self.rect.h - line_thickness), line_thickness*2)

    def update(self, event):
        """Updating the slider if the user moves it, and changes the speed according to the change"""
        self.mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pygame.mouse.get_pos()) == 1:
            self.hover = True
        else:
            self.hover = False
        initial_speed = self.rect.x + line_thickness
        self.min_speed = self.rect.x + line_thickness
        self.max_speed = self.rect.x + self.rect.w - line_thickness
        self.speed += self.min_speed - initial_speed

        if self.hover:
            if pygame.mouse.get_pressed() != (0, 0, 0):
                if (self.rect.x + line_thickness) <= self.mousePos[0] and self.mousePos[0] <= (self.rect.x + self.rect.w - line_thickness):
                    self.speed = self.mousePos[0]


class SizeField:
    def __init__(self, rect):
        self.hover = False
        self.rect = rect
        self.size = '1'
        self.max_size = 2999

    def draw(self):
        """Draw the field with the starting number"""
        screen.blit(baseFont.render("Array's size", True, colors['BLACK']), (self.rect.x - self.rect.w//2, self.rect.y - self.rect.h//2))
        pygame.draw.rect(screen, colors['BLACK'], self.rect, line_thickness)
        screen.blit(baseFont.render(self.size, True, colors['BLACK']), (self.rect.x + self.rect.h//4, self.rect.y + self.rect.h//4))
        self.rect.w = 65

    def update(self, event):
        """Updating the size if the user hovers over the size field , the size is between 1 and 1999"""
        if self.rect.collidepoint(pygame.mouse.get_pos()) == 1:
            self.hover = True
        else:
            self.hover = False

        if self.hover and event.type == pygame.KEYDOWN:
            #if int(self.size) > 9:
            if event.key == pygame.K_BACKSPACE:
                    self.size = self.size[:-1]

            if self.size == '':
                if event.unicode.isdigit() and int(event.unicode) <= 2 and int(event.unicode) != 0:
                    self.size += event.unicode
            else:
                if event.unicode.isdigit():
                    if int(self.size) + int(event.unicode) < self.max_size:
                        self.size += event.unicode



def rgb_hlight(clr, hlight):
    return (max(min(clr[0]+hlight, 255), 0), max(min(clr[1]+hlight, 255), 0), max(min(clr[2]+hlight, 255), 0))

class Button:
    def __init__(self, text, pos, font, click, fg="white", bg="black", hoverbg="gray"):
        self.x, self.y = pos; self.text = text
        self.fg, self.bg, self.hoverbg, self.font = pygame.Color(fg), pygame.Color(bg), pygame.Color(hoverbg), font
        self.isDown, self.isHover = False, False
        self.click = click
        self.redraw(self.bg)

    def redraw(self, bg):
        self.isDrawn = False
        self.textsurf = self.font.render(self.text, 1, self.fg, bg)
        self.size = self.textsurf.get_size()
        lwidth, hlight = 2, 40
        self.size = (self.size[0]+lwidth*2, self.size[1]+lwidth*2)
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        pygame.draw.line(self.surface, rgb_hlight(bg, hlight), (0, 0), (0, self.size[1]), lwidth)
        pygame.draw.line(self.surface, rgb_hlight(bg, hlight), (0, 0), (self.size[0], 0), lwidth)
        pygame.draw.line(self.surface, rgb_hlight(bg, -hlight), (lwidth, self.size[1]-lwidth), (self.size[0], self.size[1]-lwidth), lwidth)
        pygame.draw.line(self.surface, rgb_hlight(bg, -hlight), (self.size[0]-lwidth, lwidth), (self.size[0]-lwidth, self.size[1]), lwidth)
        self.surface.blit(self.textsurf, (lwidth, lwidth))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        if self.isDrawn: return []
        self.isDrawn = True
        screen.blit(self.surface, (self.x, self.y))
        return [self.rect]

    def on_mouse_event(self, event, pos, pressed):
        if event.type == pygame.MOUSEMOTION:
            x, y = pos
            if self.rect.collidepoint(x, y) ^ (not self.isHover): return
            self.isHover = not self.isHover
            self.redraw(self.hoverbg if self.isHover else self.bg)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pressed[0]:
                x, y = pos
                if self.rect.collidepoint(x, y): self.isDown = True
        elif event.type == pygame.MOUSEBUTTONUP and self.isDown:
            if not pressed[0]:
                self.isDown = False
                x, y = pos
                if self.rect.collidepoint(x, y): return self.click()
        return None
    def on_animate(self, elapsed): pass
    def click(self): return None



class ButtonBox:
    def __init__(self, img_path, rect):
        self.isClicked = False
        self.rect = pygame.Rect(rect)
        self.img = img_path

    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def update(self):
        if sizeBox.size != '':
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


# Global Variables
numBars = 0
delay = 0
sorting = False
paused = False
timer_space_bar = 0

# Input Boxes
space = 200
algorithmBox = options(pygame.Rect((w // 4), (h - 60), line_thickness * 30, line_thickness * 10))
delayBox = Slider(pygame.Rect((w // 4) + space, (h - 60), line_thickness * 25, line_thickness * 10))
sizeBox = SizeField(pygame.Rect( (w // 4) + space + space, (h - 60), line_thickness, line_thickness * 10))  # x,y , w, h
exit_img = pygame.image.load('./images/stop_Button.png').convert_alpha()

playButton = ButtonBox(pygame.image.load('./images/playButton.png'), (pygame.Rect( (w // 4) + space + space + space//2, (h - 60), line_thickness * 10, line_thickness * 10)))
stopButton = ButtonBox(pygame.image.load('./images/stop_Button.png'), (pygame.Rect( (w // 4) + space + space + space//2, (h - 60), line_thickness * 10, line_thickness * 10)))


