import pygame
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
PLAYER_SPRITE_PATH = ASSETS_DIR / "heart.png"

class Life :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(PLAYER_SPRITE_PATH)
        self.image = pygame.transform.smoothscale(self.image, (30, 30))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))