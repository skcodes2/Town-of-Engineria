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
    def __init__(self, speed, damage, direction, x, y):
        super.__init__(x, y, "bullet.png")
        self.speed = speed
        self.damage = damage
        self.direction = direction


class SpeechBubble(GameObject):
    def __init__(self, text, x, y):
        self.text = text
        super.__init__(x, y, "speechBubbleImages/speechBubble.png")

    def replaceText(self, text):
        self.text = text

    def closeBubble(self):
        self.text = ""


class Character(GameObject):
    def __init__(self, speed, health, x, y, image_path, screen, platform1):
        super().__init__(x, y, image_path)
        self.speed = speed
        self.jumpingSpeed = 16
        self.health = health
        self.currentPosition = [x, y]
        self.platform1 = platform1

        self.nexImage = 0
        self.screen = screen
        self.walkingR = pygame.image.load("animationImages/walkingR.png")
        self.walkingL = pygame.image.load("animationImages/walkingL.png")
        self.standing = pygame.image.load("characterImages/bobby.png")
        self.inAir = False

    def loseHp(self, damage):
        self.health = self.health - damage

    def playerMovementControl(self, event):

        if all(key == 0 for key in pygame.key.get_pressed()) and self.inAir is False:
            self.rect = self.screen.blit(self.standing, tuple(
                self.currentPosition), (0, 0, 100, 76))
        elif event[pygame.K_RIGHT] and self.inAir is False:
            self.rect = self.screen.blit(self.walkingR, tuple(
                self.currentPosition), (101*self.nexImage, 0, 100, 76))
            self.currentPosition[0] += self.speed
            self.nexImage += 1
            if(self.nexImage == 3):
                self.nexImage = 0
        elif event[pygame.K_LEFT] and self.inAir is False:
            self.rect = self.screen.blit(self.walkingL, tuple(
                self.currentPosition), (101*self.nexImage, 0, 95, 76))
            self.currentPosition[0] -= self.speed
            self.nexImage += 1
            if(self.nexImage == 3):
                self.nexImage = 0

        if self.inAir is False and event[pygame.K_UP]:
            self.inAir = True

        if self.inAir is True and event[pygame.K_LEFT]:
            self.rect = self.screen.blit(self.walkingL, tuple(
                self.currentPosition), (101*2, 0, 95, 76))
            self.currentPosition[1] -= self.jumpingSpeed
            self.currentPosition[0] -= self.speed
            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10

        elif self.inAir is True and event[pygame.K_RIGHT]:
            self.rect = self.screen.blit(self.walkingR, tuple(
                self.currentPosition), (101*2, 0, 100, 76))
            self.currentPosition[1] -= self.jumpingSpeed
            self.currentPosition[0] += self.speed
            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10
        
        elif self.inAir is True:
            self.rect = self.screen.blit(self.standing, tuple(
                self.currentPosition), (0, 0, 100, 76))
            self.currentPosition[1] -= self.jumpingSpeed
            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10
        
        self.rect.width -= 50
        self.rect.x += 10

        vertcollisions = pygame.sprite.spritecollide(self,self.platform1,False)
        for sprite in vertcollisions:
            if self.rect.bottom >= sprite.rect.top - 10 and self.rect.bottom <= sprite.rect.top + 10:
                self.inAir = False
                self.jumpingSpeed = 16

        if len(vertcollisions) == 0 and self.inAir is False:
            self.inAir = True
            self.jumpingSpeed = 0



class Enemy(GameObject):
    def __init__(self, type, direction, health, x, y):
        self.type = type
        self.direction = direction
        self.health = health
        super.__init__(x, y, "enemy.png")

    def loseHp(self, damage):
        self.health = self.health - damage

    def shoot(self):
        speed = ""
        damage = ""
        if type == 1:
            speed = 5
            damage = 1
        elif type == 2:
            speed = 10
            damage = 2
        elif type == 3:
            speed = 15
            damage = 3
        # return a bullet object with correct direction and starting position with given speed


class PlatForms(GameObject):
    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)
