import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y

class Bullet(GameObject):
    def __init__(self, speed, damage, goingLeft, x, y, screen):
        super().__init__(x, y, "characterAnimation/axeAnimation.png")
        self.speed = speed
        self.damage = damage
        self.goingLeft = goingLeft
        self.currentLocation = [x,y]
        self.travel = pygame.image.load("characterAnimation/axeAnimation.png")
        self.screen = screen
        self.animate = 0

    def bulletTravel(self):
        if self.goingLeft == True:
            self.rect = self.screen.blit(self.travel, tuple(self.currentLocation), (self.animate // 3 * 20, 0, 20, 20))
            self.currentLocation[0] -= self.speed
        else:
            self.rect = self.screen.blit(self.travel, tuple(self.currentLocation), (140 - self.animate // 3 * 20, 0, 20, 20))
            self.currentLocation[0] += self.speed
        self.animate += 1
        if self.animate == 24:
            self.animate = 0

class EnemyBullet(GameObject):
    def __init__(self, speed, damage, goingLeft, x, y, screen):
        super().__init__(x, y, "rockAnimation/rockthrow.png")
        self.speed = speed
        self.damage = damage
        self.goingLeft = goingLeft
        self.currentLocation = [x,y]
        self.travel = pygame.image.load("rockAnimation/rockthrow.png")
        self.screen = screen
        self.animate = 0
        self.age = 0

    def bulletTravel(self):
        if self.goingLeft == True:
            self.rect = self.screen.blit(self.travel, tuple(self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
            self.rect.height -= 5
            self.rect.y += 3
            self.currentLocation[0] -= self.speed
        else:
            self.rect = self.screen.blit(self.travel, tuple(self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
            self.rect.height -= 5
            self.rect.y += 3
            self.currentLocation[0] += self.speed
        self.animate += 1
        if self.animate == 24:
            self.animate = 0
        
    def bulletHoming(self, bobby):
        if self.goingLeft == True and self.age < 8:
            self.rect = self.screen.blit(self.travel, tuple(self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
            self.rect.height -= 5
            self.rect.y += 3
            self.currentLocation[0] -= self.speed
        elif self.goingLeft == False and self.age < 8:
            self.rect = self.screen.blit(self.travel, tuple(self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
            self.rect.height -= 5
            self.rect.y += 3
            self.currentLocation[0] += self.speed
        else:
            self.rect = self.screen.blit(self.travel, tuple(self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
            self.rect.height -= 5
            self.rect.y += 3
            if bobby.rect.centerx + 20 <= self.rect.centerx:
                self.currentLocation[0] -= self.speed
            elif bobby.rect.centerx - 20 >= self.rect.centerx:
                self.currentLocation[0] += self.speed
            else:
                pass
            
            if bobby.rect.centery + 20 <= self.rect.centery:
                self.currentLocation[1] -= self.speed
            elif bobby.rect.centery - 20 >= self.rect.centery:
                self.currentLocation[1] += self.speed
            else:
                pass
        self.animate += 1
        self.age += 1
        if self.animate == 24:
            self.animate = 0

class SpeechBubble(GameObject):
    def __init__(self, text, x, y):
        self.text = text
        super.__init__(x, y, "speechbubbleImages/speechbubble.png")

    def replaceText(self, text):
        self.text = text

    def closeBubble(self):
        self.text = ""

class Character(GameObject):
    def __init__(self, speed, health, x, y, image_path, screen, platform1, platform2):
        super().__init__(x, y, image_path)
        self.defaultSpeed = speed
        self.leftSpeed = speed
        self.rightSpeed = speed
        self.jumpingSpeed = 20
        self.money = 100
        self.attack = 1
        self.health = health
        self.currentPosition = [x, y]
        self.platform1 = platform1
        self.platform2 = platform2

        self.nexImage = 0
        self.screen = screen
        self.walkingR = pygame.image.load("characterAnimation/walkingR.png")
        self.walkingL = pygame.image.load("characterAnimation/walkingL.png")
        self.standingR = pygame.image.load("characterImages/bobbyR.png")
        self.standingL = pygame.image.load("characterImages/bobbyL.png")
        self.jumpingR = pygame.image.load("characterAnimation/jumpingR.png")
        self.jumpingL = pygame.image.load("characterAnimation/jumpingL.png")

        self.inAir = False
        self.standingLeft = False

    def loseHp(self, damage):
        self.health = self.health - damage

    def playerMovementControl(self, event):

        if not event[pygame.K_RIGHT] and not event[pygame.K_LEFT] and not event[pygame.K_UP] and self.inAir is False:
            if self.standingLeft:
                self.rect = self.screen.blit(self.standingL, tuple(
                    self.currentPosition), (0, 0, 70, 60))
            else:
                self.rect = self.screen.blit(self.standingR, tuple(
                    self.currentPosition), (0, 0, 70, 60))

        elif event[pygame.K_RIGHT] and self.inAir is False:
            if self.rightSpeed == 0:
                self.rect = self.screen.blit(self.standingR, tuple(
                    self.currentPosition), (0, 0, 70, 60))
            else:
                self.rect = self.screen.blit(self.walkingR, tuple(
                    self.currentPosition), (75*(self.nexImage // 4), 0, 76, 60))
                self.nexImage += 1
                if(self.nexImage == 16):
                    self.nexImage = 0
            self.currentPosition[0] += self.rightSpeed
            self.standingLeft = False

        elif event[pygame.K_LEFT] and self.inAir is False:
            if self.leftSpeed == 0:
                self.rect = self.screen.blit(self.standingL, tuple(
                    self.currentPosition), (0,0,70,60))
            else:
                self.rect = self.screen.blit(self.walkingL, tuple(
                    self.currentPosition), (74*(self.nexImage // 4), 0, 70, 60))
                self.nexImage += 1
                if(self.nexImage == 16):
                    self.nexImage = 0
            self.currentPosition[0] -= self.leftSpeed
            self.standingLeft = True

        if self.inAir is False and event[pygame.K_UP]:
            self.inAir = True

        if self.inAir is True and event[pygame.K_LEFT]:
            if self.jumpingSpeed > 0:
                self.rect = self.screen.blit(self.jumpingL, tuple(self.currentPosition), (125, 0, 65, 60))
            else:
                self.rect = self.screen.blit(self.jumpingL, tuple(self.currentPosition), (60, 0, 65, 60))
            self.standingLeft = True
            self.currentPosition[1] -= self.jumpingSpeed
            self.currentPosition[0] -= self.leftSpeed
            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10

        elif self.inAir is True and event[pygame.K_RIGHT]:
            if self.jumpingSpeed > 0:
                self.rect = self.screen.blit(self.jumpingR, tuple(self.currentPosition), (150, 0, 65, 60))
            else:
                self.rect = self.screen.blit(self.jumpingR, tuple(self.currentPosition), (215, 0, 65, 60))
            self.standingLeft = False
            self.currentPosition[1] -= self.jumpingSpeed
            self.currentPosition[0] += self.rightSpeed
            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10

        elif self.inAir is True:
            if self.standingLeft:
                if self.jumpingSpeed > 0:
                    self.rect = self.screen.blit(self.jumpingL, tuple(self.currentPosition), (130, 0, 65, 60))
                else:
                    self.rect = self.screen.blit(self.jumpingL, tuple(self.currentPosition), (60, 0, 65, 60))
            else:
                if self.jumpingSpeed > 0:
                    self.rect = self.screen.blit(self.jumpingR, tuple(self.currentPosition), (150, 0, 65, 60))
                else:
                    self.rect = self.screen.blit(self.jumpingR, tuple(self.currentPosition), (215, 0, 65, 60))
            self.currentPosition[1] -= self.jumpingSpeed
            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10

        self.rect.width -= 40
        self.rect.x += 20

        vertcollisions = pygame.sprite.spritecollide(
            self, self.platform1, False)
        vertcollisions2 = pygame.sprite.spritecollide(
            self, self.platform2, False)
        vertcollisions += vertcollisions2
        for sprite in vertcollisions:
            if self.rect.bottom >= sprite.rect.top - 10 and self.rect.bottom <= sprite.rect.top + 10:
                self.inAir = False
                self.jumpingSpeed = 20

        if len(vertcollisions) == 0 and self.inAir is False:
            self.inAir = True
            self.jumpingSpeed = 0

        horizcollisions = pygame.sprite.spritecollide(self, self.platform2, False)
        isLeftCollided = False
        isRightCollided = False
        for sprite in horizcollisions:
            if self.rect.right >= sprite.rect.left and self.rect.right <= sprite.rect.left + 25 and self.rect.bottom in range(sprite.rect.top + 22, sprite.rect.bottom + 10):
                self.rightSpeed = 0
                isRightCollided = True
            else:
                if isRightCollided == True:
                    pass
                else:
                    self.rightSpeed = self.defaultSpeed

            if self.rect.left <= sprite.rect.right and self.rect.left >= sprite.rect.right - 25 and self.rect.bottom in range(sprite.rect.top + 22, sprite.rect.bottom + 10):
                self.leftSpeed = 0
                isLeftCollided = True
            else:
                if isLeftCollided == True:
                    pass
                else:
                    self.leftSpeed = self.defaultSpeed
        
        if len(horizcollisions) == 0:
            self.rightSpeed = self.defaultSpeed
            self.leftSpeed = self.defaultSpeed
        
        return self.rect, self.standingLeft
    
    def changeLevel(self, platform1, platform2):
        self.platform1 = platform1
        self.platform2 = platform2

    def setLocation(self, x, y):
        self.currentPosition = [x,y]

class Enemy(GameObject):
    def __init__(self, x, y, screen, bulletGroup, type):
        self.isLeft = True
        super().__init__(x, y, "enemyImages/enemyL.png")
        self.attackR = pygame.image.load("enemyAnimation/enemyattackR.png")
        self.attackL = pygame.image.load("enemyAnimation/enemyattackL.png")
        self.screen = screen
        self.currentLocation = [x,y]
        self.animateL = 0
        self.animateR = 0
        self.animateDelay = 8
        self.bulletGroup = bulletGroup
        if type == "level1":
            self.sightRange = 300
            self.bulletSpeed = 6
            self.health = 3
        elif type == "level2":
            self.sightRange = 500
            self.bulletSpeed = 8
            self.health = 5
        elif type == "level3":
            self.sightRange = 800
            self.bulletSpeed = 12
            self.health = 8

    def handleBehaviour(self, bobby):

        if (abs(bobby.rect.centerx - self.rect.centerx) <= self.sightRange and abs(bobby.rect.centery - self.rect.centery <= self.sightRange) and bobby.rect.centerx < self.rect.centerx) or self.animateL != 0:
            self.animateR = 0
            if self.animateL // self.animateDelay == 0:
                self.rect = self.screen.blit(self.attackL, tuple(self.currentLocation), (295.2, 0, 73.8, 90)) # hard coded cuz animations arent all the same size for some reason
            
            elif self.animateL // self.animateDelay == 1:
                self.rect = self.screen.blit(self.attackL, tuple(self.currentLocation), (215, 0, 73.8, 90))
            
            elif self.animateL // self.animateDelay == 2:
                self.rect = self.screen.blit(self.attackL, tuple(self.currentLocation), (140, 0, 73.8, 90))

            elif self.animateL // self.animateDelay == 3:
                self.rect = self.screen.blit(self.attackL, tuple(self.currentLocation), (80, 0, 60, 90))

            elif self.animateL // self.animateDelay == 4:
                self.rect = self.screen.blit(self.attackL, tuple(self.currentLocation), (0, 0, 78, 90))

            self.animateL += 1
            if self.animateL == self.animateDelay * 4 + 2:
                self.bulletGroup.add(EnemyBullet(self.bulletSpeed, 1, True, self.rect.x - 16, self.rect.y + 60, self.screen))
            if self.animateL == self.animateDelay * 5:
                self.animateL = 0

        elif (abs(bobby.rect.centerx - self.rect.centerx) <= self.sightRange and abs(bobby.rect.centery - self.rect.centery <= self.sightRange) and bobby.rect.centerx >= self.rect.centerx) or self.animateR != 0:
            if self.animateR // self.animateDelay == 0:
                self.rect = self.screen.blit(self.attackR, tuple(self.currentLocation), (0, 0, 73.8, 90))
            
            elif self.animateR // self.animateDelay == 1:
                self.rect = self.screen.blit(self.attackR, tuple(self.currentLocation), (80, 0, 73.8, 90))
            
            elif self.animateR // self.animateDelay == 2:
                self.rect = self.screen.blit(self.attackR, tuple(self.currentLocation), (155, 0, 73.8, 90))

            elif self.animateR // self.animateDelay == 3:
                self.rect = self.screen.blit(self.attackR, tuple(self.currentLocation), (230, 0, 60, 90))

            elif self.animateR // self.animateDelay == 4:
                self.rect = self.screen.blit(self.attackR, tuple(self.currentLocation), (290, 0, 78, 90))

            self.animateR += 1
            if self.animateR == self.animateDelay * 4 + 2:
                self.bulletGroup.add(Enemy(self.bulletSpeed, 1, False, self.rect.x + 78, self.rect.y + 60, self.screen))
            if self.animateR == self.animateDelay * 5:
                self.animateR = 0

        elif bobby.rect.centerx < self.rect.centerx:
            self.rect = self.screen.blit(self.attackL, tuple(self.currentLocation), (295.2, 0, 73.8, 90))
        else:
            self.rect = self.screen.blit(self.attackR, tuple(self.currentLocation), (0,0,73.8,90))

        if self.health == 0:
            self.kill()
        
        self.rect.x += 15
        self.rect.y += 10
        self.rect.width -= 15
        self.rect.height -= 10


    def loseHp(self, damage):
        self.health = self.health - damage

class PlatForms(GameObject):
    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)

class Stats(GameObject):
    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)
        