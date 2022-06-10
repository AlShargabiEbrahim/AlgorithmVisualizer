from buttons import *


def renderBottomMenu():
    """"Draw the menu"""
    sizeBox.draw()
    delayBox.draw()
    algorithmBox.draw()
    if sorting:
        stopButton.draw()
    else:
        playButton.draw()


def updateWidgets(event):
    """"Update the menu"""
    sizeBox.update(event)
    delayBox.update(event)
    algorithmBox.update()
    if sorting:
        stopButton.update()
    else:
        playButton.update()


def renderTheBars(array, PURPLE_1, PURPLE_2, TEAL_1, TEAL_2, sorted={}):
    """render the bars and their sizes and colors"""
    if numBars != 0:
        bar_width = 900 / numBars
        ceil_width = ceil(bar_width)

        for num in range(numBars):
            if num in (PURPLE_1, PURPLE_2):
                color = colors['PURPLE']
            elif num in (TEAL_1, TEAL_2):
                color = colors['TEAL']
            elif num in sorted:
                color = colors['YELLOW']
                # pass
            else:
                color = colors["BLUE"]
            pygame.draw.rect(screen, color, (num * bar_width, algorithmBox.rect.y//1.1 - array[num], ceil_width, array[num]))


def render(array, PURPLE_1, PURPLE_2, TEAL_1, TEAL_2, **kwargs):
    """render the window"""
    screen.fill(colors["WHITE"])
    renderTheBars(array, PURPLE_1, PURPLE_2, TEAL_1, TEAL_2, **kwargs)
    renderBottomMenu()
    pygame.display.update()

