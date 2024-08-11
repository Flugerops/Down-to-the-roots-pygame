import pygame
from sys import exit
from settings import WIDTH, HEIGHT, FPS
from entities import Player


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Down to the roots")
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("assets/level/background.png").convert(), (WIDTH, HEIGHT))

player = Player(size=2.5, speed=7)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.pos)
    player.move()
    pygame.display.update()
    clock.tick(FPS)