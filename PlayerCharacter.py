import pygame, GameObject

class PlayerCharacter(GameObject): 
    def __init__(self,speed,health,currentLocation,x,y,damage):
        super.__init__(x,y,"Character.png")
        self.speed = speed
        self.health = health
        self.currentLocation = currentLocation
        self.damage = damage

    def loseHp(self,damage): 
        self.health = self.health - damage


    

    

            



    
        