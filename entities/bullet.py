from math import sin, cos, pi, atan2, degrees
from pygame import sprite, image, Vector2, transform, key, K_w, K_s, K_d, K_a, Rect, mouse, time
from layer import enemy_group


class Bullet(sprite.Sprite):
    def __init__(self, x, y, speed, angle, lifetime, damage) -> None:
        super().__init__()
        self.image = transform.rotozoom(image.load("assets/effects/white_bullet.png").convert_alpha(), 0, 2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.angle = angle
        self.damage = damage
        self.speed = speed
        angle_degrees = degrees(self.angle)
        self.image = transform.rotate(self.image, -self.angle)
        self.rect = self.image.get_rect()
        self.x_vel = cos(self.angle * (2*pi/360)) * self.speed
        self.y_vel = sin(self.angle * (2*pi/360)) * self.speed
        self.lifetime = lifetime
        self.spawn_time = time.get_ticks()
        
        
    def bullet_move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        if time.get_ticks() - self.spawn_time > self.lifetime:
            self.kill()
            
    def update(self):
        self.bullet_move()
        hits = sprite.spritecollide(self, enemy_group, False, sprite.collide_mask)
        if hits:
            for hit in hits:
                hit.get_damage(self.damage)
                self.kill()