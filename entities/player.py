from math import sqrt
from pygame import sprite, image, Vector2, transform, key, K_w, K_s, K_d, K_a, Rect, mouse
from settings import PLAYER_X, PLAYER_Y
from layer import Spritesheet


class Player(sprite.Sprite):
    def __init__(self, size: float, speed: float, w: int, h: int) -> None:
        super().__init__()
        sprites = Spritesheet(image.load("assets/player/Thin.png").convert_alpha())
        self.image = sprites.get_image(7, w, h, size, (0,0,0))
        self.pos = Vector2(PLAYER_X, PLAYER_Y)
        self.speed = speed
        self.hitbox = self.image.get_rect(center=self.pos)
        self.flipped = False
        self.shoot = False
        self.shoot_cooldown = 0
    
    def move(self):
        self.velocity_x = 0
        self.velocity_y = 0
        
        keys = key.get_pressed()
        
        if keys[K_w]:
            self.velocity_y = -self.speed
        if keys[K_s]:
            self.velocity_y = self.speed
        if keys[K_d]:
            self.velocity_x = self.speed
            if self.flipped:
                self.image = transform.flip(self.image, True, False)
                self.image.set_colorkey((0, 0, 0))
                self.flipped = False
        if keys[K_a]:
            self.velocity_x = -self.speed
            if not self.flipped:
                self.image = transform.flip(self.image, True, False)
                self.image.set_colorkey((0, 0, 0))
                self.flipped = True
        if mouse.get_pressed() == (True, False, False):
            self.shoot = True
            self.shooting()
        
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= sqrt(2)
            self.velocity_y /= sqrt(2)
        
        self.pos += Vector2(self.velocity_x, self.velocity_y)
        self.hitbox.center = self.pos
        # self.rect.center = self.hitbox.center
    
    def shooting(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20