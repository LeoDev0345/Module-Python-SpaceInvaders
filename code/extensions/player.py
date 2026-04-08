import pygame
from pathlib import Path
from extensions.bullet import Bullet

ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
PLAYER_SPRITE_PATH = ASSETS_DIR / "player.png"

class Player:
    def __init__(self):
        self.sprite = pygame.image.load(PLAYER_SPRITE_PATH).convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, (80, 64))
        self.x = 640
        self.y = 620
        self.cool_down = 2

    def move_left(self, speed=5):
        if self.x > 0:  # Ensure the player doesn't move off the left edge
            self.x -= speed

    def move_right(self, speed=5):
        if self.x < 1280 - 80:  # Ensure the player doesn't move off the right edge
            self.x += speed

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def shoot(self, bullets):
        bullet = Bullet(self.x + 40 - 2.5, self.y)  # Center the bullet on the player
        bullets.append(bullet)