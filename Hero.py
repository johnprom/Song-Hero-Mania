import pygame, sys
from pygame.locals import *
pygame.init()

def update():
    print("update")

def draw():
    print("draw")


if __name__ == "__main__":
    screen = pygame.display.set_mode((1440, 900))

    while True:
        update()
        draw()
        pygame.time.delay(16)
