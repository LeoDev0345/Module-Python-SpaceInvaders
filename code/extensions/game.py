import pygame
from classes.player import Player
from extensions.aliensPosition import aliensPosition, updateAliensPosition
from classes.bullet import BulletPlayer
from classes.life import Life
from classes.bonus import Bonus
from random import randint
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
SHOOTING_SOUND_PATH = ASSETS_DIR / "sound-effects" / "shooting-sound-effect.mp3"

def game(screen):
    loading(screen)
    SHOOTING_BONUS_DURATION = 3000
    PROTECT_BONUS_DURATION = 5000

    score = 0
    player = Player()
    alien_positions = aliensPosition()
    alien_direction = "right"
    screen.fill("black")
    start_shoot_time = 0
    start_protect_time = 0
    bonus_list = []
    shooting_sound = pygame.mixer.Sound(SHOOTING_SOUND_PATH)

    # on dessine le joueur, les coeurs et les aliens
    # joueur
    player.draw(screen)
    print(player.life)
    #aliens
    for row in alien_positions:
        for alien in row:
            alien.draw(screen)

    lifeList = []
    for i in range(player.life):
        heart = Life(10 + i * 40, 50)
        lifeList.append(heart)

    for heart in lifeList:
        heart.draw(screen)

    pygame.display.flip()
    GAME_RUNNING = True
    
    clock = pygame.time.Clock()
    bullets = []
    alienBullets = []
    level = 1
    
    last_shot_time = 0
    
    while GAME_RUNNING:
        ## Gestion des événements
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_RUNNING = False
                pygame.quit()
                exit()

        if (current_time - start_shoot_time >= SHOOTING_BONUS_DURATION):
            start_shoot_time = 0
            player.unshoot()

        if (current_time - start_protect_time >= PROTECT_BONUS_DURATION):
            start_protect_time = 0
            player.unprotect()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        if keys[pygame.K_SPACE]:
            if current_time - last_shot_time >= player.cool_down:
                shooting_sound.play()
                bullets.append(BulletPlayer(player.x + 40 - 2.5, player.y))  # Centrer la balle
                last_shot_time = current_time

        ## Mise à jour de l'affichage
        screen.fill("black")

        font = pygame.font.SysFont("Arial", 24)
        text_surface = font.render(f"Score: {score}", True, (255, 255, 255))

        screen.blit(text_surface, (10, 10))

        player.draw(screen)

        left_edge = alien_positions[0][0].x
        right_edge = alien_positions[0][-1].x + 40

        ## Mise à jour de la position des aliens et du sens de déplacement
        if alien_direction == "right":
            if right_edge >= screen.get_width():
                alien_direction = "left"
            else:
                alien_positions = updateAliensPosition(alien_positions, "right", level)
        else:
            if left_edge <= 0:
                alien_direction = "right"
            else:
                alien_positions = updateAliensPosition(alien_positions, "left", level)

        ## Dessin des aliens
        for row in alien_positions:
            for alien in row:
                alien.draw(screen)

                if alien.collides_with(player) :
                    GAME_RUNNING = False
                    break
        
        ## Mise à jour des balles
        for bullet in bullets[:]:
            bullet.move()

            ## Vérification des collisions entre les balles et les aliens
            for row in alien_positions:
                for alien in row:
                    if alien.isAlive and bullet.collides_with(alien):
                        alien.isAlive = False
                        bullets.remove(bullet)
                        score += alien.pointByKill

                        bonus_chance = randint(1, 100)
                        if bonus_chance <= 5:  # 10% de chance d'obtenir un bonus
                            if bonus_chance % 2 == 0:
                                bonus_list.append(Bonus(alien.x, alien.y, "protect"))
                            else:
                                bonus_list.append(Bonus(alien.x, alien.y, "shoot"))
                        break

            bullet.draw(screen)
            if bullet.y < 0:
                bullets.remove(bullet)

        ## Dessin des bonus
        for bonus in bonus_list[:]:
            bonus.move()
            bonus.draw(screen)

            if bonus.collides_with(player):
                if bonus.type == "protect":
                    start_protect_time = current_time
                    player.protect()
                elif bonus.type == "shoot":
                    start_shoot_time = current_time
                    player.shoot()
                bonus_list.remove(bonus)
            

            if bonus.y > screen.get_height():
                bonus_list.remove(bonus)

        ## Tir aléatoire des aliens
        choice = randint(1, 100)
        if choice <= 1 * level:
            alien_row = randint(0, len(alien_positions) - 1)
            alien_col = randint(0, len(alien_positions[0]) - 1)
            alien = alien_positions[alien_row][alien_col]
            if alien.isAlive:
                alienBullets.append(alien.shoot())

        ## Mise à jour des bullets aliens
        for bullet in alienBullets[:]:
            bullet.move()

            ## Gestion de la collision entre les balles aliens et le joueur
            if bullet.collides_with(player):
                if start_protect_time != 0:
                    alienBullets.remove(bullet)
                    pass
                else:
                    player.life -= 1
                    alienBullets.remove(bullet)
                    break


            bullet.draw(screen)
            if bullet.y > screen.get_height():
                alienBullets.remove(bullet)

        ## Vérification de la vie du joueur
        if player.life <= 0:
            GAME_RUNNING = False
        else :
            lifeList = []
            for i in range(player.life):
                heart = Life(640 - 40 - i * 40, 20)
                lifeList.append(heart)

            for heart in lifeList:
                heart.draw(screen)
        
        ## Vérification du score pour passer au niveau suivant
        if (level * 800 == score):
            level += 1
            start_protect_time = 0
            start_shoot_time = 0
            bullets = []
            alienBullets = []
            bonus_list = []
            loading(screen, level)
            alien_positions = aliensPosition()

        pygame.display.flip()
        clock.tick(60)
    
    loose(screen, score)

def loading(screen, level=1):
    screen.fill("blue")

    timer = 3
    font = pygame.font.SysFont("Arial", 36)
    timer_text = font.render(f"Le niveau {level} démarre dans: {timer}", True, (255, 255, 255))
    timer_rect = timer_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    for i in range(timer, 0, -1):
        timer_text = font.render(f"Le niveau {level} démarre dans : {i}", True, (255, 255, 255))
        screen.fill("darkblue")
        screen.blit(timer_text, timer_rect)
        pygame.display.flip()
        pygame.time.delay(1000)

    go_text = font.render("C'est parti !", True, (255, 255, 255))
    go_rect = go_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.fill("darkblue")
    screen.blit(go_text, go_rect)
    pygame.display.flip()
    pygame.time.delay(1000)

def loose(screen, score):
    screen.fill("red")

    font = pygame.font.SysFont("Arial", 36)
    lose_text = font.render(f"Vous avez perdu ! Votre score : {score}", True, (255, 255, 255))
    lose_rect = lose_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    screen.blit(lose_text, lose_rect)
    pygame.display.flip()
    pygame.time.delay(3000)