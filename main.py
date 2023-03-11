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


def renderLevel1():
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    platForm_group.draw(screen)
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
    renderLevel1()
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
