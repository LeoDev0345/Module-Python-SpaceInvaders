import pygame
from classes.alien import Alien

def aliensPosition():
    alienPositions = [
        [],
        [],
        [],
        [],
    ]

    for i in range(len(alienPositions)):
        if (i == 0):
            spriteFile = "assets/red.png"
            pointByKill = 30
        elif (i == 1 or i == 2):
            spriteFile = "assets/green.png"
            pointByKill = 20
        else:
            spriteFile = "assets/yellow.png"
            pointByKill = 10
        for j in range(10):
            alienPositions[i].append(Alien(spriteFile, pointByKill, x=25 + j * 60, y=50 + i * 60))

    return alienPositions
    
def updateAliensPosition(alienPositions, side, level):
    if (side == "right"):
        for row in alienPositions:
            for alien in row:
                alien.x += 0.5  # Déplacer les aliens vers la droite
                alien.y += 0.05  # Déplacer les aliens vers le bas
    elif (side == "left"):
        for row in alienPositions:
            for alien in row:
                alien.x -= 0.5 * (1 + (level-1) * 5 / 100)  # Déplacer les aliens vers la gauche
                alien.y += 0.05 * (1 + (level-1) * 5 / 100) # Descendre les aliens vers le bas
    
    return alienPositions
