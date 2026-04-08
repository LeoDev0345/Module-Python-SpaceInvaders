## Here we'll import the necessary libraries and modules for our application
import pygame

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
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    # here we'll import the game logic and rendering code from our other files

pygame.quit()