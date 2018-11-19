import pygame
pygame.init()
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Goblin Chase')
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
game_on = True
while game_on:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            game_on = False
    pygame_screen.blit(background_image,[0,0])
    pygame.display.flip()

