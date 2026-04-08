import pygame
from extensions.player import Player

def game(screen):
    loading(screen)

    player = Player()
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()
    GAME_RUNNING = True
    
    clock = pygame.time.Clock()
    
    while GAME_RUNNING:
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
            
        screen.fill("black")
        player.draw(screen)
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

    