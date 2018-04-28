import pygame, sys
from pygame.locals import *

pygame.init()

# global variables
myfont = pygame.font.SysFont("monospace", 32)

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(0,0.0)

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
score = 0

# classes
class Note:
    tick = 0
    column = 0
    hit = False

# functions
def update():
    global tick_current
    tick_current += tick_rate/frame_rate


def draw():
    screen.fill(green)

    # draw text
    label = myfont.render (str(score), 1, (0, 0, 0))
    screen.blit(label, (100, 100))

    # draws hit location circles
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


def proccess_input(column):
    for note in notes:
        if not note.column == column:
            continue
        if note.hit == True:
            continue
        if abs(note.tick - tick_current)<=16:
            note.hit = True
            global score
            score += score_calulator(note.tick)
            print (score)


def score_calulator(note_tick):
    return 16-abs(note_tick - tick_current)


if __name__ == "__main__":

    init_notes()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == ord("x"):
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == ord("d"):
                proccess_input(0)
            elif event.type == pygame.KEYDOWN and event.key == ord("f"):
                proccess_input(1)
            elif event.type == pygame.KEYDOWN and event.key == ord("j"):
                proccess_input(2)
            elif event.type == pygame.KEYDOWN and event.key == ord("k"):
                proccess_input(3)

        update()
        draw()
        pygame.time.delay(int(1000 / frame_rate))
