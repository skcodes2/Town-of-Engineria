import pygame

class SpeechBubble:
    def __init__(self,text):
        self.text = text
    
    def replaceText(self, text):
        self.text = text
    
    def closeBubble(self):
        self.text = ""
    