import pygame
def start_game():
    start= True
    while start:
        for i in pygame.event.get():
            if i.type == pygame.quit:
                start= false
        pygame.display.update()
    paygame.quit()
pygame.init()
screen = pygame.display.set_mode([600, 600])
first = pygame.draw.rect(screen, (255,255,255), (25,25,150,150))
second = pygame.draw.rect(screen, (255,255,255), (200,25,150,150))
third = pygame.draw.rect(screen, (255,255,255), (375,25,150,150))
fourth = pygame.draw.rect(screen, (255,255,255), (25,200,150,150))
fifth = pygame.draw.rect(screen, (255,255,255), (200,200,150,150))
sixth = pygame.draw.rect(screen, (255,255,255), (375,200,150,150))
seventh = pygame.draw.rect(screen, (255,255,255), (25,375,150,150))
eighth = pygame.draw.rect(screen, (255,255,255), (200,375,150,150))
ninth = pygame.draw.rect(screen, (255,255,255), (375,375,150,150))
pygame.display.set_caption("Tic Tac Toe")
start_game()


