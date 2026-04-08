## Here we'll import the necessary libraries and modules for our application
import pygame
from extensions.start import start
from extensions.game import game

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
title = "SpaceInvaders"
pygame.display.set_caption(title)
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    start(screen)

    gameIsStarting = False
    Keys = pygame.key.get_pressed()
    if any(Keys) and not gameIsStarting:
        gameIsStarting = True
        game(screen)
        # Here you can add code to transition to the game state or start the game

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()