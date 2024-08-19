from pygame import sprite, image, Vector2
from layer import all_sprites_group, enemy_group, Spritesheet


class Enemy(sprite.Sprite):
    def __init__(self, pos, size: float, speed: float, w: int, h: int, health, player) -> None:
        super().__init__(all_sprites_group, enemy_group)
        self.enemy_sprite = Spritesheet(image.load("assets/enemies/hound_run.png").convert_alpha(), 1, 300)
        self.image = self.enemy_sprite.get_image(1, w, h, size, (0,0,0))
        self.rect = self.image.get_rect(center=pos)
        self.alive = True
        self.health = health
        self.player = player
        self.direction = Vector2()
        self.velocity = Vector2()
        self.speed = speed
        self.position = Vector2(pos)
        
    def chase_player(self, player):
        player_vector = Vector2(player.rect.center)
        enemy_vector = Vector2(self.rect.center)
        distance = self.vec_dist(player_vector, enemy_vector)
        if distance > 0:
            self.direction = (player_vector - enemy_vector).normalize()
        else:
            self.direction = Vector2()
        
        self.velocity = self.direction * self.speed
        self.position += self.velocity
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y
    
    def get_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.alive = False
            self.kill()
    
    @staticmethod
    def vec_dist(vector1, vector2):
        return (vector1 - vector2).magnitude()
        
    def update(self):
        self.chase_player(self.player)