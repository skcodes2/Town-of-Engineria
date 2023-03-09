import pygame
import GameObject


pygame.init()

backgroundImage = pygame.image.load('town.png')
backgroundImage_rect = backgroundImage.get_rect()

screen = pygame.display.set_mode(
    (backgroundImage_rect.width, backgroundImage_rect.height))
screen_rect = screen.get_rect()
screen.blit(backgroundImage, backgroundImage_rect)
pygame.display.flip()

running = True
# gameloop
while running:
    screen.blit(backgroundImage, backgroundImage_rect)
    pygame.display.flip()
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
