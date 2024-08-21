from random import randint
from pygame import Rect, draw
from pygame.sprite import Group, Sprite


all_sprites_group = Group()
bullet_group = Group()
enemy_group = Group()
obstacles = Group()


class SpriteGenerator:
    def __init__(self, image, quantity) -> None:
        self.image = image
        self.quantity = quantity
        
    def generate_sprites(self):
        for i in range(self.quantity):
            x = randint(0, 4000 - self.image.get_width())
            y = randint(0, 2500 - self.image.get_height())
            sprite = Sprite(obstacles)
            sprite.image = self.image
            sprite.rect = self.image.get_rect(topleft=(x, y))
            sprite.hitbox = Rect(x + 10, y + 10, self.image.get_width() - 20, self.image.get_height() - 20)
            obstacles.add(sprite)
            all_sprites_group.add(sprite)