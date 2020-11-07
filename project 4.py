import pygame
def start_game():
    start= True
    while start:
        for i in pygame.event.get():
            if i.type == pygame.quit:
                start= false
        pygame.display.update()
    paygame.quit()
def game_board():
    screen = pygame.display.set_mode([500, 500])
    pygame.draw.rect(screen, (255, 255,255), [50, 20, 400, 450])
    pygame.draw.lines(screen, (0, 0, 0), True, [(100, 100), (400, 100)], 10)
    pygame.draw.lines(screen, (0, 0, 0), True, [(100, 170), (400, 170)], 10)
    pygame.draw.lines(screen, (0, 0, 0), True, [(100, 230), (400, 230)], 10)
    pygame.draw.lines(screen, (0, 0, 0), True, [(100, 300), (400, 300)], 10)
    pygame.draw.lines(screen, (0, 0, 0), True, [(100, 100), (100, 300)], 10)
    pygame.draw.lines(screen, (0, 0, 0), True, [(400, 100), (400, 300)], 10)
    pygame.draw.lines(screen, (0, 0, 0), True, [(200, 100), (200, 300)], 10)
    pygame.draw.lines(screen, (0, 0, 0), True, [(300, 100), (300, 300)], 10)
pygame.init()
start_game()
game_board()
