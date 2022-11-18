import random
import pygame

class Figure():
    def __init__(self) -> None:
        self.dx = 0
        self.dy = 0
        self.color = "red"

class Ball(Figure):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.r = 0
    
    def update(self, dt):
        self.x += self.x + self.dx * dt
        self.y += self.y + self.dy * dt

    def collide(self, w, h):
        if self.x >= w-self.r/2 or self.x <= self.r/2:
            self.dx = -self.dx
            self.dy = self.dy + random.uniform(-1,1)
            
        if self.y >= h-self.r/2 or self.y <= self.r/2:
            self.dy = -self.dy
            self.dx = self.dx + random.uniform(-1,1)

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.r)

class Rectangle(Figure):
    def __init__(self) -> None:
        super().__init__()
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.w = 0

    def update(self, dt):
        self.x1 += self.x1 + self.dx * dt
        self.y1 += self.y1 + self.dy * dt
        self.x2 += self.x2 + self.dx * dt
        self.y2 += self.y2 + self.dy * dt

    def collide(self, w, h):
        if self.x1 >= w or self.x2 <= 0:
            self.dx = -self.dx
            self.dy = self.dy + random.uniform(-1,1)
            
        if self.y1 >= h or self.y2 <= 0:
            self.dy = -self.dy
            self.dx = self.dx + random.uniform(-1,1)

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, [self.x1, self.x2, self.y1, self.y2])