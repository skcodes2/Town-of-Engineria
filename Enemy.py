class Enemy:
    type = ""
    health = ""
    def __init__(self, type, health):
        self.type = type
        self.health = health
    
    def loseHp(self, damage):
        self.health = self.health - damage