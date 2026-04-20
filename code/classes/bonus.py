import pygame
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
PROTECTED_SPRITE_PATH = ASSETS_DIR / "shield-bonus.png"
SHOOTING_SPRITE_PATH = ASSETS_DIR / "shooting-bonus.png"

class Bonus :
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        if self.type == "protect":
            self.sprite = pygame.image.load(PROTECTED_SPRITE_PATH).convert_alpha()
        elif self.type == "shoot":
            self.sprite = pygame.image.load(SHOOTING_SPRITE_PATH).convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, (40, 32))

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def move(self):
        self.y += 2

    def collides_with(self, player):
        player_rect = pygame.Rect(player.x, player.y, 80, 64)
        bonus_rect = pygame.Rect(self.x, self.y, 40, 32)
        return player_rect.colliderect(bonus_rect)