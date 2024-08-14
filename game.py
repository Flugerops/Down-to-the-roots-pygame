import pygame
from sys import exit
from settings import WIDTH, HEIGHT, FPS
from entities import Player
from layer import all_sprites_group, bullet_group


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Down to the roots")
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("assets/level/background.png").convert(), (WIDTH, HEIGHT))



player = Player(size=2.5, speed=7, w=21, h=61)
all_sprites_group.add(player)


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    # screen.blit(player.mask_image, (0,0))
    all_sprites_group.draw(screen)
    all_sprites_group.update()
    pygame.draw.rect(screen, "red", player.rect, width=2)
    pygame.display.update()
    clock.tick(FPS)