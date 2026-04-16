import pygame

class BulletPlayer :
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

    def collides_with(self, alien):
        bullet_rect = self.image.get_rect(topleft=(self.x, self.y))
        alien_rect = alien.sprite.get_rect(topleft=(alien.x, alien.y))
        return bullet_rect.colliderect(alien_rect)
    
class BulletAlien :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.image = pygame.Surface((5, 10))
        self.image.fill("red")
    
    def move(self):
        self.y += self.speed
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collides_with(self, player):
        bullet_rect = self.image.get_rect(topleft=(self.x, self.y))
        player_rect = player.sprite.get_rect(topleft=(player.x, player.y))
        return bullet_rect.colliderect(player_rect) 