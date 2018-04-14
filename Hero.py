import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1440, 900))

circle = pygame.image.load("circle.png")
green = 0, 255, 0

def update():
    print("")

def draw():
    screen.fill(green)
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
