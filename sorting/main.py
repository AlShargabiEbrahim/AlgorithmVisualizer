import sys
import pygame
from random import randint
from time import time
from algs import algorithmsDict
import render


def sorting_visualizer():
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

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and render.sorting:
                render.finishedSorting = not render.finishedSorting
                render.timer_space_bar = time()

            render.updateWidgets(event)

        render.delay = (render.delayBox.speed-render.delayBox.rect.x-render.line_thickness)/1000

        if render.playButton.isClicked:
            render.playButton.isClicked = False
            render.sorting = True
            current_alg = render.algorithmBox.algorithms[0]
            render.numBars = int(render.sizeBox.size)
            array_to_be_sorted = [randint(render.smallers_val,render.highest_val) for i in range(render.numBars)]
            alg_iterator = algorithmsDict[current_alg](array_to_be_sorted, 0, render.numBars-1)

        if render.stopButton.isClicked:
            render.stopButton.isClicked = False
            render.sorting = False
            render.finishedSorting = False

            try:
                while True:
                    array_to_be_sorted,  PURPLE_1, PURPLE_2, TEAL_1, TEAL_2 = next(alg_iterator)
            except StopIteration:
                print("StopIteration error")

        if render.sorting and not render.finishedSorting:
            try:
                if time()-timer_delay >= render.delay:
                    array_to_be_sorted,  PURPLE_1, PURPLE_2, TEAL_1, TEAL_2 = next(alg_iterator)
                    render.render(array_to_be_sorted,  PURPLE_1, PURPLE_2, TEAL_1, TEAL_2)
                    timer_delay = time()
            except StopIteration:
                render.sorting = False
                print("StopIteration error")

        else:
            render.render(array_to_be_sorted, -1, -1, -1, -1, sorted=set(range(render.numBars)))


if __name__ == '__main__':
    sorting_visualizer()
