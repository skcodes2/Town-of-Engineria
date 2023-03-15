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
platForm_floor = pygame.sprite.Group()
# floor platform
platForm_floor.add(GameObject.PlatForms(0, 500, "lvl1platformImages/largebrownstone.png"))
platForm_floor.add(GameObject.PlatForms(324, 550, "lvl1platformImages/largebrownstone.png"))
platForm_floor.add(GameObject.PlatForms(648, 550, "lvl1platformImages/largebrownstone.png"))
platForm_floor.add(GameObject.PlatForms(972, 550, "lvl1platformImages/largebrownstone.png"))
# orange platforms
platForm_group1.add(GameObject.PlatForms(987, 337, "lvl1platformImages/mediumorangestone.png"))
# sky platform 1
platForm_group1.add(GameObject.PlatForms(180, 430, "lvl1platformImages/leftcornerorangestone.png"))
platForm_group1.add(GameObject.PlatForms(220, 430, "lvl1platformImages/rightcornerorangestone.png"))
# sky platform 2
platForm_group1.add(GameObject.PlatForms(320, 360, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group1.add(GameObject.PlatForms(360, 360, "lvl1platformImages/rightcornerbrownstone.png"))
# brown platform
platForm_group1.add(GameObject.PlatForms(500, 446, "lvl1platformImages/smallbrownstone.png"))
platForm_group1.add(GameObject.PlatForms(500, 350, "lvl1platformImages/smallbrownstone.png"))
#sky platform 4
platForm_group1.add(GameObject.PlatForms(680, 350, "lvl1platformImages/leftcornerorangestone.png"))
platForm_group1.add(GameObject.PlatForms(720, 350, "lvl1platformImages/rightcornerorangestone.png"))
#sky platform 5 
platForm_group1.add(GameObject.PlatForms(830, 380, "lvl1platformImages/leftcornerorangestone.png"))
platForm_group1.add(GameObject.PlatForms(870, 380, "lvl1platformImages/rightcornerorangestone.png"))
#sky platform 6
platForm_group1.add(GameObject.PlatForms(730, 470, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group1.add(GameObject.PlatForms(770, 470, "lvl1platformImages/rightcornerbrownstone.png"))
#left sky flat platform
platForm_group1.add(GameObject.PlatForms(14, 200, "lvl1platformImages/brownstoneplatform.png"))
platForm_group1.add(GameObject.PlatForms(152, 200, "lvl1platformImages/brownstoneplatform.png"))
platForm_group1.add(GameObject.PlatForms(289, 200, "lvl1platformImages/brownstoneplatform.png"))
platForm_group1.add(GameObject.PlatForms(340, 200, "lvl1platformImages/brownstoneplatform.png"))
#right sky flat platform
platForm_group1.add(GameObject.PlatForms(1048, 180, "lvl1platformImages/brownstoneplatform.png"))
platForm_group1.add(GameObject.PlatForms(910, 180, "lvl1platformImages/brownstoneplatform.png"))
platForm_group1.add(GameObject.PlatForms(772, 180, "lvl1platformImages/brownstoneplatform.png"))
platForm_group1.add(GameObject.PlatForms(634, 180, "lvl1platformImages/brownstoneplatform.png"))
#frame stone for collisions
#left side
platForm_floor.add(GameObject.PlatForms(-1, 498, "lvl1platformImages/framestone.png"))
platForm_floor.add(GameObject.PlatForms(-1, 361, "lvl1platformImages/framestone.png"))
platForm_floor.add(GameObject.PlatForms(-1, 224, "lvl1platformImages/framestone.png"))
platForm_floor.add(GameObject.PlatForms(-1, 87, "lvl1platformImages/framestone.png"))
platForm_floor.add(GameObject.PlatForms(-1, -50, "lvl1platformImages/framestone.png"))
#top side
platForm_floor.add(GameObject.PlatForms(14, 0, "lvl1platformImages/brownstoneplatform.png"))
platForm_floor.add(GameObject.PlatForms(151, 0, "lvl1platformImages/brownstoneplatform.png"))
platForm_floor.add(GameObject.PlatForms(288, 0, "lvl1platformImages/brownstoneplatform.png"))
platForm_floor.add(GameObject.PlatForms(425, 0, "lvl1platformImages/brownstoneplatform.png"))
platForm_floor.add(GameObject.PlatForms(562, 0, "lvl1platformImages/brownstoneplatform.png"))
platForm_floor.add(GameObject.PlatForms(699, 0, "lvl1platformImages/brownstoneplatform.png"))
platForm_floor.add(GameObject.PlatForms(836, 0, "lvl1platformImages/brownstoneplatform.png"))
platForm_floor.add(GameObject.PlatForms(973, 0, "lvl1platformImages/brownstoneplatform.png"))
platForm_floor.add(GameObject.PlatForms(1110, 0, "lvl1platformImages/brownstoneplatform.png"))
#right side
platForm_floor.add(GameObject.PlatForms(1185, 13, "lvl1platformImages/framestone.png"))
platForm_floor.add(GameObject.PlatForms(1185, 150, "lvl1platformImages/framestone.png"))
platForm_floor.add(GameObject.PlatForms(1185, 198, "lvl1platformImages/framestone.png"))
platForm_floor.add(GameObject.PlatForms(1185, 336, "lvl1platformImages/framestone.png"))
platForm_floor.add(GameObject.PlatForms(1185, 473, "lvl1platformImages/framestone.png"))
#platform on top of brown pillar
platForm_group1.add(GameObject.PlatForms(520, 270, "lvl1platformImages/leftcornerbrownstone.png"))
platForm_group1.add(GameObject.PlatForms(560, 270, "lvl1platformImages/rightcornerbrownstone.png"))


screen = pygame.display.set_mode((backgroundImage_Lvl1_rect.width, backgroundImage_Lvl1_rect.height))
screen_rect = screen.get_rect()

# main character
bobby = GameObject.Character(5, 5, 30, 440, "characterImages/bobbyR.png", screen, platForm_group1, platForm_floor)

#shop buttons: 
healthButtonRect = pygame.Rect(screen_rect.width/2 - 100,200,200,50)
attackButtonRect = pygame.Rect(screen_rect.width/2 - 100,400,200,50)

font = pygame.font.SysFont("copperplate", 24)
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
                        # play some 'bought' sound effect
                    elif bobby.money < 5:
                        # play some 'failure' sound effect. 
                        pass

                    # execute upgrade shield action here
                elif attackButtonRect.collidepoint(event.pos): 
                    if bobby.money >=5: 
                        bobby.attack +=1
                        bobby.money -=5
                        # play some 'bought' sound effect
                    elif bobby.money <5: 
                        # play some 'failure' sound effect. 
                        pass
                        
        pygame.display.flip()
       
# Bobby's stats
bobbyStats = pygame.sprite.Group()
bobbyStats.add(GameObject.Stats(20,20,"statsImages/heart.png"))
bobbyStats.add(GameObject.Stats(95,20,"statsImages/strength.png"))
bobbyStats.add(GameObject.Stats(180,22,"statsImages/coin.png"))


def renderStats():
    heart = font.render(str(bobby.health), True, (0, 0, 0))
    strength = font.render(str(bobby.attack), True, (0, 0, 0))
    money = font.render(str(bobby.money), True, (0, 0, 0))

    bobbyStats.draw(screen)
    screen.blit(heart, (70, 30))
    screen.blit(strength, (150,30))
    screen.blit(money,(227,30))


# rendering levels
def renderLevel1():
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    platForm_group1.draw(screen)
    platForm_floor.draw(screen)


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
    renderStats()
    pygame.time.Clock().tick(50)

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
