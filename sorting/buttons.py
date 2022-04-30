import pygame

#from Colors import colors

pygame.init()

# Display settings
w , h = 900,500

windowSize = (w, h)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Sorting Algorithms Visualizer')

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
