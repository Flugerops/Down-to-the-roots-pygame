from pygame import sprite, image, transform
from layer import all_sprites_group, lightning_group, Spritesheet, enemy_group


class Lightning(sprite.Sprite):
    def __init__(self, mouse_x, mouse_y, intelligence) -> None:
        super().__init__()
        self.sprite = Spritesheet(image.load("assets/effects/lightning_strike.png").convert_alpha(), 1, 30)
        self.image = self.sprite.get_image(1, 104, 102, 5, (0, 0, 0))
        self.rect = self.image.get_rect(center=(mouse_x, mouse_y))
        self.damage = intelligence * 10 + 20
        self.lifetime = 15
        self.hit_enemies = []
        
    def update(self):
        self.image = self.sprite.play_animation(104, 102, 1, (0, 0, 0))
        self.image = transform.rotozoom(self.image, 0, 4)
        self.image.set_colorkey((0,0,0))
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()
            
        hits = sprite.spritecollide(self, enemy_group, False, sprite.collide_mask)
        if hits:
            for hit in hits:
                if hit not in self.hit_enemies:
                    self.hit_enemies.append(hit)
                    hit.get_damage(self.damage)

        