import pygame
from pygame.draw import *
from random import randint
import math

pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))  # создаём экран

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]  # массив из цветов для шарика


q=0

def new_ball():
    """
    рисует новый шарик
    :return:
    """
    global x0, y0, r0
    x0 = randint(100, 1100)
    y0 = randint(100, 800)
    r0 = randint(30, 50)
    license()
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x0, y0), r0)



def click(x, y):
    global q
    dx = x - x0
    dy = y - y0
    r = math.sqrt(dx ** 2 + dy ** 2)
    print('Диапазон значений:', r)
    if r <= r0:
        q = q + 1
        print('scores', q)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            click(x, y)

    new_ball()


    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
