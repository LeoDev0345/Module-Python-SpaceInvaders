import pygame
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
PLAYER_SPRITE_PATH = ASSETS_DIR / "player.png"

PROTECTED_PLAYER_SPRITE_PATH = ASSETS_DIR / "protected-player.png"

class Player:
    def __init__(self):
        self.sprite = pygame.image.load(PLAYER_SPRITE_PATH).convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, (80, 64))
        self.x = 300
        self.y = 620
        self.cool_down = 500
        self.life = 3

    def move_left(self, speed=5):
        if self.x > 0:  # On s'assure que le joueur ne sors pas de l'écran
            self.x -= speed

    def move_right(self, speed=5):
        if self.x < 640 - 80:  # On s'assure que le joueur ne sors pas de l'écran
            self.x += speed

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def protect(self):
        self.sprite = pygame.image.load(PROTECTED_PLAYER_SPRITE_PATH).convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, (80, 64))

    
    def unprotect(self):
        self.sprite = pygame.image.load(PLAYER_SPRITE_PATH).convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, (80, 64))

    def shoot(self):
        self.cool_down = 100

    def unshoot(self):
        self.cool_down = 500