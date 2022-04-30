import pygame

#from Colors import colors

pygame.init()

# Display settings
w , h = 900,500

windowSize = (w, h)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Sorting Algorithms Visualizer')


def get_font(size):  # Returns Press-Start-2P in the desired size
    #return pygame.font.Font('./images/font.ttf', size)
    return pygame.font.SysFont('./images/font.ttf', size)
# Font
baseFont = get_font(24)
#
line_thickness = 5


class SizeField:
    def __init__(self, rect):
        self.hover = False
        self.rect = rect
        self.size = '1'
        self.max_size = 1000

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
            if int(self.size) > 9:
                if event.key == pygame.K_BACKSPACE:
                    self.size = self.size[:-1]
            if int(self.size) < self.max_size:
                if event.unicode.isdigit():
                    self.size += event.unicode


class Slider:
    def __init__(self, rect):
        self.hover = False
        self.rect = rect
        self.speed = self.rect.x + line_thickness

    def draw(self):
        """Draw the slider"""
        screen.blit(baseFont.render("Speed", True, colors['BLACK']),
                    (self.rect.x + self.rect.w // 2, self.rect.y - self.rect.h // 2))
        self.rect.w += 1
        pygame.draw.rect(screen, colors['BLACK'], self.rect, line_thickness)
        self.rect.w -= 1
        pygame.draw.line(screen, colors['BLACK'], (self.rect.x + line_thickness, self.rect.y + self.rect.h // 2),
                         (self.rect.x + self.rect.w - line_thickness, self.rect.y + self.rect.h // 2),
                         line_thickness // 2)
        pygame.draw.line(screen, colors['BLACK'], (self.speed, self.rect.y + line_thickness),
                         (self.speed, self.rect.y + self.rect.h - line_thickness), line_thickness * 2)

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
                if (self.rect.x + line_thickness) <= self.mousePos[0] and self.mousePos[0] <= (
                        self.rect.x + self.rect.w - line_thickness):
                    self.speed = self.mousePos[0]
