from pygame import sprite, image, Vector2, transform, mixer
from layer import all_sprites_group, enemy_group, Spritesheet, obstacles


class Enemy(sprite.Sprite):
    def __init__(self, pos, size: float, speed: float, w: int, h: int, sheet, delay, health, damage, player, exp, on_death=None) -> None:
        super().__init__(all_sprites_group, enemy_group)
        self.enemy_sprite = Spritesheet(sheet, 1, delay)
        self.image = self.enemy_sprite.get_image(1, w, h, size, (0, 0, 0))
        self.rect = self.image.get_rect(center=pos)
        self.w = w
        self.h = h
        self.size = size
        self.alive = True
        self.flipped = False
        self.exp = exp
        self.health = health * (1 + player.level * 0.1)
        self.damage = damage * (1 + player.level * 0.1)
        self.player = player
        self.direction = Vector2()
        self.velocity = Vector2()
        self.speed = speed
        self.on_death = on_death
        self.position = Vector2(pos)
        self.avoid_cooldown = 0
        self.colliding = False

    def chase_player(self, player):
        self.colliding = False
        player_vector = Vector2(player.rect.center)
        enemy_vector = Vector2(self.rect.center)
        distance = self.vec_dist(player_vector, enemy_vector)
        if distance > 0:
            self.direction = (player_vector - enemy_vector).normalize()
        else:
            self.direction = Vector2()

        self.velocity = self.direction * self.speed

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.hitbox):
                avoid_direction = self.avoid_obstacle(obstacle)
                self.velocity = avoid_direction * self.speed
                self.colliding = True
                break
        
        if self.rect.colliderect(player.rect):
            player.get_damage(self.damage)
            self.velocity = -self.velocity * 5
            self.position += self.velocity * 10
            self.rect.centerx = self.position.x
            self.rect.centery = self.position.y

        self.position += self.velocity
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def get_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.alive = False
            self.kill()
            self.on_death()
            self.player.gain_exp(self.exp)

    def avoid_obstacle(self, obstacle):
        avoid_direction = (self.position - obstacle.hitbox.center).normalize()
        self.velocity += avoid_direction * (self.speed / 2)
        return avoid_direction


    @staticmethod
    def vec_dist(vector1, vector2):
        return (vector1 - vector2).magnitude()

    def update(self):

        if not self.colliding:
            if self.velocity.x < 0 and not self.flipped:
                self.flipped = True
            elif self.velocity.x > 0 and self.flipped:
                self.flipped = False

        self.image = self.enemy_sprite.play_animation(
            self.w, self.h, self.size, (0, 0, 0))
        if self.flipped:
            self.image = transform.flip(self.image, True, False)
            self.image.set_colorkey((0, 0, 0))

        self.chase_player(self.player)
