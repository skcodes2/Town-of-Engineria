import pygame
import GameObject

pygame.init()

backgroundImage_LvL1 = pygame.image.load('backgroundImages/lvl1background.png')
backgroundImage_LvL2 = pygame.image.load("backgroundImages/lvl2background.png")
backgroundImage_LvL3 = pygame.image.load("backgroundImages/lvl3background.png")
backgroundImage_Lvl1_rect = backgroundImage_LvL1.get_rect()
backgroundImage_LvL2_rect = backgroundImage_LvL2.get_rect()
backgroundImage_LvL3_rect = backgroundImage_LvL3.get_rect()

platForm_group = pygame.sprite.Group()
#floor platform 
platForm_group.add(GameObject.PlatForms(0, 500, "lvl1platformImages/largebrownstone.png"))
platForm_group.add(GameObject.PlatForms(324, 550, "lvl1platformImages/largebrownstone.png"))
platForm_group.add(GameObject.PlatForms(648, 550, "lvl1platformImages/largebrownstone.png"))
platForm_group.add(GameObject.PlatForms(972, 550, "lvl1platformImages/largebrownstone.png"))
#sky platforms
platForm_group.add(GameObject.PlatForms(987, 337, "lvl1platformImages/mediumorangestone.png"))
platForm_group.add(GameObject.PlatForms(300, 360, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group.add(GameObject.PlatForms(340, 360, "lvl1platformImages/rightcornerbrownstone.png"))

screen = pygame.display.set_mode((backgroundImage_Lvl1_rect.width, backgroundImage_Lvl1_rect.height))
screen_rect = screen.get_rect()

#main character
bobby = GameObject.Character(15,5,0,425,"bobby.png",screen)



# rendering levels
def renderLevel1():
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    platForm_group.draw(screen)

def renderLvl2():
    screen.blit(backgroundImage_LvL2, backgroundImage_LvL2_rect)
    pygame.display.flip()

def renderBossLvl():
    screen.blit(backgroundImage_LvL3, backgroundImage_LvL3_rect)
    pygame.display.flip()

running = True
# gameloop1
while running:
    renderLevel1()

    pygame.time.Clock().tick(18)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    bobby.playerMovementControl(keys)
    pygame.display.flip()


pygame.quit()
