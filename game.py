import pygame
from sys import exit
from random import randint
from pygame.sprite import Group
from settings import WIDTH, HEIGHT, FPS
from entities import Player, Enemy
from layer import all_sprites_group, bullet_group, Camera, SpriteGenerator, obstacles, UI, enemy_group


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Down to the roots")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("assets/level/test_level.png").convert()
        self.stone1_img = pygame.image.load("assets/obstacles/stone1.png").convert()
        self.tree_img = pygame.image.load("assets/obstacles/tree1.png")
        self.stone2_img = pygame.image.load("assets/obstacles/stone2.png")
        self.stone_sprites = SpriteGenerator(self.stone1_img, 20)
        self.stone_sprites.generate_sprites()
        self.tree_sprites = SpriteGenerator(self.tree_img, 10)
        self.tree_sprites.generate_sprites()
        self.stone_sprites = SpriteGenerator(self.stone2_img, 3)
        self.stone_sprites.generate_sprites()
        self.player = Player(size=2.5, speed=7, w=64, h=61)
        self.ui = UI(screen=self.screen)
        self.camera = Camera(self.background)
        self.enemy_wave = 1
        self.enemies_per_wave = 5
        self.living_enemies = 0

    def enemy_kill(enemy):
        game.living_enemies -= 1
    
    def spawn_enemies(self):
        for i in range(self.enemies_per_wave):
            enemy = Enemy(pos=(randint(0, 4000 - 67), randint(0, 2500 - 32)), size=2.5, speed=5, w=67, h=32,
                          player=self.player, health=100, damage=20, fliped=True, exp=randint(20, 80), on_death=self.enemy_kill)
        self.living_enemies = self.enemies_per_wave

    def update(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.camera.custom_draw(player=self.player, screen=self.screen)
        self.player.handle_weapons(self.screen)
        all_sprites_group.update()
        self.ui.update(player=self.player, game=self)
        if self.living_enemies == 0:
            self.enemy_wave += 1
            self.enemies_per_wave += 2
            self.spawn_enemies()
        if self.player.dead:
            exit()

    def run(self):
        self.spawn_enemies()
        while True:
            self.update()
            pygame.display.update()
            self.clock.tick(FPS)

game = Game()
game.run()