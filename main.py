import pygame
import GameObject

pygame.init()
# set up images and icons
pygame.display.set_caption("Bobby: The Town of Enginerea")
pygame.display.set_icon(pygame.image.load("gameicon.png"))
backgroundImage_LvL1 = pygame.image.load('backgroundImages/lvl1background.png')
backgroundImage_LvL2 = pygame.image.load("backgroundImages/lvl2background.png")
backgroundImage_LvL3 = pygame.image.load("backgroundImages/lvl3background.png")
backgroundImage_Lvl1_rect = backgroundImage_LvL1.get_rect()
backgroundImage_LvL2_rect = backgroundImage_LvL2.get_rect()
backgroundImage_LvL3_rect = backgroundImage_LvL3.get_rect()

# floor layout for level 1 (SPRITES)
platForm_group1 = pygame.sprite.Group()
platForm_floor = pygame.sprite.Group()
# orange floor platform
platForm_floor.add(GameObject.PlatForms(987, 337, "lvl1platformImages/largeorangestone.png"))
# brown floor platforms
platForm_floor.add(GameObject.PlatForms(0, 490, "lvl1platformImages/largebrownstone.png"))
platForm_floor.add(GameObject.PlatForms(324, 550, "lvl1platformImages/largebrownstone.png"))
platForm_floor.add(GameObject.PlatForms(648, 550, "lvl1platformImages/largebrownstone.png"))
platForm_floor.add(GameObject.PlatForms(972, 550, "lvl1platformImages/largebrownstone.png"))
# brown pillar
platForm_floor.add(GameObject.PlatForms(500, 350, "lvl1platformImages/brownpillar.png"))
# sky platform 1
platForm_group1.add(GameObject.PlatForms(180, 420, "lvl1platformImages/orangeplatform.png"))
# sky platform 2
platForm_group1.add(GameObject.PlatForms(320, 360, "lvl1platformImages/brownplatform.png"))
# sky platform 3
platForm_group1.add(GameObject.PlatForms(680, 350, "lvl1platformImages/orangeplatform.png"))
# sky platform 4
platForm_group1.add(GameObject.PlatForms(850, 380, "lvl1platformImages/orangeplatform.png"))
# sky platform 5
platForm_group1.add(GameObject.PlatForms(720, 470, "lvl1platformImages/brownplatform.png"))
# platform on top of brown pillar
platForm_group1.add(GameObject.PlatForms(520, 270, "lvl1platformImages/brownplatform.png"))
# left sky flat platform
platForm_group1.add(GameObject.PlatForms(10, 200, "lvl1platformImages/leftskyplatform.png"))
# right sky flat platform
platForm_group1.add(GameObject.PlatForms(640, 180, "lvl1platformImages/rightskyplatform.png"))
# left side border brown stone for collisions
platForm_floor.add(GameObject.PlatForms(-2, -5,"lvl1platformImages/brownborderplatform.png"))
platForm_floor.add(GameObject.PlatForms(-2, 235,"lvl1platformImages/brownborderplatform.png"))
platForm_floor.add(GameObject.PlatForms(-2, 300,"lvl1platformImages/brownborderplatform.png"))
platForm_floor.add(GameObject.PlatForms(-2, 500,"lvl1platformImages/brownborderplatform.png"))
# right side border brown stone for collisions
platForm_floor.add(GameObject.PlatForms(1175, -40, "lvl1platformImages/brownborderplatform.png"))
platForm_floor.add(GameObject.PlatForms(1175, 190, "lvl1platformImages/brownborderplatform.png"))
platForm_floor.add(GameObject.PlatForms(1175, 431, "lvl1platformImages/brownborderplatform.png"))
# top side border brown stone for collisions
platForm_floor.add(GameObject.PlatForms(0, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor.add(GameObject.PlatForms(137, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor.add(GameObject.PlatForms(274, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor.add(GameObject.PlatForms(411, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor.add(GameObject.PlatForms(548, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor.add(GameObject.PlatForms(685, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor.add(GameObject.PlatForms(822, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor.add(GameObject.PlatForms(959, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor.add(GameObject.PlatForms(1096, 0, "lvl1platformImages/brownflatplatform.png"))

# set background images for level 1
screen = pygame.display.set_mode((backgroundImage_Lvl1_rect.width, backgroundImage_Lvl1_rect.height))
screen_rect = screen.get_rect()

# Main Character (BOBBY) (speed, health, x, y, image, screen, plat1, plat2)
bobby = GameObject.Character(5, 5, 40, 350, "characterImages/bobbyR.png", screen, platForm_group1, platForm_floor)


# Bobby's Stats (SPRITE) to set the images
bobbyStats = pygame.sprite.Group()
bobbyStats.add(GameObject.Stats(30, 20, "statsImages/heart.png"))
bobbyStats.add(GameObject.Stats(105, 20, "statsImages/strength.png"))
bobbyStats.add(GameObject.Stats(190, 22, "statsImages/coin.png"))

# Shop Buttons (RECT) on shop window when P is pressed
healthButtonRect = pygame.Rect(50, 200, 300, 50)
attackButtonRect = pygame.Rect(50, 270, 300, 50)
# set the font of label and the color
font = pygame.font.SysFont("copperplate", 24)
titleFont = pygame.font.SysFont("copperplate", 42)
shield_label = font.render('Upgrade Health', True, (0, 0, 0))
attack_label = font.render('Upgrade Attack', True, (0, 0, 0))
upgrades_label = titleFont.render('PLAYER UPGRADES', True, (0,0,0))
gameSettings_label = titleFont.render('GAME SETTINGS', True, (0,0,0))
#shop sounds
success_sound = pygame.mixer.Sound("SoundEffects/successful.wav")
unsuccessful_sound = pygame.mixer.Sound("SoundEffects/unsuccessful.wav")



# bullet group 
bullet_group = pygame.sprite.Group()
bulletcooldown = 0

def renderShopStats():
    # Fill the stat surfaces with the background color
    screen.fill((255, 255, 255), (75, 30, 30, 30))
    screen.fill((255, 255, 255), (155, 30, 30, 30))
    screen.fill((255, 255, 255), (232, 30, 50, 30))

    # Render the updated stat values
    heart = font.render(str(bobby.health), True, (0, 0, 0))
    strength = font.render(str(bobby.attack), True, (0, 0, 0))
    money = font.render(str(bobby.money), True, (0, 0, 0))

    # Blit the updated stat values to the screen
    bobbyStats.draw(screen)
    screen.blit(heart, (75, 30))
    screen.blit(strength, (155, 30))
    screen.blit(money, (232, 30))



# rendering the shop
def renderShop():
    # set the caption
    pygame.display.set_caption("Game Menu")
    # fill entire screen white
    screen.fill((255, 255, 255))
    # draw rectangle of health button
    pygame.draw.rect(screen, (0, 255, 255), healthButtonRect)
    # draw rectangle of attack button
    pygame.draw.rect(screen, (0, 255, 255), attackButtonRect)
    # blit the labels inside rect
    screen.blit(shield_label, (healthButtonRect.x + 50, healthButtonRect.y + 15))
    screen.blit(attack_label, (attackButtonRect.x + 50, attackButtonRect.y + 15))
    screen.blit(upgrades_label, (50, 100))
    screen.blit(gameSettings_label, (800,100))
    

    running = True
    while running:
        renderShopStats()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.set_caption("Bobby: The Town of Enginerea")
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # event.button == 1 is a left click
                # check if the mouse click was inside a button
                if healthButtonRect.collidepoint(event.pos):
                    if bobby.money >= 5:
                        bobby.health += 1
                        bobby.money -= 5
                        success_sound.play()
                    elif bobby.money < 5:
                        unsuccessful_sound.play()
                        pass
                    # execute upgrade shield action here
                elif attackButtonRect.collidepoint(event.pos):
                    if bobby.money >= 5:
                        bobby.attack += 1
                        bobby.money -= 5
                        success_sound.play()
                    elif bobby.money < 5:
                        unsuccessful_sound.play()
                        pass
        pygame.display.flip()


# rendering levels


def renderLevel1():
    screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
    platForm_group1.draw(screen)
    platForm_floor.draw(screen)


def renderLevel2():
    screen.blit(backgroundImage_LvL2, backgroundImage_LvL2_rect)
    pygame.display.flip()


def renderlevel3():
    screen.blit(backgroundImage_LvL3, backgroundImage_LvL3_rect)
    pygame.display.flip()

# rendering Bobby's Stats


def renderStats():
    heart = font.render(str(bobby.health), True, (0, 0, 0))
    strength = font.render(str(bobby.attack), True, (0, 0, 0))
    money = font.render(str(bobby.money), True, (0, 0, 0))

    bobbyStats.draw(screen)
    screen.blit(heart, (75, 30))
    screen.blit(strength, (155, 30))
    screen.blit(money, (232, 30))



running = True
# gameloop1
while running:
    renderLevel1()
    renderStats()
    pygame.time.Clock().tick(100)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            renderShop()
    keys = pygame.key.get_pressed()
    direction = bobby.playerMovementControl(keys)
    
    if keys[pygame.K_SPACE]:
        if bulletcooldown >= 30:
            if direction[1] == True:
                bullet_group.add(GameObject.Bullet(8, 1, direction[1], direction[0].x - 25, direction[0].y + 18, screen))
            else:
                bullet_group.add(GameObject.Bullet(8, 1, direction[1], direction[0].x + 35, direction[0].y + 18, screen))
            bulletcooldown = 0
    bulletcooldown += 1
    if bulletcooldown >= 30:
        bulletcooldown = 30
    
    for bullet in bullet_group:
        bullet.bulletTravel()
    
    collisions1 = pygame.sprite.groupcollide(bullet_group, platForm_floor, True, False)
    collisions2 = pygame.sprite.groupcollide(bullet_group, platForm_group1, True, False)

    pygame.display.flip()

pygame.quit()
