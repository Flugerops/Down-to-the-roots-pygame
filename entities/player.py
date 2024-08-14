from math import sqrt, degrees, atan2
from pygame import sprite, image, Vector2, transform, key, K_w, K_s, K_d, K_a, Rect, mouse, mask, KEYUP
from settings import PLAYER_X, PLAYER_Y
from .bullet import Bullet
from layer import Spritesheet, bullet_group, all_sprites_group
from settings import WIDTH, HEIGHT


class Player(sprite.Sprite):
    def __init__(self, size: float, speed: float, w: int, h: int) -> None:
        super().__init__()
        sprites = Spritesheet(image.load("assets/player/Thin.png").convert_alpha())
        self.image = sprites.get_image(7, w, h, size, (0,0,0))
        self.pos = Vector2(PLAYER_X, PLAYER_Y)
        self.speed = speed
        self.rect = self.image.get_rect(center=self.pos)
        self.flipped = False
        self.shoot = False
        self.shoot_cooldown = 0
        # self.mask = mask.from_surface(self.image)
        # self.mask_image = self.mask.to_surface()
        
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
        else:
            self.shoot = False
        
            
        
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= sqrt(2)
            self.velocity_y /= sqrt(2)
        
        self.pos += Vector2(self.velocity_x, self.velocity_y)
        self.rect.center = self.pos

    
    # @staticmethod
    # def get_mouse_pos():
    #     mouse_coords = mouse.get_pos()
    #     x_changed_mouse = (mouse_coords[0] - (WIDTH // 2))
    #     y_changed_mouse = (mouse_coords[1] - (HEIGHT // 2))
    #     angle = int(degrees(atan2(y_changed_mouse, x_changed_mouse)))
    #     return (angle) % 360
    
    # def get_mouse_pos(self):
    #     self.mouse_coords = mouse.get_pos()
    #     self.x_changed_mouse = (self.mouse_coords[0] - (WIDTH // 2))
    #     self.y_changed_mouse = (self.mouse_coords[1] - (HEIGHT // 2))
    #     self.angle = int(degrees(atan2(self.y_changed_mouse, self.x_changed_mouse)))
    #     self.angle = (self.angle) % 360
    
    def shooting(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            bullet_pos = self.pos
            # self.get_mouse_pos()
            # self.angle = (self.mouse_coords[0], self.mouse_coords[1])
            # self.bullet = Bullet(bullet_pos[0], bullet_pos[1], self.angle, 50)
            mouse_x, mouse_y = mouse.get_pos()
            self.bullet = Bullet(bullet_pos[0], bullet_pos[1], 50, mouse_x, mouse_y, 500)
            bullet_group.add(self.bullet)
            all_sprites_group.add(self.bullet)
            
    def update(self):
        self.move()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.shoot:
            self.shooting()