from sys import exit
from random import randint
from pygame import init, display, font, image, time, mixer, key, event, QUIT, quit, MOUSEBUTTONDOWN
from settings import WIDTH, HEIGHT, FPS, WHITE
from entities import Player, Enemy
from layer import all_sprites_group, Camera, SpriteGenerator, UI


class Game:
    """Main game class that run all game procces
    """
    def __init__(self):
        init()
        self.font = font.Font(None, 36)
        self.screen = display.set_mode((WIDTH, HEIGHT))
        display.set_caption("Down to the roots")
        self.clock = time.Clock()
        self.background = image.load(
            "assets/level/test_level.png").convert()
        self.stone1_img = image.load(
            "assets/obstacles/stone1.png").convert()
        self.tree_img = image.load("assets/obstacles/tree1.png")
        self.stone2_img = image.load("assets/obstacles/stone2.png")
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
        self.running = True
        self.background_music = mixer.Sound("assets/sounds/background_music.mp3")
        self.background_music.play(-1)
        self.background_music.set_volume(0.2)
        self.wave_sound = mixer.Sound("assets/sounds/new_wave.mp3")
        self.show_menu = False

    def enemy_kill(self):
        self.living_enemies -= 1

    def spawn_enemies(self):
        """Enemy spawner
        """
        hound_image = image.load("assets/enemies/hound_run.png")
        armored_skeleton = image.load(
            "assets/enemies/armored_skeleton.png")
        shield_skeleton = image.load(
            "assets/enemies/shield_skeleton.png")
        for _ in range(self.enemies_per_wave):
            enemy_type = randint(0, 2)
            if enemy_type == 0:
                enemy = Enemy(pos=(randint(0, 4000 - 67), randint(0, 2500 - 32)), size=2.5, speed=7, w=67, h=32, delay=50,
                              player=self.player, health=50, damage=20, sheet=hound_image, exp=randint(20, 80)*self.enemy_wave, on_death=self.enemy_kill)
            if enemy_type == 1:
                enemy = Enemy(pos=(randint(0, 4000 - 67), randint(0, 2500 - 32)), size=2.5, speed=5, w=75, h=64, delay=100,
                              player=self.player, health=250, damage=50, sheet=armored_skeleton, exp=randint(100, 300)*self.enemy_wave, on_death=self.enemy_kill)
            if enemy_type == 2:
                enemy = Enemy(pos=(randint(0, 4000 - 67), randint(0, 2500 - 32)), size=2.5, speed=3, w=32, h=64, delay=100,
                              player=self.player, health=500, damage=35, sheet=shield_skeleton, exp=randint(200, 400)*self.enemy_wave, on_death=self.enemy_kill)

        self.living_enemies = self.enemies_per_wave

    def game_over(self):
        """Game over screen
        """
        self.background_music.stop()
        text = self.font.render("Game Over", True, WHITE)
        waves_text = self.font.render(
            f"Survived for {self.enemy_wave} wave", True, WHITE)
        retry_text = self.font.render("Retry", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
        waves_rect = waves_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 20))
        self.retry_rect = retry_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 70))
        
        for sprite in all_sprites_group:
            sprite.kill()

        self.screen.fill((0, 0, 0))
        self.screen.blit(text, text_rect)
        self.screen.blit(waves_text, waves_rect)
        self.screen.blit(retry_text, self.retry_rect)

    def update(self):
        """
        Screen and events update/draw
        """
        
        keys = key.get_pressed()
        for ev in event.get():
            if ev.type == QUIT:
                quit()
                self.running = False
                exit()
            try:
                if ev.type == MOUSEBUTTONDOWN:
                    if self.retry_rect.collidepoint(ev.pos):
                        self.show_menu = True
            except: pass

        self.camera.custom_draw(player=self.player, screen=self.screen)
        self.player.handle_weapons(self.screen)
        all_sprites_group.update()
        self.ui.update(player=self.player, game=self)
        if self.living_enemies == 0:
            self.enemy_wave += 1
            self.enemies_per_wave += 2
            self.wave_sound.play()
            self.spawn_enemies()
        if self.player.dead:
            self.game_over()

    def run(self):
        """
        Method that loops the game
        """
        self.spawn_enemies()
        while self.running:
            self.update()
            if self.show_menu:
                break
            display.update()
            self.clock.tick(FPS)
