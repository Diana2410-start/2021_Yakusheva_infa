import pygame
from pygame.draw import *
from random import randint
import math

pygame.init()

FPS = 40
screen = pygame.display.set_mode((1200, 900))  # создаём экран

pygame.display.set_caption("")  # создаем название

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]  # массив из цветов для шарика
SPEED_X = randint(-10, 10)
SPEED_Y = randint(-20, 20)

x = randint(100, 1100)
y = randint(100, 800)
r = randint(30, 50)
color = COLORS[randint(0, 5)]
ball = circle(screen, color, (x, y), r)


def new_ball():
    """
    рисует новый шарик
    :return:
    """
    global x, y, r, SPEED_X, SPEED_Y
    x += SPEED_X
    y += SPEED_Y
    screen.fill(BLACK)
    license()
    ball = circle(screen, color, (x, y), r)

    if ball.topleft[0] <= 0 or ball.bottomright[0] >= 1200:
        SPEED_X = -SPEED_X

    if ball.topleft[1] <= 0 or ball.bottomright[1] >= 900:
        SPEED_Y = -SPEED_Y


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    new_ball()

    pygame.display.update()
screen.fill(BLACK)

pygame.quit()
