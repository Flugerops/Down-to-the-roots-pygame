from pygame import sprite, image, Vector2, transform, key, K_w, K_s, K_d, K_a
from settings import PLAYER_X, PLAYER_Y
import math


class Player(sprite.Sprite):
    def __init__(self, size: float, speed: float) -> None:
        super().__init__()
        self.image = transform.rotozoom(image.load("assets/player/fire_idle_1.png").convert_alpha(), 0, size)
        self.pos = Vector2(PLAYER_X, PLAYER_Y)
        self.speed = speed
        
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
        if keys[K_a]:
            self.velocity_x = -self.speed
        
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)
        
        self.pos += Vector2(self.velocity_x, self.velocity_y)
    