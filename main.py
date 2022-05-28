import pygame
import pygame.gfxdraw
import sys
from random import randint


def get_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def spreadfire():
    for x in range(0,WIDTH):
        for y in range(1,HEIGHT):
            rand = randint(0,2)
            ran2 = randint(0,3)
            if ran2 != 1:
                ran2 = 0
            frm = y * WIDTH + x + ran2
            to = frm - WIDTH
            if FIREPIXELS[frm] >= rand:
                FIREPIXELS[to] = FIREPIXELS[frm] - rand 

def draw():
    spreadfire()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = colors[FIREPIXELS[y * WIDTH + x]]
            pygame.gfxdraw.pixel(display, x,y, color)


WIDTH=500
HEIGHT=100
FPS=0

FIREPIXELS = [ 0 for i in range(WIDTH * HEIGHT) ]

colors = [
    (7, 7, 7),          (31, 7, 7),         (47, 15, 7),
    (71, 15, 7),        (87, 23, 7),        (103, 31, 7),
    (119, 31, 7),       (143, 39, 7),       (159, 47, 7),
    (175, 63, 7),       (191, 71, 7),       (199, 71, 7),
    (223, 79, 7),       (223, 87, 7),       (223, 87, 7),
    (215, 95, 7),       (215, 95, 7),       (215, 103, 15),
    (207, 111, 15),     (207, 119, 15),     (207, 127, 15),
    (207, 135, 23),     (199, 135, 23),     (199, 143, 23),
    (199, 151, 31),     (191, 159, 31),     (191, 159, 31),
    (191, 167, 39),     (191, 167, 39),     (191, 175, 47),
    (183, 175, 47),     (183, 183, 47),     (183, 183, 55),
    (207, 207, 111),    (223, 223, 159),    (239, 239, 199)
]

for i in range(WIDTH):
    FIREPIXELS[i + (WIDTH * HEIGHT - WIDTH)] = 35


display = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
while True:
    draw()
    clock.tick(FPS)
    get_events()
    pygame.display.update()
