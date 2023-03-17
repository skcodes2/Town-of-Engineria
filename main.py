import pygame
import GameObject

pygame.init()
# set up images and icons
pygame.display.set_caption("Bobby: The Town of Enginerea")
pygame.display.set_icon(pygame.image.load("gameicon.png"))
backgroundImage_LvL1 = pygame.image.load('backgroundImages/lvl1background.png')
backgroundImage_LvL2 = pygame.image.load("backgroundImages/lvl2background.png")
backgroundImage_LvL3 = pygame.image.load("backgroundImages/lvl3background.png")
backgroundImage_LvL1_rect = backgroundImage_LvL1.get_rect()
backgroundImage_LvL2_rect = backgroundImage_LvL2.get_rect()
backgroundImage_LvL3_rect = backgroundImage_LvL3.get_rect()

# floor layout for level 1 (SPRITES)
platform_group1 = pygame.sprite.Group()
platform_floor1 = pygame.sprite.Group()
# orange floor platform
platform_floor1.add(GameObject.PlatForms(987, 337, "lvl1platformImages/largeorangestone.png"))
# left side border brown stone for collisions
platform_floor1.add(GameObject.PlatForms(-2, -5, "lvl1platformImages/brownborderplatform.png"))
platform_floor1.add(GameObject.PlatForms(-2, 235, "lvl1platformImages/brownborderplatform.png"))
platform_floor1.add(GameObject.PlatForms(-2, 300, "lvl1platformImages/brownborderplatform.png"))
platform_floor1.add(GameObject.PlatForms(-2, 500, "lvl1platformImages/brownborderplatform.png"))
# right side border brown stone for collisions
platform_floor1.add(GameObject.PlatForms(1175, -40, "lvl1platformImages/brownborderplatform.png"))
platform_floor1.add(GameObject.PlatForms(1175, 190, "lvl1platformImages/brownborderplatform.png"))
platform_floor1.add(GameObject.PlatForms(1175, 431, "lvl1platformImages/brownborderplatform.png"))
# brown floor platforms
platform_floor1.add(GameObject.PlatForms(0, 490, "lvl1platformImages/largebrownstone.png"))
platform_floor1.add(GameObject.PlatForms(324, 550, "lvl1platformImages/largebrownstone.png"))
platform_floor1.add(GameObject.PlatForms(648, 550, "lvl1platformImages/largebrownstone.png"))
platform_floor1.add(GameObject.PlatForms(972, 550, "lvl1platformImages/largebrownstone.png"))
# brown pillar
platform_floor1.add(GameObject.PlatForms(500, 350, "lvl1platformImages/brownpillar.png"))
# sky platform 1
platform_group1.add(GameObject.PlatForms(180, 420, "lvl1platformImages/orangeplatform.png"))
# sky platform 2
platform_group1.add(GameObject.PlatForms(320, 360, "lvl1platformImages/brownplatform.png"))
# sky platform 3
platform_group1.add(GameObject.PlatForms(680, 350, "lvl1platformImages/orangeplatform.png"))
# sky platform 4
platform_group1.add(GameObject.PlatForms(850, 380, "lvl1platformImages/orangeplatform.png"))
# sky platform 5
platform_group1.add(GameObject.PlatForms(720, 470, "lvl1platformImages/brownplatform.png"))
# platform on top of brown pillar
platform_group1.add(GameObject.PlatForms(520, 270, "lvl1platformImages/brownplatform.png"))
# left sky flat platform
platform_group1.add(GameObject.PlatForms(10, 200, "lvl1platformImages/leftskyplatform.png"))
# right sky flat platform
platform_group1.add(GameObject.PlatForms(640, 180, "lvl1platformImages/rightskyplatform.png"))
# top side border brown stone for collisions
platform_floor1.add(GameObject.PlatForms(0, 0, "lvl1platformImages/brownflatplatform.png"))
platform_floor1.add(GameObject.PlatForms(137, 0, "lvl1platformImages/brownflatplatform.png"))
platform_floor1.add(GameObject.PlatForms(274, 0, "lvl1platformImages/brownflatplatform.png"))
platform_floor1.add(GameObject.PlatForms(411, 0, "lvl1platformImages/brownflatplatform.png"))
platform_floor1.add(GameObject.PlatForms(548, 0, "lvl1platformImages/brownflatplatform.png"))
platform_floor1.add(GameObject.PlatForms(685, 0, "lvl1platformImages/brownflatplatform.png"))
platform_floor1.add(GameObject.PlatForms(822, 0, "lvl1platformImages/brownflatplatform.png"))
platform_floor1.add(GameObject.PlatForms(959, 0, "lvl1platformImages/brownflatplatform.png"))
platform_floor1.add(GameObject.PlatForms(1096, 0, "lvl1platformImages/brownflatplatform.png"))


