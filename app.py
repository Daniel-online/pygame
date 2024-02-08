import pygame
from sys import exit
pygame.init()

#propriedades da janela
width = 800
heigth = 400
screen = pygame.display.set_mode((width, heigth))
screen.fill('blue')

pygame.display.set_caption('Runner Game')
player_active = True

clock = pygame.time.Clock()



#player

player_heigth = 40
player_width = 40
player = pygame.Surface((player_width, player_heigth))
player.fill('Red')
#chão
test_width = 800
test_height = 160
test_surface = pygame.Surface((test_width, test_height))
test_surface.fill('green')
#loop de janela
while (player_active ):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(test_surface, (0,320))
    screen.blit(player, (10, 280))
    pygame.display.update()
    clock.tick(60)
