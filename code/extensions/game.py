import pygame
from classes.player import Player
from extensions.aliensPosition import aliensPosition, updateAliensPosition
from classes.bullet import BulletPlayer

def game(screen):
    loading(screen)

    score = 0
    player = Player()
    alien_positions = aliensPosition()
    alien_direction = "right"
    screen.fill("black")

    # on dessine le joueur et les aliens
    # joueur
    player.draw(screen)

    #aliens
    for row in alien_positions:
        for alien in row:
            alien.draw(screen)

    pygame.display.flip()
    GAME_RUNNING = True
    
    clock = pygame.time.Clock()
    bullets = []
    level = 1
    
    last_shot_time = 0
    cooldown_duration = 500
    
    while GAME_RUNNING:
        ## Gestion des événements
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_RUNNING = False
                pygame.quit()
                exit()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        if keys[pygame.K_SPACE]:
            if current_time - last_shot_time >= cooldown_duration:
                bullets.append(BulletPlayer(player.x + 20 - 2.5, player.y))  # Centrer la balle
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
                alien_positions = updateAliensPosition(alien_positions, "right")
        else:
            if left_edge <= 0:
                alien_direction = "right"
            else:
                alien_positions = updateAliensPosition(alien_positions, "left")

        ## Dessin des aliens
        for row in alien_positions:
            for alien in row:
                alien.draw(screen)
        
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
                        break
                else:
                    continue
                break

            bullet.draw(screen)
            if bullet.y < 0:
                bullets.remove(bullet)

        
        if (level * 800 == score):
            level += 1
            loading(screen, level)
            alien_positions = aliensPosition()

        pygame.display.flip()
        clock.tick(60)
        

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
