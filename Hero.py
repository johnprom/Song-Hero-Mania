import pygame, sys
from pygame.locals import *

pygame.init()

icon = pygame.image.load('yellowcircle.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Song Hero Mania')


# global variables
myfont = pygame.font.SysFont("monospace", 64)

screen = pygame.display.set_mode((1440, 900))

# circle textures
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
scroll_speed = 14

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

def draw_hitnotes():
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

def draw_hit_locations():
    for i in range(0, 4):
        circle_rect.x = 345 + 200 * i
        circle_rect.y = 600
        screen.blit(circle_hit_box, circle_rect)

def draw():
    screen.fill(green)
    draw_hitnotes()
    draw_hit_locations()

    # draw score
    label = myfont.render("Score - " + str(int(score)), 1, (255, 255, 255))
    screen.blit(label, (510, 150))

    pygame.display.flip()

# "song" notes
def init_notes():
    notes.append(Note(100, 3))
    notes.append(Note(120, 2))
    notes.append(Note(140, 1))
    notes.append(Note(160, 0))
    notes.append(Note(180, 1))
    notes.append(Note(200, 3))
    notes.append(Note(215, 2))
    notes.append(Note(230, 2))
    notes.append(Note(245, 2))
    notes.append(Note(260, 2))
    notes.append(Note(280, 3))
    notes.append(Note(300, 2))
    notes.append(Note(320, 1))
    notes.append(Note(340, 2))
    notes.append(Note(360, 1))
    notes.append(Note(375, 3))
    notes.append(Note(390, 2))
    notes.append(Note(415, 3))
    notes.append(Note(425, 3))
    notes.append(Note(435, 2))
    notes.append(Note(445, 3))
    notes.append(Note(455, 1))
    notes.append(Note(465, 2))
    notes.append(Note(475, 1))
    notes.append(Note(490, 0))
    notes.append(Note(505, 3))
    notes.append(Note(520, 2))
    notes.append(Note(535, 1))
    notes.append(Note(550, 2))
    notes.append(Note(565, 0))
    notes.append(Note(580, 3))
    notes.append(Note(595, 2))
    notes.append(Note(610, 3))
    notes.append(Note(625, 1))
    notes.append(Note(640, 2))
    notes.append(Note(650, 1))
    notes.append(Note(660, 0))
    notes.append(Note(670, 3))
    notes.append(Note(680, 2))
    notes.append(Note(690, 0))
    notes.append(Note(700, 3))
    notes.append(Note(725, 1))
    notes.append(Note(735, 1))
    notes.append(Note(770, 2))
    notes.append(Note(777, 2))
    notes.append(Note(784, 2))

# decides weather to award point
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

if __name__ == "__main__":

    init_notes()

    # get user key data
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
