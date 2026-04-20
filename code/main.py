## Here we'll import the necessary libraries and modules for our application
import pygame
from extensions.start import start
from extensions.game import game

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 720))
title = "SpaceInvaders"
pygame.display.set_caption(title)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    start(screen)

    gameIsStarting = False
    Keys = pygame.key.get_pressed()
    if any(Keys) and not gameIsStarting:
        gameIsStarting = True
        game(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()