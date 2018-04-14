import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1440, 900))

circle = pygame.image.load("circle.png")
circle = pygame.transform.scale(circle, (300, 300))
circlerect = circle.get_rect()

green = 0, 255, 0


def update():
    circlerect.x += 1


def draw():
    screen.fill(green)
    screen.blit(circle, circlerect)
    pygame.display.flip()


if __name__ == "__main__":

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == ord("x"):
                sys.exit()

        update()
        draw()
        pygame.time.delay(16)
