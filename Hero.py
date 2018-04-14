import pygame, sys
from pygame.locals import *
pygame.init()



def update():
    print("")

def draw():
    print("")


if __name__ == "__main__":
    screen = pygame.display.set_mode((1440, 900))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == ord("x"):
                sys.exit()

        update()
        draw()
        pygame.time.delay(16)
