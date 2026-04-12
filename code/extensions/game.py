import pygame
from classes.player import Player
from classes.alien import Alien
from extensions.bullet import Bullet

def game(screen):
    loading(screen)

    player = Player()
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()
    GAME_RUNNING = True
    
    clock = pygame.time.Clock()
    bullets = []
    
    last_shot_time = 0
    cooldown_duration = 500
    
    while GAME_RUNNING:
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
                bullets.append(Bullet(player.x + 20 - 2.5, player.y))  # Centrer la balle
                last_shot_time = current_time
            

        screen.fill("black")
        player.draw(screen)
        
        for bullet in bullets[:]:
            bullet.move()
            bullet.draw(screen)
            if bullet.y < 0:
                bullets.remove(bullet)
                
        pygame.display.flip()
        clock.tick(60)
        

def loading(screen):
    screen.fill("blue")

    timer = 3
    font = pygame.font.SysFont("Arial", 48)
    timer_text = font.render(f"Le jeu démarre dans: {timer}", True, (255, 255, 255))
    timer_rect = timer_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    for i in range(timer, 0, -1):
        timer_text = font.render(f"Le jeu démarre dans: {i}", True, (255, 255, 255))
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

