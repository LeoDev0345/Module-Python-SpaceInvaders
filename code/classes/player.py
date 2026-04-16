import pygame
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
PLAYER_SPRITE_PATH = ASSETS_DIR / "player.png"

class Player:
    def __init__(self):
        self.sprite = pygame.image.load(PLAYER_SPRITE_PATH).convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, (40, 32))
        self.x = 300
        self.y = 620
        self.cool_down = 2

    def move_left(self, speed=5):
        if self.x > 0:  # On s'assure que le joueur ne sors pas de l'écran
            self.x -= speed

    def move_right(self, speed=5):
        if self.x < 640 - 40:  # On s'assure que le joueur ne sors pas de l'écran
            self.x += speed

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
