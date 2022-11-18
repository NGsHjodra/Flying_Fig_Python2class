import random
import pygame

class Figure():
    def __init__(self) -> None:
        self.dx = 0
        self.dy = 0
        self.x = 0
        self.y = 0
        self.color = "red"

    def update(self, dt):
        self.x +=  self.dx * dt
        self.y +=  self.dy * dt

class Ball(Figure):
    def __init__(self) -> None:
        super().__init__()
        self.r = 0

    def collide(self, w, h):
        if self.x+self.r/2 >= w or self.x-self.r/2 <= 0:
            self.dx = -self.dx
            self.dy = self.dy + random.uniform(-0.1,0.1)
            
        if self.y+self.r/2 >= h or self.y-self.r/2 <= 0:
            self.dy = -self.dy
            self.dx = self.dx + random.uniform(-0.1,0.1)

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.r)

class Rectangle(Figure):
    def __init__(self) -> None:
        super().__init__()
        self.w = 0
        self.h = 0

    def collide(self, w, h):
        if self.x+self.w >= w or self.x <= 0:
            self.dx = -self.dx
            self.dy = self.dy + random.uniform(-0.1,0.1)
            
        if self.y+self.h >= h or self.y <= 0:
            self.dy = -self.dy
            self.dx = self.dx + random.uniform(-0.1,0.1)

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, [self.x, self.y, self.w, self.h])