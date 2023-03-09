import pygame
import GameObject


pygame.init()

backgroundImage_LvL1 = pygame.image.load('town.png')
backgroundImage_Lvl1_rect = backgroundImage_LvL1.get_rect()

screen = pygame.display.set_mode(
    (backgroundImage_Lvl1_rect.width, backgroundImage_Lvl1_rect.height))
screen_rect = screen.get_rect()

def renderLevel1(): 
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    pygame.display.flip()
def renderLvl2():
    pass
def renderBossLvl(): 
    pass
running = True
# gameloop
while running:
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    pygame.display.flip()
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
