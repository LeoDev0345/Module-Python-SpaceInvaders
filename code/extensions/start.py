import pygame

def start(screen):
    font = pygame.font.SysFont("Arial", 48)
    title = font.render("Space Invaders", True, (255, 255, 255))
    title_rect = title.get_rect(center=(screen.get_width() // 2, screen.get_height() // 5))
    screen.blit(title, title_rect)
    font = pygame.font.SysFont("Arial", 24)
    instructions = font.render("Appuyez sur une touche pour commencer", True, (255, 255, 255))
    instructions_rect = instructions.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(instructions, instructions_rect)