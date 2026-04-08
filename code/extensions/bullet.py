import pygame

class Bullet :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 15
        self.image = pygame.Surface((5, 10))
        self.image.fill("white")
    
    def move(self):
        self.y -= self.speed
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))