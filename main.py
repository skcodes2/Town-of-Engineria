import pygame
import GameObject

pygame.init()

backgroundImage_LvL1 = pygame.image.load('lvl1background.png')
backgroundImage_LvL2 = pygame.image.load("lvl2background.png")
backgroundImage_LvL3 = pygame.image.load("lvl3background.png")
backgroundImage_Lvl1_rect = backgroundImage_LvL1.get_rect()
backgroundImage_LvL2_rect = backgroundImage_LvL2.get_rect()
backgroundImage_LvL3_rect = backgroundImage_LvL3.get_rect()

screen = pygame.display.set_mode((backgroundImage_Lvl1_rect.width, backgroundImage_Lvl1_rect.height))
screen_rect = screen.get_rect()

def renderLevel1(): 
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    pygame.display.flip()
def renderLvl2():
    screen.blit(backgroundImage_LvL2, backgroundImage_LvL2_rect)
    pygame.display.flip()
def renderBossLvl(): 
    screen.blit(backgroundImage_LvL3, backgroundImage_LvL3_rect)
    pygame.display.flip()

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
