import sys
import random
from collections import deque
import pygame as pg
pg.init()

size = width, height = 1000, 720
speed = [0, 0]
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (241, 252, 25)
blue = (0, 106, 255)
red = (237, 64, 64)
clock = pg.time.Clock()
game_over = False

screen = pg.display.set_mode(size)

def random_location():
    x = random.randint(0, 49) * 20
    y = random.randint(0, 35) * 20
    return (x, y)

def fruit_center():
    (x,y) = random_location()
    x += 10
    y += 10
    center = (x, y)
    return center

snakeRects = deque()
# Rect(left, top, width, height) -> Rect
snakeRects.append(pg.Rect(random_location(), (20, 20)))

center = fruit_center()
# circle(surface, color, center, radius) -> Rect
fruit = pg.draw.circle(screen, yellow, center, 10)

while 1:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: sys.exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_q: sys.exit()
        if not game_over:
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT and speed != [-20, 0]:
                speed = [20, 0]
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT and speed != [20, 0]:
                speed = [-20, 0]
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN and speed != [0, -20]:
                speed = [0, 20]
            elif event.type == pg.KEYDOWN and event.key == pg.K_UP and speed != [0, 20]:
                speed = [0, -20]
        
    
    snakeRect = snakeRects[0].move(speed)  # this is just for convenience (snakeRect is the head of the snake)
    # Move the snake by adding the new head and deleting the tail
    snake_tail = snakeRects.pop()

    for square in snakeRects:
        if pg.Rect.colliderect(snakeRect, square):
            game_over = True
            speed = [0, 0]

    snakeRects.appendleft(snakeRect)    

    if snakeRect.left < 0 or snakeRect.right > width:
        game_over = True
        speed = [0, 0]
    if snakeRect.top < 0 or snakeRect.bottom > height:
        game_over = True
        speed = [0, 0]

    # If the snake eats a fruit:
    if pg.Rect.colliderect(snakeRect, fruit):
        center = fruit_center()
        snakeRects.append(snake_tail)

    screen.fill(black)
    fruit = pg.draw.circle(screen, yellow, center, 10)

    # for every rectangle in snakeRects
    for snake in snakeRects:
        pg.draw.rect(screen, blue, snake, 0, 0)
    if game_over == True:
        pg.draw.rect(screen, red, snakeRect, 0, 0)
        
    pg.display.flip()