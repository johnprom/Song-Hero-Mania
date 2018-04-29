import pygame, sys
from pygame.locals import *

pygame.init()

icon = pygame.image.load('yellowcircle.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Song Hero Mania')


# global variables
myfont = pygame.font.SysFont("monospace", 64)

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(0,0.0)

screen = pygame.display.set_mode((1440, 900))

circle0 = pygame.image.load("redcircle.png")
circle0 = pygame.transform.scale(circle0, (100, 100))
circle1 = pygame.image.load("yellowcircle.png")
circle1 = pygame.transform.scale(circle1, (100, 100))
circle2 = pygame.image.load("bluecircle.png")
circle2 = pygame.transform.scale(circle2, (100, 100))
circle3 = pygame.image.load("greencircle.png")
circle3 = pygame.transform.scale(circle3, (100, 100))
circle_hit_box = pygame.image.load("whitecircle.png")
circle_hit_box = pygame.transform.scale(circle_hit_box, (110, 110))
circle_rect = circle0.get_rect()

green = 0, 0, 0
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
    def __init__(self, tick, column):
        self.tick = tick
        self.column = column


# functions
def update():
    global tick_current
    tick_current += tick_rate/frame_rate


def draw():
    screen.fill(green)

    for note in notes:
        x = 350 + 200 * note.column
        y = 600 + (-1 * note.tick + tick_current) * scroll_speed
        circle_rect.x = x
        circle_rect.y = y
        if note.column == 0:
            screen.blit(circle0, circle_rect)
        elif note.column == 1:
            screen.blit(circle1, circle_rect)
        elif note.column == 2:
            screen.blit(circle2, circle_rect)
        elif note.column == 3:
            screen.blit(circle3, circle_rect)

    # draw score
    label = myfont.render("Score - " + str(int(score)), 1, (255, 255, 255))
    screen.blit(label, (510, 150))

    # draws hit location circles
    for i in range(0, 4):
        circle_rect.x = 345 + 200 * i
        circle_rect.y = 600
        screen.blit(circle_hit_box, circle_rect)

    pygame.display.flip()


def init_notes():
    notes.append(Note(100, 1))
    notes.append(Note(200, 2))
    notes.append(Note(300, 3))

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

def restart_game():
    notes.clear()
    init_notes()
    global tick_current
    tick_current = 0
    global score
    score = 0
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(0, 0.0)



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
            elif event.type == pygame.KEYDOWN and event.key == ord("r"):
                restart_game()

        update()
        draw()
        pygame.time.delay(int(1000 / frame_rate))
