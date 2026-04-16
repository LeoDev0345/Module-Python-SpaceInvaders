import pygame
from classes.bullet import BulletAlien


class Alien:

    def __init__(self, spriteFile, pointByKill, x = None, y = None, isAlive = True):
        self.sprite = pygame.image.load(spriteFile).convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, (40, 32))

        self.pointByKill = pointByKill
        self.x = x if x is not None else 0
        self.isAlive = isAlive
        self.y = y if y is not None else 0

    def draw(self, screen):
        if self.isAlive:
            screen.blit(self.sprite, (self.x, self.y))

    def shoot(self):
        return BulletAlien(self.x + self.sprite.get_width() // 2, self.y + self.sprite.get_height())