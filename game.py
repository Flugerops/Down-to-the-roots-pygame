import pygame
from sys import exit
from pygame.sprite import Group
from settings import WIDTH, HEIGHT, FPS
from entities import Player, Enemy
from layer import all_sprites_group, bullet_group, Camera



pygame.init()

#TODO REMEMBER THAT TO GET SPAWN POS YOU NEED TO DIVIDE WIDTH AND HEIGHT BY 2 WIDTH // 2 HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Down to the roots")
clock = pygame.time.Clock()

background = pygame.image.load("assets/level/ground.png").convert()


player = Player(size=2.5, speed=7, w=64, h=61)
enemy = Enemy(pos=(500,600), size=2.5, speed=5, w=67, h=32, player=player, health=100, fliped=True)
camera = Camera(background)


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # all_sprites_group.draw(screen)
    camera.custom_draw(player=player, screen=screen)
    player.handle_weapons(screen)
    all_sprites_group.update()   
    # screen.blit(background, (0, 0))
    # screen.blit(player.mask_image, (0,0))
     
    
    pygame.display.update()
    clock.tick(FPS)