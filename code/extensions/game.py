import pygame

def game(screen):
    loading(screen)

def loading(screen):
    screen.fill("blue")

    timer = 3
    font = pygame.font.SysFont("Arial", 48)
    timer_text = font.render(f"Game starts in: {timer}", True, (255, 255, 255))
    timer_rect = timer_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    for i in range(timer, 0, -1):
        timer_text = font.render(f"Game starts in: {i}", True, (255, 255, 255))
        screen.fill("darkblue")
        screen.blit(timer_text, timer_rect)
        pygame.display.flip()
        pygame.time.delay(1000)

    go_text = font.render("Go!", True, (255, 255, 255))
    go_rect = go_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.fill("darkblue")
    screen.blit(go_text, go_rect)
    pygame.display.flip()
    pygame.time.delay(1000)