import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1440, 900))

circle = pygame.image.load("circle.png")
circle = pygame.transform.scale(circle, (100, 100))
circle_rect = circle.get_rect()

green = 0, 255, 0
scroll_speed = 5

notes = []

tick_current = 0
tick_rate = 60
frame_rate = 60


class Note:
    tick = 0
    column = 0
    hit = False


def update():
    global tick_current
    tick_current += tick_rate/frame_rate


def draw():
    screen.fill(green)

    # temp
    for i in range(0, 4):
        circle_rect.x = 350 + 200 * i
        circle_rect.y = 600
        screen.blit(circle, circle_rect)

    for note in notes:
        x = 350 + 200 * note.column
        y = 600 + (-1 * note.tick + tick_current) * scroll_speed
        circle_rect.x = x
        circle_rect.y = y
        screen.blit(circle, circle_rect)

    pygame.display.flip()


def init_notes():
    note1 = Note()
    note1.column = 3
    note1.tick = 600
    notes.append(note1)

    note2 = Note()
    note2.column = 2
    note2.tick = 450
    notes.append(note2)

    note3 = Note()
    note3.column = 1
    note3.tick = 200
    notes.append(note3)

    note4 = Note()
    note4.column = 0
    note4.tick = 500
    notes.append(note4)


if __name__ == "__main__":

    init_notes()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == ord("x"):
                sys.exit()

        update()
        draw()
        pygame.time.delay(int(1000 / frame_rate))
