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
bobby = GameObject.Character(15,5,0,425,"bobby.png")

#animations 
walkingR = pygame.image.load("animationImages/walkingR.png")
walkingL = pygame.image.load("animationImages/walkingL.png")
walking_next = 0

# walking 
standLeft = False; 

def checkStand(): 
    if standLeft: 
        screen.blit(walkingL,tuple(bobby.currentPosition),(0,0,95,76))
    else:    
        screen.blit(walkingR,tuple(bobby.currentPosition),(0,0,100,76))

def walkingRight():
    screen.blit(walkingR,tuple(bobby.currentPosition),(101*walking_next,0,100,76))
    pygame.display.flip()

def walkingLeft():
    screen.blit(walkingL,tuple(bobby.currentPosition),(404 - 101*walking_next,0,95,76))
    pygame.display.flip()

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

#jumping
vel_y = 30
jump = False

# dictionary to keep track of which keys are currently being pressed
keys_pressed = {}
running = True


# gameloop1
while running:
    renderLevel1()

    pygame.time.Clock().tick(18)
    if(walking_next>3):
        walking_next=0
    walking_next +=1

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Add pressed keys to the dictionary
            keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            # Remove keys from the dictionary when they are released
            keys_pressed.pop(event.key, None)

    # Check which keys are currently pressed
    if pygame.K_LEFT in keys_pressed:
        bobby.currentPosition[0] -= bobby.speed
        walkingLeft()
        standLeft = True
    elif pygame.K_RIGHT in keys_pressed: 
        bobby.currentPosition[0] += bobby.speed
        walkingRight()
        standLeft = False

    userInp = pygame.key.get_pressed()
    if jump is False and userInp[pygame.K_UP]:
        jump = True

    if jump: 
        if standLeft: 
            walkingLeft()
        else: 
            walkingRight()

        bobby.currentPosition[1] -= vel_y
        vel_y -= 5
        if vel_y < -30: # or on a platform (implement later)
            jump = False
            vel_y = 30

    if len(keys_pressed) == 0 and jump is False: # if no keys are being pressed we don't want to running animation.
        checkStand()


    pygame.display.flip()


pygame.quit()
