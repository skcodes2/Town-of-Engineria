import pygame
import GameObject
import Shop
import death

pygame.init()
# set up images and icons
pygame.display.set_caption("Main Menu")
pygame.display.set_icon(pygame.image.load("mainScreenImages/gameicon.png"))
# main screen background 
mainScreenImage = pygame.image.load('mainScreenImages/main.png'); 
mainScreenImageRect = mainScreenImage.get_rect()
# level 1 background
backgroundImage_LvL1 = pygame.image.load('backgroundImages/lvl1background.png')
backgroundImage_Lvl1_rect = backgroundImage_LvL1.get_rect()
# level 2 background
backgroundImage_LvL2 = pygame.image.load("backgroundImages/lvl2background.png")
backgroundImage_LvL2_rect = backgroundImage_LvL2.get_rect()
# level 3 background
backgroundImage_LvL3 = pygame.image.load("backgroundImages/lvl3background.png")
backgroundImage_LvL3_rect = backgroundImage_LvL3.get_rect()

# set size of window screen
screen = pygame.display.set_mode((1200, 575))
screen_rect = screen.get_rect()

# floor layout for level 1 (SPRITES)
platForm_group1 = pygame.sprite.Group()
platForm_floor1 = pygame.sprite.Group()
movingPlatform_group1 = pygame.sprite.Group()
lavapool1 = pygame.sprite.Group()
vertMovingPlatform_group1 = pygame.sprite.Group()


# orange floor platform
platForm_floor1.add(GameObject.PlatForms(987, 337, "lvl1platformImages/largeorangestone.png"))
# brown floor platforms
platForm_floor1.add(GameObject.PlatForms(0, 480, "lvl1platformImages/largebrownstone.png"))
platForm_floor1.add(GameObject.PlatForms(324, 550, "lvl1platformImages/largebrownstone.png"))
platForm_floor1.add(GameObject.PlatForms(648, 550, "lvl1platformImages/largebrownstone.png"))
platForm_floor1.add(GameObject.PlatForms(972, 550, "lvl1platformImages/largebrownstone.png"))
# brown pillar
platForm_floor1.add(GameObject.PlatForms(500, 350, "lvl1platformImages/brownpillar.png"))

# sky platform 1
platForm_group1.add(GameObject.PlatForms(380, 420, "lvl1platformImages/orangeplatform.png"))
# sky platform 2
platForm_group1.add(GameObject.PlatForms(520, 250, "lvl1platformImages/brownplatform.png"))
# sky platform 3
platForm_group1.add(GameObject.PlatForms(680, 350, "lvl1platformImages/orangeplatform.png"))
# sky platform 4
platForm_group1.add(GameObject.PlatForms(850, 370, "lvl1platformImages/orangeplatform.png"))

# moving sky platform
movingPlatform_group1.add(GameObject.MovingPlatForms(720, 470, 3, 600, 900, "lvl1platformImages/brownplatform.png"))

