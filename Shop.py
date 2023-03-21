import GameObject,pygame
class Shop:
    def __init__(self,screen,playerObject):
        self.screen = screen
        self.bobby = playerObject
        self.isOpen = False
        
        self.UpgradeFrame = pygame.image.load("backgroundImages/UpgradePage.png")
        self.playerFrame = pygame.image.load("backgroundImages/PlayerViewPage.png")
        self.shopBackground = pygame.image.load("backgroundImages/shopBg.png")
    def renderShop(self):
        while self.isOpen:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.isOpen = False
                self.screen.fill((0,0,0))
                self.screen.blit(self.shopBackground,(0,-12))
                self.screen.blit(self.UpgradeFrame,(1,15))
                self.screen.blit(self.UpgradeFrame,(810,15))
                self.screen.blit(self.playerFrame,(445,100))
                pygame.display.flip()

    def renderShopStats(self):
        pass