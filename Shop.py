import GameObject,pygame
class Shop:
    def __init__(self,screen,playerObject):
        self.screen = screen
        self.bobby = playerObject
        self.isOpen = False
        
        #fonts and backgrounds
        self.UpgradeFrame = pygame.image.load("shopImages/UpgradePage.png")
        self.playerFrame = pygame.image.load("shopImages/PlayerViewPage.png")
        self.shopBackground = pygame.image.load("shopImages/ShopBg.png")
        self.font = pygame.font.Font("Fonts/titles.otf", 35)
        self.Statsupgrades_label = self.font.render('Stats', True, (255,226,183))
        self.Equipmentupgrades_label = self.font.render('Equipment', True, (255,226,183))
        self.player_label = self.font.render("Bobby",True,(255,226,183))

        #Statsbuttons
        self.attackBtn = GameObject.GameObject(950,190,"Buttons/AttackUpgradeBtn.png")
        self.healthBtn = GameObject.GameObject(890,325,"Buttons/HealthUpgradeBtn.png")
        self.speedBtn = GameObject.GameObject(1020,325,"Buttons/SorcShoesUpgradeBtn.png")
        self.StatsFont = pygame.font.Font("Fonts/Stats.ttf",20)
        self.HealthTitle = self.StatsFont.render("Health +1",True,(0,0,0))
        self.DamageTitle = self.StatsFont.render("Damage +1",True,(0,0,0))
        self.SpeedTitle = self.StatsFont.render("Speed +1",True,(0,0,0))

        self.WoodTitle2 = self.StatsFont.render("Armour +3",True,(0,0,0))
        self.AxeTitle2 = self.StatsFont.render("Damage +1",True,(0,0,0))
        self.SteelTitle2 = self.StatsFont.render("Armour +5",True,(0,0,0))
        #Equipment Button
        self.axeBtn = GameObject.GameObject(140,190,"Buttons/AxeButton.png")
        self.shield1Btn = GameObject.GameObject(70,325,"Buttons/Shield1Button.png")
        self.shield2Btn = GameObject.GameObject(200,325,"Buttons/Shield2Button.png")

        #characters
        self.baseBobby = GameObject.GameObject(500,260,"shopImages/BaseBobby.png")

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

                self.screen.blit(self.Equipmentupgrades_label,(117,60))
                self.screen.blit(self.Statsupgrades_label,(965,60))
                self.screen.blit(self.player_label,(550,130))  
                #Buttons
                self.screen.blit(self.shield1Btn.image,self.shield1Btn.rect)
                self.screen.blit(self.shield2Btn.image,self.shield2Btn.rect)
                self.screen.blit(self.axeBtn.image,self.axeBtn.rect)
                self.screen.blit(self.attackBtn.image,self.attackBtn.rect)
                self.screen.blit(self.speedBtn.image,self.speedBtn.rect)
                self.screen.blit(self.healthBtn.image,self.healthBtn.rect) 
                self.screen.blit(self.HealthTitle,(915,305))
                self.screen.blit(self.DamageTitle,(980,170))
                self.screen.blit(self.SpeedTitle,(1055,305))

                self.screen.blit(self.WoodTitle2,(90,305))
                self.screen.blit(self.AxeTitle2,(160,170))
                self.screen.blit(self.SteelTitle2,(220,305))

                self.screen.blit(self.baseBobby.image,self.baseBobby.rect)
                
                pygame.display.flip()   
                
    def renderShopStats(self):
        pass