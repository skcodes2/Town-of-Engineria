import pygame

class Death:
    
    def __init__(self,screen,playerObject):
        self.screen = screen
        self.bobby = playerObject

        #getting all match stats: 
        self.enemiesKilled = 0
        self.totalMoneyEarned = 0
        self.totalDamageTaken = 0
        self.totalJumps = 0
        self.axesChucked = 0
        self.lavaSpills = 0

        # images and fonts for death screen
        self.deathScreenTitle = pygame.font.Font("Fonts/mainScreen.ttf",70)
        self.deathScreenSubtitle = pygame.font.Font("Fonts/mainScreen.ttf",50)
        self.deathScreenText = pygame.font.Font("Fonts/mainScreen.ttf",25)

        self.deadBobby = pygame.image.load("bobbyBaseAnimation/bobbyDeath.png")
        self.deathScreenTitle = self.deathScreenTitle.render("YOU DIED!",True,(255,255,255))
        self.matchStatsTitle = self.deathScreenSubtitle.render("Match Stats",True,(255,255,255))
        self.optionsTitle = self.deathScreenSubtitle.render("Options",True,(255,255,255))
        self.playBtnImage = pygame.image.load("mainScreenImages/playbutton.png")
        self.exitBtnImage = pygame.image.load("mainScreenImages/exitbutton.png")


        self.enemiesKilledText = self.deathScreenText.render("{:<20}  {:<25}".format("Enemies Killed", self.enemiesKilled), True, (255, 255, 255))
        self.totalMoneyEarnedText = self.deathScreenText.render("{:<20}{:<25}".format("Money earned", self.totalMoneyEarned), True, (255, 255, 255))
        self.totalDamageTakenText = self.deathScreenText.render("{:<20} {:<25}".format("Damage taken", self.totalDamageTaken), True, (255, 255, 255))
        self.totalJumpsText = self.deathScreenText.render("{:<20}   {:<25}".format("Total Jumps", self.totalJumps), True, (255, 255, 255))
        self.totalAxesChucked = self.deathScreenText.render("{:<20}{:<25}".format("Axes Chucked", self.axesChucked), True, (255, 255, 255))
        self.totalLavaSpills = self.deathScreenText.render("{:<20}     {:<25}".format("Lava spills", self.lavaSpills), True, (255, 255, 255))


    def renderDeathScreen(self,mp,sp):
        self.screen.fill((0,0,0))
        self.totalElapsedTime = self.deathScreenText.render("Time played              " + str(mp) + ":" + str(sp),True,(255,255,255))

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.blit(self.deathScreenTitle, (400,40))
            self.screen.blit(self.deadBobby,(480,200))
            self.screen.blit(self.matchStatsTitle,(100,140))
            self.screen.blit(self.optionsTitle,(800,140))
            self.screen.blit(self.playBtnImage, (850,250))
            self.screen.blit(self.exitBtnImage, (850,310))

            #if event.type == pygame.MOUSEBUTTONDOWN and self.playBtnImage.rect.collidepoint(event.pos): 
            #    main.mainScreen = True
            #    running = False
            #if event.type == pygame.MOUSEBUTTONDOWN and self.exitBtn.rect.collidepoint(event.pos): 
            #    quit()


            self.screen.blit(self.enemiesKilledText,(100,230))
            self.screen.blit(self.totalMoneyEarnedText,(100,260))
            self.screen.blit(self.totalDamageTakenText,(100,290))
            self.screen.blit(self.totalJumpsText,(100,320))
            self.screen.blit(self.totalAxesChucked,(100,350))
            self.screen.blit(self.totalLavaSpills,(100,380))
            self.screen.blit(self.totalElapsedTime,(100,410))
            
            pygame.display.flip()