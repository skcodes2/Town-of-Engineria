import pygame

class Character: 
    def __init__(self,speed,health,currentLocation):
        self.speed = speed
        self.health = health
        self.currentLocation = currentLocation

    def loseHp(self,damage): 
        self.health = self.health - damage

    

            



    
        