# left sky flat platform
platForm_group1.add(GameObject.PlatForms(10, 190, "lvl1platformImages/leftskyplatform.png"))
# right sky flat platform
platForm_group1.add(GameObject.PlatForms(640, 180, "lvl1platformImages/rightskyplatform.png"))
# left side border brown stone for collisions
platForm_floor1.add(GameObject.PlatForms(-2, -5,"lvl1platformImages/brownborderplatform.png"))
platForm_floor1.add(GameObject.PlatForms(-2, 235,"lvl1platformImages/brownborderplatform.png"))
platForm_floor1.add(GameObject.PlatForms(-2, 300,"lvl1platformImages/brownborderplatform.png"))
platForm_floor1.add(GameObject.PlatForms(-2, 500,"lvl1platformImages/brownborderplatform.png"))
# right side border brown stone for collisions
platForm_floor1.add(GameObject.PlatForms(1175, -40, "lvl1platformImages/brownborderplatform.png"))
platForm_floor1.add(GameObject.PlatForms(1175, 190, "lvl1platformImages/brownborderplatform.png"))
platForm_floor1.add(GameObject.PlatForms(1175, 431, "lvl1platformImages/brownborderplatform.png"))
# top side border brown stone for collisions
platForm_floor1.add(GameObject.PlatForms(0, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor1.add(GameObject.PlatForms(137, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor1.add(GameObject.PlatForms(274, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor1.add(GameObject.PlatForms(411, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor1.add(GameObject.PlatForms(548, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor1.add(GameObject.PlatForms(685, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor1.add(GameObject.PlatForms(822, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor1.add(GameObject.PlatForms(959, 0, "lvl1platformImages/brownflatplatform.png"))
platForm_floor1.add(GameObject.PlatForms(1096, 0, "lvl1platformImages/brownflatplatform.png"))
# lavapools
lavapool1.add(GameObject.LavaPool(320, 530, "lvl1platformImages/lava.png"))
lavapool1.add(GameObject.LavaPool(462, 530, "lvl1platformImages/lava.png"))
lavapool1.add(GameObject.LavaPool(605, 530, "lvl1platformImages/lava.png"))
lavapool1.add(GameObject.LavaPool(747, 530, "lvl1platformImages/lava.png"))
lavapool1.add(GameObject.LavaPool(889, 530, "lvl1platformImages/lava.png"))

# aesthetic images
destroyedbuilding1 = pygame.image.load("lvl1platformImages/destroyedbuilding1.png")
destroyedbuilding2 = pygame.image.load("lvl1platformImages/destroyedbuilding2.png")
destroyedbuilding3 = pygame.image.load("lvl1platformImages/destroyedbuilding3.png")
destroyedbuilding4 = pygame.image.load("lvl1platformImages/destroyedbuilding4.png")
destroyedcar = pygame.image.load("lvl1platformImages/destroyedcar.png")



#-----------------------------------------------------------------------------------^^^^^ Level 1 platforms

# floor layout for level 2 (SPRITES)
platForm_group2 = pygame.sprite.Group()
platForm_floor2 = pygame.sprite.Group()
movingPlatform_group2 = pygame.sprite.Group()
vertMovingPlatform_group2 = pygame.sprite.Group()
# ice floor platforms
platForm_floor2.add(GameObject.PlatForms(0, 500, "lvl2platformImages/largeplatform.png"))
platForm_floor2.add(GameObject.PlatForms(324, 500, "lvl2platformImages/largeplatform.png"))
platForm_floor2.add(GameObject.PlatForms(648, 500, "lvl2platformImages/largeplatform.png"))
platForm_floor2.add(GameObject.PlatForms(972, 350, "lvl2platformImages/largeplatform.png"))
vertMovingPlatform_group2.add(GameObject.VertMovingPlatForms(50,450,2,100,450, "lvl1platformImages/brownplatform.png"))


# Main Character (BOBBY) (speed, health, armour, x, y, image, screen, plat1, plat2)
bobby = GameObject.Character(5, 10, 0, 75, 380, "Axe1/axe1R.png", screen, platForm_group1, platForm_floor1, movingPlatform_group1, vertMovingPlatform_group1)
#bobby axe throw sound effect
bobbythrow = pygame.mixer.Sound("SoundEffects/axeThrow.mp3")

#Coin Collected
collected = pygame.mixer.Sound("SoundEffects/collectedCoin.mp3")
collected.set_volume(0.5)
#treasure collected
chestcollected = pygame.mixer.Sound("SoundEffects/chestOpenSound.mp3")
chestcollected.set_volume(0.5)
#key collected 
keyCollected = pygame.mixer.Sound("SoundEffects/keyGrab.mp3")
keyCollected.set_volume(0.5)
#enemy hit sound effect
enemyHitSound = pygame.mixer.Sound("SoundEffects/enemyHitSound.mp3")
enemyHitSound.set_volume(0.2)
#door open sound
doorOpen = pygame.mixer.Sound("SoundEffects/doorOpen.mp3")
doorOpen.set_volume(0.5)

#death sound 
lost = pygame.mixer.Sound("SoundEffects/deathSound.mp3")
lost.set_volume(5)

# bullet group 
bullet_group = pygame.sprite.Group()
bulletcooldown = 0
# enemy bullet group
enemy_bullets1 = pygame.sprite.Group()

# coins
coins1 = pygame.sprite.Group()

# Initialize Enemy Groups
enemies1 = pygame.sprite.Group()
enemies1.add(GameObject.Enemy(385, 334, screen, enemy_bullets1, "level1", coins1))
enemies1.add(GameObject.Enemy(855, 284, screen, enemy_bullets1, "level1", coins1))
enemies1.add(GameObject.Enemy(900, 94, screen, enemy_bullets1, "level1", coins1))
enemies1.add(GameObject.Enemy(90, 44, screen, enemy_bullets1, "level1", coins1))

#Shop Initialization
shop = Shop.Shop(screen,bobby)

#mainScreenRender
fontForMainScreen = pygame.font.Font("Fonts/mainScreen.ttf",50)
Title = fontForMainScreen.render("Bobby: The Town of Enginerea",True,(255,255,255))
playBtn = GameObject.GameObject(510,200,"mainScreenImages/playbutton.png")
exitBtn = GameObject.GameObject(510,260,"mainScreenImages/exitbutton.png")
helpBtn = GameObject.GameObject(510,320,"mainScreenImages/helpbutton.png")
playBtnImage = pygame.image.load("mainScreenImages/playbutton.png")
exitBtnImage = pygame.image.load("mainScreenImages/exitbutton.png")
helpBtnImage = pygame.image.load("mainScreenImages/helpbutton.png")

mainScreen = True
sb = GameObject.SpeechBubble(bobby.rect.x, bobby.rect.y, bobby, screen)
#mainScreen Music
pygame.display.set_caption("Main Menu")
pygame.mixer.init()
pygame.mixer.music.load("GameMusic/mainScreenMusic.mp3")
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

# help render loop
def renderHelpScreen():
    help = True
    screen.fill((255,255,255))
    while help:
        pygame.display.set_caption("Help Screen")
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                help = False

        pygame.display.flip()


# rendering the main screen
def renderMainScreen():
    global mainScreen
    while mainScreen:
        pygame.display.set_caption("Main Menu")
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        screen.blit(mainScreenImage,mainScreenImageRect)
        screen.blit(Title, (180,55))
        screen.blit(playBtnImage, (510,200))
        screen.blit(exitBtnImage, (510,260))
        screen.blit(helpBtnImage, (505,320))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and playBtn.rect.collidepoint(event.pos): 
                pygame.mixer.music.stop()
                pygame.time.delay(200)
                pygame.mixer.music.load("GameMusic/level1music.mp3")
                mainScreen = False
            if event.type == pygame.MOUSEBUTTONDOWN and exitBtn.rect.collidepoint(event.pos): 
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and helpBtn.rect.collidepoint(event.pos): 
                # place the render help here. 
                renderHelpScreen()

# death screen stuff
die = death.Death(screen,bobby)
startTime = pygame.time.get_ticks()

doorOpenRect = GameObject.GameObject(1040,237,"lvl1platformImages/doorOpen.png")
doorClosedImage = pygame.image.load("lvl1platformImages/doorClosed.png")
doorOpenImage = pygame.image.load("lvl1platformImages/doorOpen.png")

chestOpenImage =  GameObject.GameObject(1090,127,"chestImages/openedChest.png")
chestClosedImage = GameObject.GameObject(1090,137,"chestImages/closedChest.png")
chestKeyRect = GameObject.GameObject(120,150,"chestImages/chestKey.png")
chestKeyImage = GameObject.GameObject(120,150,"chestImages/chestKey.png")
numberOfKeys=[]
Level1keyAlive = True
Level1ChestAlive = True

#instructions to move 
playDialogue1 = True
#instructions to defeat enemies 
playDialogue2 = True
#says "Good Work!"
playDialogue3 = True
#instructions to open shop 
playDialogue4 = True
dialogueClock = 0

Level1 = True
# rendering levels 
def renderLevel1():
    if Level1:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        pygame.display.set_caption("Bobby: The Town of Enginerea | LEVEL 1")
        numberOfKeys.append(chestKeyImage)
        screen.blit(backgroundImage_LvL1, backgroundImage_Lvl1_rect)
        screen.blit(destroyedbuilding1, (30,187)) # next to booby
        screen.blit(destroyedbuilding2, (625,-135)) # top right corner 
        screen.blit(destroyedbuilding3, (335,450)) # in the lava 
        screen.blit(destroyedbuilding4, (30,-209)) # top left corner 
        screen.blit(destroyedcar, (23,88)) # car image on left sky platform
        #iif there are chests 
        if Level1ChestAlive:
            screen.blit(chestClosedImage.image,chestClosedImage.rect)
        #if there are no enemies, open the chest 
        elif len(enemies1)==0:
            screen.blit(chestOpenImage.image,chestOpenImage.rect)
        #if there are keys 
        if Level1keyAlive:
            screen.blit(chestKeyImage.image, chestKeyImage.rect)
        lavapool1.draw(screen)
        platForm_group1.draw(screen)
        platForm_floor1.draw(screen)
        screen.blit(doorClosedImage, (1040, 237))
        movingPlatform_group1.update()
        movingPlatform_group1.draw(screen)
        for enemy in enemies1:
            enemy.handleBehaviour(bobby)
        for coin in coins1:
            coin.animate()
        for bullet in bullet_group:
            bullet.bulletTravel()

        for bullet in enemy_bullets1:
            bullet.bulletHoming(bobby)

    else:
        print("function is false")

Level2 = True
def renderLevel2():
    if Level2:
        movingPlatform_group1.empty()
        pygame.display.set_caption("Bobby: The Town of Enginerea | LEVEL 2")
        screen.blit(backgroundImage_LvL2, backgroundImage_LvL2_rect)

        vertMovingPlatform_group2.update()
        vertMovingPlatform_group2.draw(screen)

        platForm_group2.draw(screen)
        platForm_floor2.draw(screen)
    else:
        print("function is false")

Level3 = True
def renderLevel3():
    if Level3:
        pygame.display.set_caption("Bobby: The Town of Enginerea | LEVEL 3")
        screen.blit(backgroundImage_LvL3, backgroundImage_LvL3_rect)
    else:
        print("function is false")

# Bobby's Stats (SPRITE) to set the images
bobbyStats = pygame.sprite.Group()
bobbyStats.add(GameObject.Stats(28, 17, "statsImages/heart.png"))
bobbyStats.add(GameObject.Stats(99, 20, "statsImages/strength.png"))
bobbyStats.add(GameObject.Stats(175, 22, "statsImages/coin.png"))

# set the font of label and the color
font = pygame.font.SysFont("arial.ttf", 24)

# rendering Bobby's Stats
def renderStats():
    heart = font.render(str(bobby.health), True, (255, 255, 255))
    strength = font.render(str(bobby.attack), True, (255, 255, 255))
    money = font.render(str(bobby.money), True, (255, 255, 255))
    statBG = pygame.Rect(24, 15, 222, 42)

    pygame.draw.rect(screen, (0,0,0), statBG)
    bobbyStats.draw(screen)
    screen.blit(heart, (70, 27))
    screen.blit(strength, (143, 27))
    screen.blit(money, (210, 27))

# Game Loop 1
current_level = 1
running = True
while running:
    renderMainScreen()
    pygame.time.Clock().tick(100)

    if bobby.health <= 0: 
        bobby.health = 10
        #resetting the game
        current_level = 1
        mainScreen = True

        endTime = pygame.time.get_ticks()
        elapsedTime = (endTime - startTime)/1000 #time in seconds.
        minutesPlayed = int(elapsedTime // 60)
        secondsPlayed = int(elapsedTime%60)
        die.renderDeathScreen(minutesPlayed,secondsPlayed)

    if current_level == 1:
        renderLevel1()
        renderStats()
        keys = pygame.key.get_pressed()

        enemyCollisions = pygame.sprite.spritecollide(bobby, enemies1, False)
        for collision in enemyCollisions:
            lost.play() 
            bobby.loseHp(1)
            die.totalDamageTaken += 1
            bobby.setLocation(40, 400)

        bulletCollisions = pygame.sprite.spritecollide(bobby, enemy_bullets1, False)
        for sprite in bulletCollisions:
            lost.play()
            bobby.loseHp(1)
            die.totalDamageTaken += 1
            bobby.setLocation(40, 400)
            sprite.kill()
            del sprite

        lavaCollisions = pygame.sprite.spritecollide(bobby, lavapool1, False)
        if len(lavaCollisions) > 0:
            lost.play()
            bobby.loseHp(1)
            die.totalDamageTaken += 1
            die.lavaSpills += 1
            bobby.setLocation(40,400)

        coinCollisions = pygame.sprite.spritecollide(bobby, coins1, False)
        for coin in coinCollisions:
            collected.play()
            bobby.gainMoney(coin.value)
            die.totalMoneyEarned += 20 
            coin.kill()
            del coin

        direction = bobby.playerMovementControl(keys)
        damage =1
        if keys[pygame.K_SPACE]:
            if bulletcooldown >= 20:
                if direction[1] == True:
                    bullet_group.add(GameObject.Bullet(8, damage, direction[1], direction[0].x - 25, direction[0].y + 20, screen))
                else:
                    bullet_group.add(GameObject.Bullet(8, damage, direction[1], direction[0].x + 35, direction[0].y + 20, screen))
                bulletcooldown = 0
                die.axesChucked += 1
            
        bulletcooldown += 1
        if bulletcooldown >= 20:
            bulletcooldown = 20

        collisions1 = pygame.sprite.groupcollide(bullet_group, platForm_floor1, True, False)
        collisions2 = pygame.sprite.groupcollide(bullet_group, platForm_group1, True, False)
        collisions3 = pygame.sprite.groupcollide(enemy_bullets1, platForm_floor1, True, False)
        collisions4 = pygame.sprite.groupcollide(enemy_bullets1, platForm_group1, True, False)
        collisions5 = pygame.sprite.groupcollide(bullet_group, enemy_bullets1, True, True)

        enemiesHit = pygame.sprite.groupcollide(enemies1, bullet_group, False, True)
        #if enemy gets hit by bullet
        for enemy in enemiesHit.keys():
            enemyHitSound.play()
            enemy.loseHp(bobby.attack)
            
        if len(enemies1) == 0 and bobby.rect.colliderect(doorOpenRect):
            sb.showsmallspeechbubble(bobby)
            sb.showText(bobby, "Press [ENTER]", 32.5, 65)
        #if chest key exist on level
        if Level1keyAlive: 
            #and collides with the key rectangle and bobby has 0 key  
            if bobby.rect.colliderect(chestKeyRect) and bobby.keys==0:
                #stop blitting key image and increase his key amount 
                Level1keyAlive = False
                keyCollected.play()
                bobby.keys+=1
        #if chest is closed and enemies are killed
        if Level1ChestAlive and len(enemies1)==0:
            #and if he collides with the closed chest with a key
            if bobby.rect.colliderect(chestClosedImage.rect) and bobby.keys>=1:
                #blit the opened chest 
                Level1ChestAlive = False
                chestcollected.play()
                bobby.money+=20
                bobby.keys-=1

    
    elif current_level == 2:
        renderLevel2()
        renderStats()
        keys = pygame.key.get_pressed()
        direction = bobby.playerMovementControl(keys)
        
        if keys[pygame.K_SPACE]:
            if bulletcooldown >= 20:
                if direction[1] == True:
                    bullet_group.add(GameObject.Bullet(8, 1, direction[1], direction[0].x - 25, direction[0].y + 18, screen))
                else:
                    bullet_group.add(GameObject.Bullet(8, 1, direction[1], direction[0].x + 35, direction[0].y + 18, screen))
                bulletcooldown = 0
                die.axesChucked += 1
        
        bulletcooldown += 1
        if bulletcooldown >= 20:
            bulletcooldown = 20
        for bullet in bullet_group:
            bullet.bulletTravel()

        collisions1 = pygame.sprite.groupcollide(bullet_group, platForm_floor2, True, False)
        collisions2 = pygame.sprite.groupcollide(bullet_group, platForm_group2, True, False)

    elif current_level == 3:
        renderLevel3()
        renderStats()
        
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            # renderShop()
            shop.isOpen=True
            bobby = shop.renderShop()
            damage = bobby.attack
            if current_level == 1:
                renderLevel1()
                renderStats()
            if current_level == 2:
                renderLevel2()
                renderStats()
            if current_level == 3:
                renderLevel3()
                renderStats()

        elif event.type == pygame.KEYDOWN and current_level == 1:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                if bobby.rect.colliderect(doorOpenRect) and len(enemies1) == 0:
                    pygame.mixer.music.stop()
                    pygame.time.delay(100)
                    doorOpen.play()
                    current_level += 1
                    Level1 = False
                    bobby.changeLevel(platForm_group2, platForm_floor2, movingPlatform_group2, vertMovingPlatform_group2)
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and current_level == 2:
            Level2 = False
            current_level += 1

    if current_level == 1 and playDialogue2 == True:
        if playDialogue1 == True:
            bobby.defaultSpeed = 0
            sb.showSpeechBubbleLevel1(bobby)
            sb.showText(bobby, "Move and jump with [ARROW]", 20, 130)
            sb.showText(bobby, "keys. Press [SPACE] key to", 20, 110)
            sb.showText(bobby, "attack and deflect enemy", 20, 90)
            sb.showText(bobby, "bullets.", 20, 70)
            dialogueClock += 1
        if dialogueClock >= 100:
            playDialogue1 = False
            playDialogue2 == True
            sb.showSpeechBubbleLevel1(bobby)
            sb.showText(bobby, "Defete all enemies to collect", 20, 130)
            sb.showText(bobby, "chests and proceed to next", 20, 110)
            sb.showText(bobby, "level.", 20, 90)
            dialogueClock += 1
        if dialogueClock == 200:
            playDialogue2 = False
            dialogueClock = 0
            bobby.defaultSpeed = 5
    
    if len(enemies1) == 0 and playDialogue3 == True:
        doorClosedImage = doorOpenImage
        sb.showsmallspeechbubble(bobby)
        sb.showText(bobby, "Good work!", 20, 70)
        dialogueClock += 1
        if dialogueClock == 50:
            playDialogue3 = False
            dialogueClock = 0
    
    if current_level == 2 and playDialogue4 == True:
        if playDialogue4 == True:
            bobby.defaultSpeed = 0
            sb.showSpeechBubbleLevel2(bobby)
            sb.showText(bobby, "Press [P] to open shop menu.", 170, 130)
            sb.showText(bobby, "You can upgrade weapons and", 170, 110)
            sb.showText(bobby, "stats by [LEFT] clicking the", 170, 90)
            sb.showText(bobby, "icons.", 170, 70)
            dialogueClock += 1
        if dialogueClock == 90:
            playDialogue4 = False
            dialogueClock = 0
            bobby.defaultSpeed = 5
            
    pygame.display.flip()
pygame.quit()
