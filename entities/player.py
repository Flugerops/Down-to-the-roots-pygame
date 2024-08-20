from math import sqrt, degrees, atan2, pi
from pygame import sprite, image, Vector2, transform, key, K_w, K_s, K_d, K_a, Rect, mouse, mask, KEYUP, draw
from settings import WIDTH, HEIGHT
from layer import Spritesheet, bullet_group, all_sprites_group
from .bullet import Bullet



class Player(sprite.Sprite):
    def __init__(self, size: float, speed: float, w: int, h: int) -> None:
        super().__init__(all_sprites_group)
        self.idle = Spritesheet(image.load("assets/player/Thin.png").convert_alpha(), 1, 300)
        self.run = Spritesheet(image.load("assets/player/Run.png").convert_alpha(), 1, 50)
        self.w = w
        self.h = h
        self.size = size
        self.weapon_img = image.load("assets/weapons/2_1.png").convert()
        self.weapon_img = transform.rotozoom(self.weapon_img, 0, size)
        self.weapon_img.set_colorkey((0,0,0))
        self.image = self.idle.get_image(4, w, h, size, (0,0,0))
        self.pos = Vector2(WIDTH, HEIGHT)
        self.speed = speed
        self.rect = self.image.get_rect(center=self.pos)
        self.flipped = False
        self.running = False
        self.shoot = False
        self.shoot_cooldown = 0
        self.velocity_x = 0
        self.velocity_y = 0
        
        
    def move(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.velocity_y = -self.speed
            self.running = True
            
        if keys[K_s]:
            self.velocity_y = self.speed
            self.running = True
            
        if keys[K_d]:
            self.velocity_x = self.speed
            self.running = True
            if self.flipped:
                self.flipped = False
                
        if keys[K_a]:
            self.velocity_x = -self.speed
            self.running = True
            if not self.flipped:
                self.flipped = True
        
        if not all([keys[K_a] or keys[K_d] or keys[K_s] or keys[K_w]]):
            self.running = False
            
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

    
    # def handle_weapons(self, screen):
    #     mouse_x, mouse_y = mouse.get_pos()
    #     rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
    #     angle = (180 / pi) * -atan2(rel_y, rel_x)
    #     offset_x = self.rect.centerx - WIDTH // 2
    #     offset_y = self.rect.centery - HEIGHT // 2
    #     self.get_mouse_pos()
    #     weapon_copy = transform.rotate(self.weapon_img, angle + self.angle)
    #     screen.blit(weapon_copy, (offset_x+15-int(weapon_copy.get_width()/2), offset_y+25-int(weapon_copy.get_height()/2)))        
        
    def handle_weapons(self, screen):
        self.get_mouse_pos()
        if self.angle < -90 or self.angle > 90:
            weapon_copy = transform.flip(self.weapon_img, False, True)
            weapon_copy = transform.rotate(weapon_copy, -self.angle)
        else:
            weapon_copy = transform.rotate(self.weapon_img, -self.angle)
        offset_x = self.rect.centerx - WIDTH // 2 + 10
        offset_y = self.rect.centery - HEIGHT // 2 + 5
        screen.blit(weapon_copy, (self.rect.centerx - offset_x, self.rect.centery - offset_y))
    
    def get_mouse_pos(self):
        self.mouse_coords = mouse.get_pos()
        self.x_changed_mouse = (self.mouse_coords[0] - WIDTH // 2)
        self.y_changed_mouse = (self.mouse_coords[1] - HEIGHT // 2)
        self.angle = degrees(atan2(self.y_changed_mouse, self.x_changed_mouse))

    def shooting(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            bullet_pos = self.pos
            self.get_mouse_pos()
            self.bullet = Bullet(bullet_pos[0], bullet_pos[1], 50, self.angle, 500, damage=20)
            bullet_group.add(self.bullet)
            all_sprites_group.add(self.bullet)
            
    def update(self):
        if self.running:
            if self.flipped:
                self.image = transform.flip(self.run.play_animation(self.w, self.h, self.size, (0, 0, 0)), True, False)
                self.image.set_colorkey((0, 0, 0))
            else: 
                self.image = self.run.play_animation(self.w, self.h, self.size, (0, 0, 0))
        else:
            if self.flipped:
                self.image = transform.flip(self.idle.play_animation(self.w, self.h, self.size, (0, 0, 0)), True, False)
                self.image.set_colorkey((0, 0, 0))
            else:
                self.image = self.idle.play_animation(self.w, self.h, self.size, (0, 0, 0))
                
        self.move()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.shoot:
            self.shooting()