# floor layout for level 2 (SPRITES)

# set background images for level 1
screen = pygame.display.set_mode((backgroundImage_LvL1_rect.width, backgroundImage_LvL1_rect.height))
screen_rect = screen.get_rect()
# set background images for level 2
screen = pygame.display.set_mode((backgroundImage_LvL2_rect.width, backgroundImage_LvL2_rect.height))
screen_rect = screen.get_rect()
# set background images for level 3
screen = pygame.display.set_mode((backgroundImage_LvL3_rect.width, backgroundImage_LvL3_rect.height))
screen_rect = screen.get_rect()

# Main Character (BOBBY) (speed, health, x, y, image, screen, plat1, plat2)
bobby1 = GameObject.Character(5, 5, 60, 350, "characterImages/bobbyR.png", screen, platform_group1, platform_floor1)

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
upgrades_label = titleFont.render('PLAYER UPGRADES', True, (0, 0, 0))
gameSettings_label = titleFont.render('GAME SETTINGS', True, (0, 0, 0))
# shop sounds
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
    heart = font.render(str(bobby1.health), True, (0, 0, 0))
    strength = font.render(str(bobby1.attack), True, (0, 0, 0))
    money = font.render(str(bobby1.money), True, (0, 0, 0))
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
    screen.blit(gameSettings_label, (800, 100))
    # game loop
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
                    if bobby1.money >= 5:
                        bobby1.health += 1
                        bobby1.money -= 5
                        success_sound.play()
                    elif bobby1.money < 5:
                        unsuccessful_sound.play()
                        pass
                    # execute upgrade shield action here
                elif attackButtonRect.collidepoint(event.pos):
                    if bobby1.money >= 5:
                        bobby1.attack += 1
                        bobby1.money -= 5
                        success_sound.play()
                    elif bobby1.money < 5:
                        unsuccessful_sound.play()
                        pass
        pygame.display.flip()

# rendering level 1
def renderLevel1():
    screen.blit(backgroundImage_LvL1, backgroundImage_LvL1_rect)
    platform_group1.draw(screen)
    platform_floor1.draw(screen)
    pass
# rendering level 2
def renderLevel2():
    screen.blit(backgroundImage_LvL2, backgroundImage_LvL2_rect)
    pass
# rendering level 3
def renderlevel3():
    screen.blit(backgroundImage_LvL3, backgroundImage_LvL3_rect)
    pass
# rendering Bobby's Stats
def renderStats():
    heart = font.render(str(bobby1.health), True, (0, 0, 0))
    strength = font.render(str(bobby1.attack), True, (0, 0, 0))
    money = font.render(str(bobby1.money), True, (0, 0, 0))
    # draw on screen and blit the numbers
    bobbyStats.draw(screen)
    screen.blit(heart, (75, 30))
    screen.blit(strength, (155, 30))
    screen.blit(money, (232, 30))

current_level = 1
running = True
# gameloop1
while running:
    pygame.time.Clock().tick(120)
    if current_level == 1:
        renderLevel1()
        renderStats()
        keys = pygame.key.get_pressed()
        direction = bobby1.playerMovementControl(keys)

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
        collisions1 = pygame.sprite.groupcollide(bullet_group, platform_floor1, True, False)
        collisions2 = pygame.sprite.groupcollide(bullet_group, platform_group1, True, False)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            renderShop()
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        current_level += 1
        if current_level == 2:
            renderLevel2()
            renderStats()
    
    pygame.display.flip()
pygame.quit()
