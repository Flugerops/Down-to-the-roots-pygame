from math import sin, cos, pi
from pygame import sprite, image, Vector2, transform, key, K_w, K_s, K_d, K_a, Rect, mouse


class Bullet(sprite.Sprite):
    def __init__(self, x, y, angle, speed) -> None:
        super().__init__()
        self.image = transform(image.load("assets/effects/white_bullet").convert_alpha(), 0, 1.4)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y 
        self.speed = speed
        self.angle = angle
        self.x_vel = cos(self.angle * (2*pi/360)) * self.speed
        self.y_vel = sin(self.angle * (2*pi/360)) * self.speed
    
    