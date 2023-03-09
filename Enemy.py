import Bullet, pygame

class Enemy:
    def __init__(self, type, direction, health, x, y):
        self.type = type
        self.direction = direction
        self.health = health
        super.__init__(x,y,"Enemy.png")
    
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