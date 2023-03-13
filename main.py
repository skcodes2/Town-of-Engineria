import pygame
import GameObject

pygame.init()

pygame.display.set_caption("Bobby: The Town of Enginerea")
pygame.display.set_icon(pygame.image.load("gameicon.png"))
backgroundImage_LvL1 = pygame.image.load('backgroundImages/lvl1background.png')
backgroundImage_LvL2 = pygame.image.load("backgroundImages/lvl2background.png")
backgroundImage_LvL3 = pygame.image.load("backgroundImages/lvl3background.png")
backgroundImage_Lvl1_rect = backgroundImage_LvL1.get_rect()
backgroundImage_LvL2_rect = backgroundImage_LvL2.get_rect()
backgroundImage_LvL3_rect = backgroundImage_LvL3.get_rect()

platForm_group1 = pygame.sprite.Group()
# floor platform
platForm_group1.add(GameObject.PlatForms(0, 500, "lvl1platformImages/largebrownstone.png"))
platForm_group1.add(GameObject.PlatForms(324, 550, "lvl1platformImages/largebrownstone.png"))
platForm_group1.add(GameObject.PlatForms(648, 550, "lvl1platformImages/largebrownstone.png"))
platForm_group1.add(GameObject.PlatForms(972, 550, "lvl1platformImages/largebrownstone.png"))
# orange platforms
platForm_group1.add(GameObject.PlatForms(987, 337, "lvl1platformImages/mediumorangestone.png"))
# sky platform 1
platForm_group1.add(GameObject.PlatForms(135, 430, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group1.add(GameObject.PlatForms(175, 430, "lvl1platformImages/rightcornerbrownstone.png"))
# sky platform 2
platForm_group1.add(GameObject.PlatForms(290, 360, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group1.add(GameObject.PlatForms(330, 360, "lvl1platformImages/rightcornerbrownstone.png"))
# brown platform
platForm_group1.add(GameObject.PlatForms(450, 446, "lvl1platformImages/smallbrownstone.png"))
platForm_group1.add(GameObject.PlatForms(450, 350, "lvl1platformImages/smallbrownstone.png"))
#sky platform 3
platForm_group1.add(GameObject.PlatForms(620, 390, "lvl1platformImages/leftcornerorangestone.png"))
platForm_group1.add(GameObject.PlatForms(660, 390, "lvl1platformImages/rightcornerorangestone.png"))
#sky platform 4
platForm_group1.add(GameObject.PlatForms(750, 350, "lvl1platformImages/leftcornerorangestone.png"))
platForm_group1.add(GameObject.PlatForms(790, 350, "lvl1platformImages/rightcornerorangestone.png"))
#sky platform 5 
platForm_group1.add(GameObject.PlatForms(870, 380, "lvl1platformImages/leftcornerorangestone.png"))
platForm_group1.add(GameObject.PlatForms(910, 380, "lvl1platformImages/rightcornerorangestone.png"))
#sky platform 6
platForm_group1.add(GameObject.PlatForms(850, 500, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group1.add(GameObject.PlatForms(890, 500, "lvl1platformImages/rightcornerbrownstone.png"))
#sky platform 7
platForm_group1.add(GameObject.PlatForms(740, 450, "lvl1platformImages/leftcornerorangestone.png"))
platForm_group1.add(GameObject.PlatForms(780, 450, "lvl1platformImages/rightcornerorangestone.png"))


screen = pygame.display.set_mode((backgroundImage_Lvl1_rect.width, backgroundImage_Lvl1_rect.height))
screen_rect = screen.get_rect()

# main character
bobby = GameObject.Character(17, 5, 0, 425, "characterImages/bobbyR.png", screen, platForm_group1)

#shop buttons: 
healthButtonRect = pygame.Rect(screen_rect.width/2 - 100,200,200,50)
attackButtonRect = pygame.Rect(screen_rect.width/2 - 100,400,200,50)

font = pygame.font.SysFont(None, 24)
shield_label = font.render('Upgrade Health', True, (255, 255, 255))
attack_label = font.render('Upgrade Attack', True, (255, 255, 255))

# rendering the shop
def renderShop():
    pygame.display.set_caption("Item Shop")
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0, 0, 255), healthButtonRect)
    pygame.draw.rect(screen, (255, 0, 0), attackButtonRect)
    screen.blit(shield_label, (healthButtonRect.x + 10, healthButtonRect.y + 10))
    screen.blit(attack_label, (attackButtonRect.x + 10, attackButtonRect.y + 10))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.set_caption("Bobby: The Town of Enginerea")
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # event.button == 1 is a left click
                # check if the mouse click was inside a button
                if healthButtonRect.collidepoint(event.pos): 
                    if bobby.money >= 5: 
                        bobby.health += 1
                        bobby.money -=5
                        print(bobby.money)
                        print(bobby.health)
                        # play some 'bought' sound effect
                    elif bobby.money < 5:
                        # play some 'failure' sound effect. 
                        pass

                    # execute upgrade shield action here
                elif attackButtonRect.collidepoint(event.pos): 
                    if bobby.money >=5: 
                        bobby.attack +=1
                        bobby.money -=5
                        print(bobby.money)
                        print(bobby.attack)
                        # play some 'bought' sound effect
                    elif bobby.money <5: 
                        # play some 'failure' sound effect. 
                        pass
                        

        pygame.display.flip()
       


# rendering levels
def renderLevel1():
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    platForm_group1.draw(screen)


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

    pygame.time.Clock().tick(14)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            renderShop()


    keys = pygame.key.get_pressed()
    bobby.playerMovementControl(keys)
    pygame.display.flip()


pygame.quit()
