import pygame
from Class import Ball,Rectangle
import random

#setup
pygame.init()
clock = pygame.time.Clock()
w = 600
h = 600
bg_color = 'green'
drawing_color = 'blue'
radius = 30

window_size = pygame.math.Vector2(w, h)
pygame.display.set_mode(window_size)

done = False

Figs = []

for i in range(6):
    ball = Ball()
    ball.x = w/2 + random.uniform(-5,5)
    ball.y = h/2 + random.uniform(-5,5)
    ball.r = random.randint(40,60)
    ball.dx = 0.5 + random.uniform(-0.1,0.1)
    ball.dy = 0.5 + random.uniform(-0.1,0.1)
    ball.color = random.choice(['red','blue','yellow'])
    Figs.append(ball)

for i in range(6):
    rect = Rectangle()
    rect.x = w/2 + random.uniform(-10, -5)
    rect.y = rect.x
    rect.w = 50 + random.randint(-10,10)
    rect.h = 50 + random.randint(-10,10)
    rect.dx = 0.5 + random.uniform(-0.4,0.4)
    rect.dy = 0.5 + random.uniform(-0.4,0.4)
    rect.color = random.choice(['red','blue','yellow'])
    Figs.append(rect)

while not done:

    dt = clock.tick(144)

    pygame.display.get_surface().fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True

    surf = pygame.display.get_surface()
    for fig in Figs:
        fig.draw(surf)
    pygame.display.flip()

    for fig in Figs:
        fig.update(dt)
        fig.collide(w, h)

pygame.quit()