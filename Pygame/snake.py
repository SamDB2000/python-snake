import sys, random
import pygame as pg
pg.init()

size = width, height = 1000, 750
speed = [0, 0]
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 106, 255)
clock = pg.time.Clock()

screen = pg.display.set_mode(size)

#ball = pg.image.load("intro_ball.gif")
#snakeRect = ball.get_rect()

def random_location():
    x = random.randint(0, 39) * 25
    y = random.randint(0, 29) * 25
    return (x, y)

# Rect(left, top, width, height) -> Rect
snakeRect = pg.Rect(random_location(), (25, 25))
# rect(screen, color, rect, width=0, border_radius=0)
snake = pg.draw.rect(screen, blue, snakeRect, 0)

while 1:
    clock.tick(6)
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: sys.exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_q: sys.exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            speed = [25, 0]
        elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            speed = [-25, 0]
        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            speed = [0, 25]
        elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
            speed = [0, -25]

    snakeRect = snakeRect.move(speed)

    if snakeRect.left < 0 or snakeRect.right > width:
        speed[0] = -speed[0]  # Change this to ending the game eventually
    if snakeRect.top < 0 or snakeRect.bottom > height:
        speed[1] = -speed[1]  # Change this to ending the game eventually

    screen.fill(black)
    snake = pg.draw.rect(screen, blue, snakeRect, 0, 0)
    pg.display.flip()