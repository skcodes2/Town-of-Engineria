import Bullet

class Enemy:
    def __init__(self, type, health):
        self.type = type
        self.health = health
    
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
        return Bullet(speed, damage)