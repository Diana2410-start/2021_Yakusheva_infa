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

# значеия для функции new_ball()
sp_x = randint(-10, 10)
sp_y = randint(-10, 10)
x = randint(100, 1100)
y = randint(100, 800)
r = randint(30, 50)
color = COLORS[randint(0, 5)]
ball = circle(screen, color, (x, y), r)

# значеия для функции new_ball_1()
sp_x1 = randint(-10, 10)
sp_y1 = randint(-10, 10)
x1 = randint(100, 1100)
y1 = randint(100, 800)
r1 = randint(30, 50)
color1 = COLORS[randint(0, 5)]
ball_1 = circle(screen, color1, (x1, y1), r1)

q = 0
w = 0

# значения для функции new_square()
sp_xxx = 60
sp_yyy = 3
xxx = randint(100, 1100)
yyy = randint(100, 800)
rrr = randint(30, 50)
color_0 = COLORS[randint(0, 5)]
square = pygame.draw.rect(screen, color_0, (xxx, yyy, rrr, rrr))


def new_ball():
    global x, y, r, color, sp_x, sp_y
    x += sp_x
    y += sp_y
    screen.fill(BLACK)
    license()
    ball = circle(screen, color, (x, y), r)

    if ball.topleft[0] <= 0 or ball.bottomright[0] >= 1200:
        sp_x = -sp_x

    if ball.topleft[1] <= 0 or ball.bottomright[1] >= 900:
        sp_y = -sp_y

    pygame.display.update()


def new_ball_1():
    global x1, y1, r1, color1, sp_x1, sp_y1
    x1 += sp_x1
    y1 += sp_y1
    screen.fill(BLACK)
    license()
    ball_1 = circle(screen, color1, (x1, y1), r1)

    if ball_1.topleft[0] <= 0 or ball_1.bottomright[0] >= 1200:
        sp_x1 = -sp_x1

    if ball_1.topleft[1] <= 0 or ball_1.bottomright[1] >= 900:
        sp_y1 = -sp_y1

    pygame.display.update()


def click_ball():
    global q, x0, y0
    dx_1 = x0 - x
    dy_1 = y0 - y
    dr_1 = math.sqrt(dx_1 ** 2 + dy_1 ** 2)
    dx_2 = x0 - x1
    dy_2 = y0 - y1
    dr_2 = math.sqrt(dx_2 ** 2 + dy_2 ** 2)
    if dr_1 <= r or dr_2 <= r1:
        q = q + 1
        print('scores ball', q)


def click_square():
    global w, x00, y00
    dx_square = x00 - xxx
    dy_square = y00 - yyy
    if dx_square <= rrr and dy_square <= rrr:
        w = w + 5
        print('scores square', w)


def new_square():
    global xxx, yyy, rrr, sp_xxx, sp_yyy
    xxx += sp_xxx
    yyy += math.sin(xxx * math.pi / 180)
    license()
    square = pygame.draw.rect(screen, color_0, (xxx, yyy, rrr, rrr))
    if square.topleft[0] <= 0 or square.bottomright[0] >= 1200:
        sp_xxx = -sp_xxx

    if square.topleft[1] <= 0 or square.bottomright[1] >= 900:
        sp_yyy = -sp_yyy

    pygame.display.update()


def scores():
    global l
    l = q + w
    print('scores end:', l)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = pygame.mouse.get_pos()
            click_ball()
            x00, y00 = pygame.mouse.get_pos()
            click_square()
    new_ball()
    new_ball_1()
    new_square()
    scores()
    pygame.display.update()

screen.fill(BLACK)

pygame.quit()
