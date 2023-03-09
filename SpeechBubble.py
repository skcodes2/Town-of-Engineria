class SpeechBubble:
    text = ""
    def __init__(self,text):
        self.text = text
    
    def replaceText(self, text):
        self.text = text
    
    def closeBubble(self):
        self.text = ""
    