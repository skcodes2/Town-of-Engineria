import pygame, GameObject

class Bullet(GameObject):
    def __init__(self, speed, damage, direction, x, y):
        super.__init__(x,y,"Bullet.png")
        self.speed = speed
        self.damage = damage
        self.direction = direction