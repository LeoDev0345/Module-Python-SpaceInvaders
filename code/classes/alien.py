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
    
    def collides_with(self, player):
        if not self.isAlive:
            return False
        alien_rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        player_rect = pygame.Rect(player.x, player.y, player.sprite.get_width(), player.sprite.get_height())
        return alien_rect.colliderect(player_rect)