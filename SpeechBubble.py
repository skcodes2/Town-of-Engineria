import pygame, GameObject

class SpeechBubble(GameObject):
    def __init__(self,text, x, y):
        self.text = text
        super.__init__(x,y,"SpeechBubble.png")
    
    def replaceText(self, text):
        self.text = text
    
    def closeBubble(self):
        self.text = ""
    